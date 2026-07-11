# Trading Dashboard

A Vue 3 + Vite trading monitoring dashboard for MetaTrader 5 (mock data phase).

## Tech Stack

- **Vue 3** (Composition API) + **Vite**
- **Pinia** - State management
- **Vue Router** - Routing
- **TailwindCSS** - Styling
- **ECharts** - Charts (vue-echarts)
- **Lucide Vue** - Icons
- **Day.js** - Date formatting

## Design

Dark Minimalism with Light theme option.
- Dark: `#0f0f11` bg, `#1a1a1d` surface, orange accent `#f97316 → #fb923c`
- Light: `#fafafa` bg, `#ffffff` surface
- Profit: green `#3ecf8e`, Loss: red `#ef4444`

## Project Structure

```
src/
├── assets/          CSS, fonts
├── components/
│   ├── common/      (Button, Card, Badge, etc.)
│   ├── charts/      (ECharts wrappers)
│   └── layout/      Sidebar, Navbar, MainLayout
├── views/
│   ├── overview/    Dashboard
│   ├── accounts/    User, MT5, Verification
│   ├── analytics/   PnL, Profit, Statistics, Reports, Export
│   ├── logs/        Candle, Trade, Audit, Errors
│   ├── alerts/      Rules, History, Channels
│   └── settings/    General, Database, Providers, Notifications
├── router/          Vue Router config
├── store/           Pinia stores (theme)
├── mock/            JSON mock data
└── App.vue
```

## Features

- Collapsible sidebar with submenus
- Dark/Light theme toggle (saved to localStorage)
- Dashboard with stat cards, MT5 account status, Top Movers, recent alerts
- Account management (users, MT5 accounts, verification)
- Analytics (PnL charts, profit charts, statistics, reports, export)
- Logs (candle, trade, audit, errors)
- Alerts & Rules (CRUD, history, notification channels)
- Settings (general, database, providers, notifications)

All data is **mock/dummy** - structured to resemble potential API responses for future backend integration.

## Getting Started

```bash
npm install
npm run dev
```

Open http://localhost:5173
