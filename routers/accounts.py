from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_conn

router = APIRouter(prefix="/api/accounts", tags=["accounts"])


class AccountCreate(BaseModel):
    login: str
    password: str
    broker: str
    server: str
    is_active: bool = True


class AccountUpdate(BaseModel):
    login: str | None = None
    password: str | None = None
    broker: str | None = None
    server: str | None = None
    is_active: bool | None = None


@router.get("/")
def list_accounts():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT a.*, 
               COALESCE(b.is_running, FALSE) as is_running,
               c.lot_size, c.percent_risk, c.confidence_threshold
        FROM mt5_accounts a
        LEFT JOIN bot_status b ON b.account_id = a.id
        LEFT JOIN bot_configs c ON c.account_id = a.id
        ORDER BY a.id
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    # Mask password
    result = []
    for r in rows:
        d = dict(r)
        d["password"] = "••••••••"
        result.append(d)
    return result


@router.post("/", status_code=201)
def create_account(data: AccountCreate):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO mt5_accounts (login, password, broker, server, is_active)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (data.login, data.password, data.broker, data.server, data.is_active))
        account_id = cur.fetchone()["id"]

        # Buat konfigurasi default
        cur.execute("""
            INSERT INTO bot_configs (account_id) VALUES (%s)
            ON CONFLICT (account_id) DO NOTHING
        """, (account_id,))

        # Buat status default
        cur.execute("""
            INSERT INTO bot_status (account_id, is_running)
            VALUES (%s, FALSE)
            ON CONFLICT (account_id) DO NOTHING
        """, (account_id,))

        conn.commit()
        return {"success": True, "id": account_id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


@router.put("/{account_id}")
def update_account(account_id: int, data: AccountUpdate):
    conn = get_conn()
    cur = conn.cursor()
    fields = []
    values = []
    if data.login is not None:
        fields.append("login = %s"); values.append(data.login)
    if data.password is not None:
        fields.append("password = %s"); values.append(data.password)
    if data.broker is not None:
        fields.append("broker = %s"); values.append(data.broker)
    if data.server is not None:
        fields.append("server = %s"); values.append(data.server)
    if data.is_active is not None:
        fields.append("is_active = %s"); values.append(data.is_active)

    if not fields:
        raise HTTPException(status_code=400, detail="Tidak ada field yang diupdate.")

    values.append(account_id)
    cur.execute(f"UPDATE mt5_accounts SET {', '.join(fields)} WHERE id = %s", values)
    conn.commit()
    cur.close()
    conn.close()
    return {"success": True}


@router.delete("/{account_id}")
def delete_account(account_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM mt5_accounts WHERE id = %s", (account_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"success": True}


@router.patch("/{account_id}/toggle")
def toggle_active(account_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE mt5_accounts SET is_active = NOT is_active WHERE id = %s
        RETURNING is_active
    """, (account_id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Akun tidak ditemukan.")
    return {"is_active": row["is_active"]}
