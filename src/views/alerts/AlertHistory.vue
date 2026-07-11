<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Bell, Clock } from 'lucide-vue-next'

const themeStore = useThemeStore()

const history = ref([
  { id: 1, ruleName: 'Max Drawdown Alert', message: 'Drawdown exceeded 10%', triggeredAt: '2026-07-10 15:30:00', status: 'resolved' },
  { id: 2, ruleName: 'Daily Loss Limit', message: 'Daily loss reached $520', triggeredAt: '2026-07-08 18:45:00', status: 'resolved' },
  { id: 3, ruleName: 'Margin Call Warning', message: 'Margin level dropped to 145%', triggeredAt: '2026-07-05 09:20:00', status: 'dismissed' }
])

const statusColors = {
  resolved: 'bg-profit/10 text-profit',
  dismissed: 'bg-dark-text-muted/10 text-dark-text-muted',
  pending: 'bg-accent/10 text-accent'
}
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
        Alert History
      </h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        Previously triggered alerts
      </p>
    </div>

    <div class="space-y-3">
      <div v-for="alert in history" :key="alert.id" class="card p-4">
        <div class="flex items-start gap-3">
          <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
            <Bell class="w-4 h-4 text-accent" />
          </div>
          <div class="flex-1">
            <div class="flex items-center justify-between">
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ alert.ruleName }}</h3>
              <span class="px-2 py-1 rounded-full text-xs font-medium capitalize" :class="statusColors[alert.status]">
                {{ alert.status }}
              </span>
            </div>
            <p class="text-sm mt-1" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ alert.message }}</p>
            <div class="flex items-center gap-1.5 mt-2 text-xs" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              <Clock class="w-3 h-3" />
              {{ alert.triggeredAt }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
