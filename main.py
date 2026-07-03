import asyncio
import json
import os
from contextlib import asynccontextmanager
from datetime import datetime

import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from database import init_db, get_conn
from routers import accounts, config, logs, bot

load_dotenv()


# ── WebSocket Manager ──────────────────────────────────────────────
class ConnectionManager:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        self.active.remove(ws)

    async def broadcast(self, data: dict):
        dead = []
        for ws in self.active:
            try:
                await ws.send_json(data)
            except Exception:
                dead.append(ws)
        for ws in dead:
            self.active.remove(ws)


manager = ConnectionManager()
_last_log_id = 0


async def poll_new_logs():
    """Cek log baru setiap 2 detik, broadcast ke semua WS client."""
    global _last_log_id
    while True:
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("""
                SELECT l.*, a.login as account_login
                FROM trade_logs l
                LEFT JOIN mt5_accounts a ON a.id = l.account_id
                WHERE l.id > %s
                ORDER BY l.id ASC
                LIMIT 50
            """, (_last_log_id,))
            rows = cur.fetchall()
            cur.close()
            conn.close()

            for row in rows:
                d = dict(row)
                # Serialize datetime
                for k, v in d.items():
                    if isinstance(v, datetime):
                        d[k] = v.isoformat()
                await manager.broadcast({"type": "log", "data": d})
                _last_log_id = max(_last_log_id, d["id"])
        except Exception as e:
            print(f"[WS Poll Error] {e}")

        await asyncio.sleep(2)


# ── Lifespan ───────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    task = asyncio.create_task(poll_new_logs())
    yield
    task.cancel()


# ── App ────────────────────────────────────────────────────────────
app = FastAPI(title="TradeDashboard", lifespan=lifespan)

templates = Jinja2Templates(directory="templates")

app.include_router(accounts.router)
app.include_router(config.router)
app.include_router(logs.router)
app.include_router(bot.router)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        # Kirim 50 log terakhir saat connect
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            SELECT l.*, a.login as account_login
            FROM trade_logs l
            LEFT JOIN mt5_accounts a ON a.id = l.account_id
            ORDER BY l.created_at DESC
            LIMIT 50
        """)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        for row in reversed(rows):
            d = dict(row)
            for k, v in d.items():
                if isinstance(v, datetime):
                    d[k] = v.isoformat()
            await websocket.send_json({"type": "log", "data": d})

        # Keep alive
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
