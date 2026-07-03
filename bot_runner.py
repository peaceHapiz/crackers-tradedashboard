import subprocess
import psutil
import os
import sys
from datetime import datetime
from database import get_conn

# Simpan proses aktif di memory (key: account_id, value: Popen object)
_processes: dict[int, subprocess.Popen] = {}


def start_bot(account_id: int, script_path: str) -> dict:
    """Jalankan bot Python untuk akun tertentu."""
    if account_id in _processes:
        proc = _processes[account_id]
        if proc.poll() is None:  # masih jalan
            return {"success": False, "message": "Bot sudah berjalan."}

    if not os.path.exists(script_path):
        return {"success": False, "message": f"Script tidak ditemukan: {script_path}"}

    try:
        proc = subprocess.Popen(
            [sys.executable, script_path, str(account_id)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
        )
        _processes[account_id] = proc

        # Update DB
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO bot_status (account_id, is_running, pid, started_at)
            VALUES (%s, TRUE, %s, %s)
            ON CONFLICT (account_id) DO UPDATE
            SET is_running = TRUE, pid = %s, started_at = %s, stopped_at = NULL
        """, (account_id, proc.pid, datetime.now(), proc.pid, datetime.now()))
        conn.commit()
        cur.close()
        conn.close()

        return {"success": True, "message": f"Bot started. PID: {proc.pid}"}
    except Exception as e:
        return {"success": False, "message": str(e)}


def stop_bot(account_id: int) -> dict:
    """Hentikan bot Python untuk akun tertentu."""
    proc = _processes.get(account_id)
    killed = False

    if proc and proc.poll() is None:
        try:
            parent = psutil.Process(proc.pid)
            for child in parent.children(recursive=True):
                child.kill()
            parent.kill()
            killed = True
        except Exception:
            pass
        _processes.pop(account_id, None)

    # Coba kill by PID dari DB kalau proses tidak ada di memory
    if not killed:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT pid FROM bot_status WHERE account_id = %s", (account_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row and row["pid"]:
            try:
                p = psutil.Process(row["pid"])
                p.kill()
                killed = True
            except Exception:
                pass

    # Update DB
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE bot_status SET is_running = FALSE, pid = NULL, stopped_at = %s
        WHERE account_id = %s
    """, (datetime.now(), account_id))
    conn.commit()
    cur.close()
    conn.close()

    return {"success": True, "message": "Bot stopped." if killed else "Bot tidak sedang berjalan."}


def get_status(account_id: int) -> dict:
    """Cek status bot untuk akun tertentu."""
    proc = _processes.get(account_id)
    in_memory_running = proc is not None and proc.poll() is None

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bot_status WHERE account_id = %s", (account_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        # Sinkronisasi: kalau proses mati tapi DB masih running
        if row["is_running"] and not in_memory_running:
            pid = row["pid"]
            pid_alive = False
            if pid:
                try:
                    pid_alive = psutil.pid_exists(pid)
                except Exception:
                    pass
            if not pid_alive:
                conn2 = get_conn()
                cur2 = conn2.cursor()
                cur2.execute("""
                    UPDATE bot_status SET is_running = FALSE, stopped_at = %s
                    WHERE account_id = %s
                """, (datetime.now(), account_id))
                conn2.commit()
                cur2.close()
                conn2.close()
                return {"is_running": False, "pid": None}

        return {"is_running": row["is_running"], "pid": row["pid"]}

    return {"is_running": False, "pid": None}
