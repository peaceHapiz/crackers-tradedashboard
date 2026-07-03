from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_conn

router = APIRouter(prefix="/api/config", tags=["config"])


class ConfigUpdate(BaseModel):
    lot_size: float | None = None
    percent_risk: float | None = None
    confidence_threshold: float | None = None


@router.get("/{account_id}")
def get_config(account_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bot_configs WHERE account_id = %s", (account_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Config tidak ditemukan.")
    return dict(row)


@router.put("/{account_id}")
def update_config(account_id: int, data: ConfigUpdate):
    conn = get_conn()
    cur = conn.cursor()
    fields = []
    values = []
    if data.lot_size is not None:
        fields.append("lot_size = %s"); values.append(data.lot_size)
    if data.percent_risk is not None:
        fields.append("percent_risk = %s"); values.append(data.percent_risk)
    if data.confidence_threshold is not None:
        fields.append("confidence_threshold = %s"); values.append(data.confidence_threshold)

    if not fields:
        raise HTTPException(status_code=400, detail="Tidak ada field yang diupdate.")

    fields.append("updated_at = NOW()")
    values.append(account_id)

    cur.execute(f"""
        UPDATE bot_configs SET {', '.join(fields)}
        WHERE account_id = %s
    """, values)
    conn.commit()
    cur.close()
    conn.close()
    return {"success": True}
