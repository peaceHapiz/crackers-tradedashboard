<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Search } from 'lucide-vue-next'

const themeStore = useThemeStore()
const searchQuery = ref('')

const candles = ref([
  { symbol: 'EURUSD', timeframe: 'H1', open: 1.0850, high: 1.0895, low: 1.0842, close: 1.0875, timestamp: '2026-07-11 12:00:00' },
  { symbol: 'GBPUSD', timeframe: 'H1', open: 1.2650, high: 1.2685, low: 1.2638, close: 1.2672, timestamp: '2026-07-11 12:00:00' },
  { symbol: 'XAUUSD', timeframe: 'H4', open: 2350.50, high: 2365.20, low: 2348.00, close: 2360.80, timestamp: '2026-07-11 10:00:00' }
])
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Candle Logs</h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Market data history</p>
    </div>

    <div class="flex items-center gap-2 px-3 py-2 rounded-md border max-w-md"
      :class="themeStore.isDark ? 'bg-dark-surface border-dark-border' : 'bg-light-surface border-light-border'">
      <Search class="w-4 h-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
      <input v-model="searchQuery" type="text" placeholder="Search..."
        class="bg-transparent outline-none text-sm w-full"
        :class="themeStore.isDark ? 'text-dark-text placeholder:text-dark-text-muted' : 'text-light-text placeholder:text-light-text-muted'" />
    </div>

    <div class="card overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b" :class="themeStore.isDark ? 'border-dark-border bg-dark-bg' : 'border-light-border bg-light-bg'">
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Symbol</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">TF</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Open</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">High</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Low</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Close</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Time</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(candle, i) in candles" :key="i" class="border-b"
            :class="themeStore.isDark ? 'border-dark-border' : 'border-light-border'">
            <td class="py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ candle.symbol }}</td>
            <td class="py-3 px-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ candle.timeframe }}</td>
            <td class="py-3 px-4 text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ candle.open }}</td>
            <td class="py-3 px-4 text-right text-profit">{{ candle.high }}</td>
            <td class="py-3 px-4 text-right text-loss">{{ candle.low }}</td>
            <td class="py-3 px-4 text-right" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ candle.close }}</td>
            <td class="py-3 px-4 text-xs" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ candle.timestamp }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
