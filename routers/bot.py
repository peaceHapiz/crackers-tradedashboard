from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_conn
import bot_runner

router = APIRouter(prefix="/api/bot", tags=["bot"])


class BotStartRequest(BaseModel):
    script_path: str


@router.post("/{account_id}/start")
def start_bot(account_id: int, body: BotStartRequest):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM mt5_accounts WHERE id = %s", (account_id,))
    if not cur.fetchone():
        raise HTTPException(status_code=404, detail="Akun tidak ditemukan.")
    cur.close()
    conn.close()
    result = bot_runner.start_bot(account_id, body.script_path)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result


@router.post("/{account_id}/stop")
def stop_bot(account_id: int):
    result = bot_runner.stop_bot(account_id)
    return result


@router.get("/{account_id}/status")
def bot_status(account_id: int):
    return bot_runner.get_status(account_id)


@router.get("/status/all")
def all_status():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.id, a.login, a.broker,
               COALESCE(b.is_running, FALSE) as is_running,
               b.pid, b.started_at
        FROM mt5_accounts a
        LEFT JOIN bot_status b ON b.account_id = a.id
        ORDER BY a.id
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(r) for r in rows]
