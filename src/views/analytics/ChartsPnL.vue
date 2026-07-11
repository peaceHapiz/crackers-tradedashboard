<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Calendar, TrendingUp } from 'lucide-vue-next'
import mockData from '@/mock/dashboard.json'

const themeStore = useThemeStore()
const dailyPnL = ref(mockData.dailyPnL)

const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value)
}

const totalPnL = dailyPnL.value.reduce((sum, d) => sum + d.pnl, 0)
const winDays = dailyPnL.value.filter(d => d.pnl > 0).length
const lossDays = dailyPnL.value.filter(d => d.pnl < 0).length
</script>

<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          PnL Charts
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Daily and cumulative profit & loss analysis
        </p>
      </div>
      <div class="flex items-center gap-2">
        <button class="btn-secondary flex items-center gap-2">
          <Calendar class="w-4 h-4" />
          Last 7 Days
        </button>
      </div>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
      <div class="card p-4">
        <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Total PnL</p>
        <p class="text-2xl font-semibold mt-2" :class="totalPnL >= 0 ? 'text-profit' : 'text-loss'">
          {{ formatCurrency(totalPnL) }}
        </p>
      </div>
      <div class="card p-4">
        <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Win Days</p>
        <p class="text-2xl font-semibold mt-2 text-profit">{{ winDays }}</p>
      </div>
      <div class="card p-4">
        <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Loss Days</p>
        <p class="text-2xl font-semibold mt-2 text-loss">{{ lossDays }}</p>
      </div>
      <div class="card p-4">
        <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Win Rate</p>
        <p class="text-2xl font-semibold mt-2" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          {{ ((winDays / dailyPnL.length) * 100).toFixed(1) }}%
        </p>
      </div>
    </div>

    <!-- Chart Placeholder -->
    <div class="card p-6">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Daily PnL
        </h3>
        <div class="flex items-center gap-4 text-sm">
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-profit"></span>
            <span :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Profit</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-loss"></span>
            <span :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Loss</span>
          </div>
        </div>
      </div>
      <div class="h-80 flex items-center justify-center" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
        <div class="text-center">
          <TrendingUp class="w-12 h-12 mx-auto mb-2" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
          <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
            ECharts PnL visualization will be rendered here
          </p>
        </div>
      </div>
    </div>

    <!-- Daily PnL Table -->
    <div class="card overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b" :class="themeStore.isDark ? 'border-dark-border bg-dark-bg' : 'border-light-border bg-light-bg'">
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Date</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">PnL</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Cumulative</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="(day, index) in dailyPnL" 
            :key="day.date"
            class="border-b transition-colors"
            :class="themeStore.isDark ? 'border-dark-border hover:bg-dark-bg/50' : 'border-light-border hover:bg-light-bg/50'"
          >
            <td class="py-3 px-4" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
              {{ day.date }}
            </td>
            <td class="py-3 px-4 text-right font-medium" :class="day.pnl >= 0 ? 'text-profit' : 'text-loss'">
              {{ day.pnl >= 0 ? '+' : '' }}{{ formatCurrency(day.pnl) }}
            </td>
            <td class="py-3 px-4 text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              {{ formatCurrency(dailyPnL.slice(0, index + 1).reduce((sum, d) => sum + d.pnl, 0)) }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
