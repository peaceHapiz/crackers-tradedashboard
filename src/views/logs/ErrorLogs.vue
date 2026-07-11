<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { AlertTriangle, AlertCircle, Info } from 'lucide-vue-next'

const themeStore = useThemeStore()

const errors = ref([
  { id: 1, severity: 'error', message: 'MT5 connection timeout for account 11223344', timestamp: '2026-07-11 12:30:00' },
  { id: 2, severity: 'warning', message: 'High memory usage detected (85%)', timestamp: '2026-07-11 10:15:00' },
  { id: 3, severity: 'info', message: 'Backup completed successfully', timestamp: '2026-07-10 23:00:00' }
])

const severityConfig = {
  error: { icon: AlertCircle, color: 'text-loss', bg: 'bg-loss/10' },
  warning: { icon: AlertTriangle, color: 'text-accent', bg: 'bg-accent/10' },
  info: { icon: Info, color: 'text-blue-500', bg: 'bg-blue-500/10' }
}
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Error Logs</h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">System errors and warnings</p>
    </div>

    <div class="space-y-3">
      <div v-for="error in errors" :key="error.id" class="card p-4">
        <div class="flex items-start gap-3">
          <div class="p-2 rounded-md" :class="severityConfig[error.severity].bg">
            <component :is="severityConfig[error.severity].icon" class="w-4 h-4" :class="severityConfig[error.severity].color" />
          </div>
          <div class="flex-1">
            <p class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ error.message }}</p>
            <p class="text-xs mt-1" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ error.timestamp }}</p>
          </div>
          <span class="px-2 py-1 rounded text-xs font-medium capitalize" :class="[severityConfig[error.severity].bg, severityConfig[error.severity].color]">
            {{ error.severity }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
