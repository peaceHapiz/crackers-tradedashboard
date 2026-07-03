import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/tradebot")


def get_conn():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # Tabel akun MT5
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mt5_accounts (
            id          SERIAL PRIMARY KEY,
            login       VARCHAR(50)  NOT NULL UNIQUE,
            password    VARCHAR(255) NOT NULL,
            broker      VARCHAR(100) NOT NULL,
            server      VARCHAR(100) NOT NULL,
            is_active   BOOLEAN      DEFAULT TRUE,
            created_at  TIMESTAMP    DEFAULT NOW()
        )
    """)

    # Tabel konfigurasi per-akun
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bot_configs (
            id                   SERIAL PRIMARY KEY,
            account_id           INTEGER REFERENCES mt5_accounts(id) ON DELETE CASCADE,
            lot_size             FLOAT   DEFAULT 0.01,
            percent_risk         FLOAT   DEFAULT 1.0,
            confidence_threshold FLOAT   DEFAULT 0.7,
            updated_at           TIMESTAMP DEFAULT NOW(),
            UNIQUE(account_id)
        )
    """)

    # Tabel log sinyal trading
    cur.execute("""
        CREATE TABLE IF NOT EXISTS trade_logs (
            id           SERIAL PRIMARY KEY,
            account_id   INTEGER REFERENCES mt5_accounts(id) ON DELETE SET NULL,
            symbol       VARCHAR(20),
            signal       VARCHAR(10),
            confidence   FLOAT,
            lot          FLOAT,
            price        FLOAT,
            status       VARCHAR(30) DEFAULT 'PENDING',
            message      TEXT,
            created_at   TIMESTAMP DEFAULT NOW()
        )
    """)

    # Tabel status bot per-akun
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bot_status (
            id          SERIAL PRIMARY KEY,
            account_id  INTEGER REFERENCES mt5_accounts(id) ON DELETE CASCADE UNIQUE,
            is_running  BOOLEAN   DEFAULT FALSE,
            pid         INTEGER,
            started_at  TIMESTAMP,
            stopped_at  TIMESTAMP
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("[DB] Tables initialized.")
