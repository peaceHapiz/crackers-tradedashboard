<script setup>
import { useThemeStore } from '@/store/theme'
import { BarChart2, TrendingUp, TrendingDown, Percent, Activity } from 'lucide-vue-next'

const themeStore = useThemeStore()

const statistics = [
  { label: 'Win Rate', value: '65.5%', icon: Percent, color: 'text-profit' },
  { label: 'Profit Factor', value: '2.34', icon: TrendingUp, color: 'text-profit' },
  { label: 'Average RR', value: '1:2.5', icon: Activity, color: 'text-accent' },
  { label: 'Max Drawdown', value: '8.2%', icon: TrendingDown, color: 'text-loss' },
  { label: 'Sharpe Ratio', value: '1.85', icon: BarChart2, color: 'text-profit' },
  { label: 'Total Trades', value: '156', icon: Activity, color: 'text-accent' }
]
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
        Statistics
      </h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        Performance metrics and trading statistics
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div 
        v-for="stat in statistics" 
        :key="stat.label"
        class="card p-6"
      >
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              {{ stat.label }}
            </p>
            <p class="text-3xl font-semibold mt-2" :class="stat.color">
              {{ stat.value }}
            </p>
          </div>
          <div class="p-3 rounded-md" :class="themeStore.isDark ? 'bg-dark-border' : 'bg-light-border'">
            <component :is="stat.icon" class="w-6 h-6" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
