import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('@/components/layout/MainLayout.vue'),
      children: [
        {
          path: '',
          name: 'overview',
          component: () => import('@/views/overview/DashboardView.vue')
        },
        {
          path: 'accounts',
          name: 'accounts',
          component: () => import('@/views/accounts/UserAccounts.vue')
        },
        {
          path: 'accounts/mt5',
          name: 'mt5-accounts',
          component: () => import('@/views/accounts/MT5Accounts.vue')
        },
        {
          path: 'accounts/verification',
          name: 'verification',
          component: () => import('@/views/accounts/Verification.vue')
        },
        {
          path: 'analytics',
          name: 'analytics',
          component: () => import('@/views/analytics/ChartsPnL.vue')
        },
        {
          path: 'analytics/profit',
          name: 'profit-charts',
          component: () => import('@/views/analytics/ChartsProfit.vue')
        },
        {
          path: 'analytics/statistics',
          name: 'statistics',
          component: () => import('@/views/analytics/Statistics.vue')
        },
        {
          path: 'analytics/reports',
          name: 'reports',
          component: () => import('@/views/analytics/Reports.vue')
        },
        {
          path: 'analytics/export',
          name: 'export',
          component: () => import('@/views/analytics/Export.vue')
        },
        {
          path: 'logs/candle',
          name: 'candle-logs',
          component: () => import('@/views/logs/CandleLogs.vue')
        },
        {
          path: 'logs/trade',
          name: 'trade-logs',
          component: () => import('@/views/logs/TradeLogs.vue')
        },
        {
          path: 'logs/audit',
          name: 'audit-logs',
          component: () => import('@/views/logs/AuditLogs.vue')
        },
        {
          path: 'logs/errors',
          name: 'error-logs',
          component: () => import('@/views/logs/ErrorLogs.vue')
        },
        {
          path: 'alerts',
          name: 'alerts',
          component: () => import('@/views/alerts/RuleList.vue')
        },
        {
          path: 'alerts/history',
          name: 'alert-history',
          component: () => import('@/views/alerts/AlertHistory.vue')
        },
        {
          path: 'alerts/channels',
          name: 'notification-channels',
          component: () => import('@/views/alerts/NotificationChannels.vue')
        },
        {
          path: 'settings',
          name: 'settings',
          component: () => import('@/views/settings/General.vue')
        },
        {
          path: 'settings/database',
          name: 'database-settings',
          component: () => import('@/views/settings/Database.vue')
        },
        {
          path: 'settings/providers',
          name: 'providers',
          component: () => import('@/views/settings/Providers.vue')
        },
        {
          path: 'settings/notifications',
          name: 'notification-settings',
          component: () => import('@/views/settings/Notifications.vue')
        }
      ]
    }
  ]
})

export default router
