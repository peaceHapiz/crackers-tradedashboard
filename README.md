# TradeDashboard

Dashboard monitoring tradebot MT5 berbasis FastAPI + Alpine.js + PostgreSQL.

## 🏗 Struktur
```
tradedashboard/
├── main.py           ← FastAPI app + WebSocket
├── database.py       ← Koneksi & init tabel PostgreSQL
├── bot_runner.py     ← Start/stop subprocess bot
├── dummy_bot.py      ← Bot simulasi untuk testing
├── routers/
│   ├── accounts.py   ← CRUD akun MT5
│   ├── config.py     ← Konfigurasi per-akun
│   ├── logs.py       ← Riwayat log signal
│   └── bot.py        ← API start/stop bot
├── templates/
│   └── index.html    ← UI Dashboard (Alpine.js + Tailwind)
├── .env              ← Konfigurasi DATABASE_URL
├── requirements.txt
└── start.bat         ← Shortcut jalankan di Windows
```

## ⚙️ Setup

### 1. Buat database PostgreSQL
```sql
CREATE DATABASE tradebot;
```

### 2. Edit `.env`
```
DATABASE_URL=postgresql://postgres:PASSWORD@localhost:5432/tradebot
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan dashboard
```bash
python main.py
# atau klik start.bat
```

Buka browser: http://localhost:8000

## 🚀 Cara Pakai

### Tambah Akun MT5
1. Buka tab **Akun MT5**
2. Klik **+ Tambah Akun**
3. Isi login, password, broker, server
4. Klik **Simpan**

### Set Konfigurasi Bot
1. Di Dashboard atau tab Akun, klik **⚙ Config**
2. Geser slider untuk lot size, percent risk, confidence threshold
3. Klik **Simpan**

### Start/Stop Bot
1. Di Dashboard, klik **Start** pada akun yang ingin dijalankan
2. Masukkan path ke script Python bot (misal: `C:\bot\livetrader.py`)
3. Klik **▶ Start**

Bot akan dijalankan sebagai subprocess terpisah.
Dashboard akan otomatis mendeteksi jika bot mati.

### Live Monitoring
- Tab **Dashboard** menampilkan live stream sinyal via WebSocket
- Update otomatis tiap 2 detik
- Tab **Log Signal** untuk riwayat lengkap dengan filter per akun

## 🔌 Integrasi Bot ke PostgreSQL

Dari bot Python Anda, log sinyal ke tabel `trade_logs`:

```python
import psycopg2

conn = psycopg2.connect("postgresql://postgres:pass@localhost:5432/tradebot")
cur  = conn.cursor()
cur.execute("""
    INSERT INTO trade_logs 
    (account_id, symbol, signal, confidence, lot, price, status, message)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""", (account_id, "EURUSD", "BUY", 0.87, 0.1, 1.0821, "EXECUTED", "Signal fired"))
conn.commit()
```

Konfigurasi bot dibaca dari tabel `bot_configs`:
```python
cur.execute("SELECT * FROM bot_configs WHERE account_id = %s", (account_id,))
config = cur.fetchone()
lot_size             = config["lot_size"]
percent_risk         = config["percent_risk"]
confidence_threshold = config["confidence_threshold"]
```

## 🧪 Testing dengan Dummy Bot
```bash
# Pastikan sudah ada akun di dashboard, catat id-nya
python dummy_bot.py 1   # jalankan dummy bot untuk account_id=1
```

## 📊 Skema Database

| Tabel | Deskripsi |
|---|---|
| `mt5_accounts` | Akun MT5 (login, password, broker, server) |
| `bot_configs` | Konfigurasi per akun (lot, risk, threshold) |
| `trade_logs` | Log sinyal trading |
| `bot_status` | Status running bot per akun |
