<script setup>
import { ref, computed, onMounted } from 'vue'
import { useThemeStore } from '@/store/theme'
import { TrendingUp, TrendingDown, Activity, AlertTriangle, Wallet, BarChart2, Percent, ArrowUpRight } from 'lucide-vue-next'
import mockData from '@/mock/dashboard.json'
import mockAccounts from '@/mock/accounts.json'
import mockAlerts from '@/mock/alerts.json'

const themeStore = useThemeStore()
const stats = ref(mockData.summary)
const equityCurve = ref(mockData.equityCurve)
const topMovers = ref(mockData.topMovers)
const accounts = ref(mockAccounts.accounts)
const recentAlerts = ref(mockAlerts.slice(0, 3))

const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value)
}

const formatPercent = (value) => {
  return value.toFixed(2) + '%'
}

const statCards = computed(() => [
  {
    label: 'Total Equity',
    value: formatCurrency(stats.value.totalEquity),
    icon: Wallet,
    change: '+2.5%',
    positive: true
  },
  {
    label: 'Total Balance',
    value: formatCurrency(stats.value.totalBalance),
    icon: BarChart2,
    change: '+1.2%',
    positive: true
  },
  {
    label: 'Floating PnL',
    value: formatCurrency(stats.value.totalFloatingPnL),
    icon: stats.value.totalFloatingPnL >= 0 ? TrendingUp : TrendingDown,
    change: stats.value.totalFloatingPnL >= 0 ? 'Profit' : 'Loss',
    positive: stats.value.totalFloatingPnL >= 0
  },
  {
    label: 'Avg Margin Level',
    value: formatPercent(stats.value.avgMarginLevel),
    icon: Percent,
    change: 'Safe',
    positive: true
  }
])

const connectionStatus = computed(() => {
  const connected = accounts.value.filter(a => a.status === 'connected').length
  return `${connected}/${accounts.value.length} Connected`
})
</script>

<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Dashboard Overview
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Monitor your trading accounts and performance
        </p>
      </div>
      <div class="flex items-center gap-2 px-3 py-1.5 rounded-full text-sm font-medium"
        :class="[
          'bg-profit/10 text-profit'
        ]">
        <Activity class="w-4 h-4" />
        {{ connectionStatus }}
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <div 
        v-for="stat in statCards" 
        :key="stat.label"
        class="card p-4"
      >
        <div class="flex items-start justify-between">
          <div>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              {{ stat.label }}
            </p>
            <p class="mt-2 text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
              {{ stat.value }}
            </p>
            <p 
              class="mt-1 text-xs font-medium"
              :class="stat.positive ? 'text-profit' : 'text-loss'"
            >
              {{ stat.change }}
            </p>
          </div>
          <div 
            class="p-2.5 rounded-md"
            :class="themeStore.isDark ? 'bg-dark-border' : 'bg-light-border'"
          >
            <component :is="stat.icon" class="w-5 h-5" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
          </div>
        </div>
      </div>
    </div>

    <!-- Charts & Tables Row -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Equity Curve Chart -->
      <div class="lg:col-span-2 card p-4">
        <h3 class="text-lg font-medium mb-4" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Equity Curve (7 Days)
        </h3>
        <div class="h-64 flex items-center justify-center" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
          <div class="text-center">
            <BarChart2 class="w-12 h-12 mx-auto mb-2" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              ECharts visualization will be rendered here
            </p>
          </div>
        </div>
      </div>

      <!-- Top Movers -->
      <div class="card p-4">
        <h3 class="text-lg font-medium mb-4" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Top Movers
        </h3>
        <div class="space-y-3">
          <div 
            v-for="mover in topMovers" 
            :key="mover.account"
            class="flex items-center justify-between p-3 rounded-md"
            :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'"
          >
            <div>
              <p class="font-medium text-sm" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
                {{ mover.broker }}
              </p>
              <p class="text-xs" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                {{ mover.account }}
              </p>
            </div>
            <div class="text-right">
              <p 
                class="font-medium text-sm"
                :class="mover.type === 'profit' ? 'text-profit' : 'text-loss'"
              >
                {{ mover.type === 'profit' ? '+' : '' }}{{ formatCurrency(mover.pnl) }}
              </p>
              <ArrowUpRight 
                class="w-4 h-4 ml-auto mt-1"
                :class="mover.type === 'profit' ? 'text-profit' : 'text-loss rotate-180'"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Accounts Table & Alerts -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Accounts Status -->
      <div class="lg:col-span-2 card p-4">
        <h3 class="text-lg font-medium mb-4" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          MT5 Accounts Status
        </h3>
        <div class="overflow-x-auto">
          <table class="w-full text-sm">
            <thead>
              <tr :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                <th class="text-left py-2 font-medium">Login</th>
                <th class="text-left py-2 font-medium">Broker</th>
                <th class="text-right py-2 font-medium">Balance</th>
                <th class="text-right py-2 font-medium">Equity</th>
                <th class="text-right py-2 font-medium">PnL</th>
                <th class="text-center py-2 font-medium">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr 
                v-for="account in accounts" 
                :key="account.id"
                class="border-t"
                :class="themeStore.isDark ? 'border-dark-border' : 'border-light-border'"
              >
                <td class="py-3 font-mono" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
                  {{ account.login }}
                </td>
                <td :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                  {{ account.broker }}
                </td>
                <td class="text-right font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
                  {{ formatCurrency(account.balance) }}
                </td>
                <td class="text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                  {{ formatCurrency(account.equity) }}
                </td>
                <td 
                  class="text-right font-medium"
                  :class="account.unrealizedPnL >= 0 ? 'text-profit' : 'text-loss'"
                >
                  {{ account.unrealizedPnL >= 0 ? '+' : '' }}{{ formatCurrency(account.unrealizedPnL) }}
                </td>
                <td class="text-center">
                  <span 
                    class="inline-flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium"
                    :class="[
                      account.status === 'connected' 
                        ? 'bg-profit/10 text-profit' 
                        : 'bg-loss/10 text-loss'
                    ]"
                  >
                    <span class="w-1.5 h-1.5 rounded-full"
                      :class="account.status === 'connected' ? 'bg-profit' : 'bg-loss'"
                    ></span>
                    {{ account.status }}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Recent Alerts -->
      <div class="card p-4">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-lg font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
            Recent Alerts
          </h3>
          <AlertTriangle class="w-5 h-5" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
        </div>
        <div class="space-y-3">
          <div 
            v-for="alert in recentAlerts" 
            :key="alert.id"
            class="p-3 rounded-md"
            :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'"
          >
            <div class="flex items-start justify-between">
              <div>
                <p class="font-medium text-sm" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
                  {{ alert.ruleName }}
                </p>
                <p class="text-xs mt-1" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                  {{ alert.condition }}
                </p>
              </div>
              <span 
                class="px-2 py-0.5 rounded text-xs font-medium"
                :class="[
                  alert.status === 'active' 
                    ? 'bg-profit/10 text-profit' 
                    : 'bg-loss/10 text-loss'
                ]"
              >
                {{ alert.status }}
              </span>
            </div>
            <p v-if="alert.lastTriggered" class="text-xs mt-2" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              Last: {{ alert.lastTriggered }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
