<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Search, Filter } from 'lucide-vue-next'
import mockTrades from '@/mock/trades.json'

const themeStore = useThemeStore()
const trades = ref(mockTrades)
const searchQuery = ref('')

const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value)
}
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
        Trade Logs
      </h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        History of all trading activity
      </p>
    </div>

    <div class="flex items-center gap-4">
      <div class="flex items-center gap-2 px-3 py-2 rounded-md border flex-1 max-w-md"
        :class="themeStore.isDark ? 'bg-dark-surface border-dark-border' : 'bg-light-surface border-light-border'">
        <Search class="w-4 h-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
        <input v-model="searchQuery" type="text" placeholder="Search trades..."
          class="bg-transparent outline-none text-sm w-full"
          :class="themeStore.isDark ? 'text-dark-text placeholder:text-dark-text-muted' : 'text-light-text placeholder:text-light-text-muted'" />
      </div>
      <button class="btn-secondary flex items-center gap-2">
        <Filter class="w-4 h-4" />
        Filter
      </button>
    </div>

    <div class="card overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b" :class="themeStore.isDark ? 'border-dark-border bg-dark-bg' : 'border-light-border bg-light-bg'">
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Order ID</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Symbol</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Type</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Lots</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Open</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Close</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">PnL</th>
            <th class="text-center py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="trade in trades" :key="trade.orderId"
            class="border-b transition-colors"
            :class="themeStore.isDark ? 'border-dark-border hover:bg-dark-bg/50' : 'border-light-border hover:bg-light-bg/50'">
            <td class="py-3 px-4 font-mono" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ trade.orderId }}</td>
            <td class="py-3 px-4" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ trade.symbol }}</td>
            <td class="py-3 px-4">
              <span class="px-2 py-1 rounded text-xs font-medium"
                :class="trade.type === 'BUY' ? 'bg-profit/10 text-profit' : 'bg-loss/10 text-loss'">
                {{ trade.type }}
              </span>
            </td>
            <td class="py-3 px-4 text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ trade.lots }}</td>
            <td class="py-3 px-4 text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ trade.openPrice }}</td>
            <td class="py-3 px-4 text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ trade.closePrice || '-' }}</td>
            <td class="py-3 px-4 text-right font-medium" :class="trade.pnl >= 0 ? 'text-profit' : 'text-loss'">
              {{ trade.pnl >= 0 ? '+' : '' }}{{ formatCurrency(trade.pnl) }}
            </td>
            <td class="py-3 px-4 text-center">
              <span class="px-2 py-1 rounded-full text-xs font-medium"
                :class="trade.status === 'closed' ? 'bg-dark-text-muted/10 text-dark-text-muted' : 'bg-accent/10 text-accent'">
                {{ trade.status }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
