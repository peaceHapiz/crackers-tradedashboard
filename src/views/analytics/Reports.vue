<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Calendar, Download } from 'lucide-vue-next'

const themeStore = useThemeStore()

const reports = ref([
  { id: 1, period: 'July 2026', trades: 45, profit: 2850.50, winRate: '68.9%' },
  { id: 2, period: 'June 2026', trades: 52, profit: -320.00, winRate: '51.9%' },
  { id: 3, period: 'May 2026', trades: 38, profit: 1420.00, winRate: '60.5%' }
])

const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value)
}
</script>

<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Reports
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Performance summary reports
        </p>
      </div>
      <button class="btn-primary flex items-center gap-2">
        <Calendar class="w-4 h-4" />
        Generate Report
      </button>
    </div>

    <div class="card overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b" :class="themeStore.isDark ? 'border-dark-border bg-dark-bg' : 'border-light-border bg-light-bg'">
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Period</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Trades</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Profit</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Win Rate</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="report in reports" :key="report.id"
            class="border-b" :class="themeStore.isDark ? 'border-dark-border' : 'border-light-border'">
            <td class="py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ report.period }}</td>
            <td class="py-3 px-4 text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ report.trades }}</td>
            <td class="py-3 px-4 text-right font-medium" :class="report.profit >= 0 ? 'text-profit' : 'text-loss'">
              {{ formatCurrency(report.profit) }}
            </td>
            <td class="py-3 px-4 text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ report.winRate }}</td>
            <td class="py-3 px-4 text-right">
              <button class="btn-secondary text-xs py-1.5">
                <Download class="w-3 h-3 inline mr-1" />
                Download
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
