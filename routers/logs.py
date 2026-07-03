from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from database import get_conn

router = APIRouter(prefix="/api/logs", tags=["logs"])


@router.get("/")
def get_logs(
    account_id: int | None = Query(None),
    limit: int = Query(100, le=500),
    offset: int = Query(0)
):
    conn = get_conn()
    cur = conn.cursor()

    where = ""
    params = []
    if account_id:
        where = "WHERE l.account_id = %s"
        params.append(account_id)

    params += [limit, offset]
    cur.execute(f"""
        SELECT l.*, a.login as account_login
        FROM trade_logs l
        LEFT JOIN mt5_accounts a ON a.id = l.account_id
        {where}
        ORDER BY l.created_at DESC
        LIMIT %s OFFSET %s
    """, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(r) for r in rows]


@router.get("/stats")
def get_stats(account_id: int | None = Query(None)):
    conn = get_conn()
    cur = conn.cursor()

    where = "WHERE account_id = %s" if account_id else ""
    params = [account_id] if account_id else []

    cur.execute(f"""
        SELECT
            COUNT(*) as total,
            COUNT(*) FILTER (WHERE signal = 'BUY')  as buy_count,
            COUNT(*) FILTER (WHERE signal = 'SELL') as sell_count,
            COUNT(*) FILTER (WHERE status = 'EXECUTED') as executed,
            COUNT(*) FILTER (WHERE status = 'REJECTED') as rejected,
            ROUND(AVG(confidence)::numeric, 4) as avg_confidence,
            DATE(created_at) as date
        FROM trade_logs
        {where}
        GROUP BY DATE(created_at)
        ORDER BY date DESC
        LIMIT 30
    """, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(r) for r in rows]


@router.delete("/clear")
def clear_logs(account_id: int | None = Query(None)):
    conn = get_conn()
    cur = conn.cursor()
    if account_id:
        cur.execute("DELETE FROM trade_logs WHERE account_id = %s", (account_id,))
    else:
        cur.execute("DELETE FROM trade_logs")
    conn.commit()
    cur.close()
    conn.close()
    return {"success": True}
