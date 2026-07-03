"""
dummy_bot.py — Simulasi bot trading untuk testing dashboard.
Jalankan TERPISAH dari dashboard.

Usage: python dummy_bot.py <account_id>
"""
import sys
import time
import random
import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/tradebot")

SYMBOLS  = ["EURUSD", "GBPUSD", "XAUUSD", "USDJPY", "BTCUSD"]
SIGNALS  = ["BUY", "SELL"]
STATUSES = ["EXECUTED", "EXECUTED", "EXECUTED", "REJECTED", "PENDING"]


def log_signal(account_id: int):
    conn = psycopg2.connect(DATABASE_URL)
    cur  = conn.cursor()

    symbol     = random.choice(SYMBOLS)
    signal     = random.choice(SIGNALS)
    confidence = round(random.uniform(0.5, 0.99), 4)
    lot        = round(random.uniform(0.01, 1.0), 2)
    price      = round(random.uniform(1.0, 2000.0), 5)
    status     = random.choice(STATUSES)

    cur.execute("""
        INSERT INTO trade_logs (account_id, symbol, signal, confidence, lot, price, status, message)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (account_id, symbol, signal, confidence, lot, price, status,
          f"Auto signal {signal} on {symbol} @ {price}"))

    conn.commit()
    cur.close()
    conn.close()
    print(f"[{datetime.now().isoformat()}] Logged: {signal} {symbol} conf={confidence}")


if __name__ == "__main__":
    account_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    print(f"[DummyBot] Running for account_id={account_id}")
    while True:
        try:
            log_signal(account_id)
        except Exception as e:
            print(f"[Error] {e}")
        time.sleep(random.uniform(3, 8))  # sinyal tiap 3-8 detik
