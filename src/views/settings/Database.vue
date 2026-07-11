<script setup>
import { useThemeStore } from '@/store/theme'
import { Database, Clock, HardDrive, RefreshCw } from 'lucide-vue-next'

const themeStore = useThemeStore()
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
        Database Settings
      </h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        Database management and backup
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="card p-4">
        <div class="flex items-center gap-3 mb-3">
          <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
            <Clock class="w-5 h-5" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
          </div>
          <div>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Last Backup</p>
            <p class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">2026-07-10 23:00:00</p>
          </div>
        </div>
      </div>

      <div class="card p-4">
        <div class="flex items-center gap-3 mb-3">
          <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
            <HardDrive class="w-5 h-5" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
          </div>
          <div>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Storage Used</p>
            <p class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">2.4 GB</p>
          </div>
        </div>
      </div>
    </div>

    <div class="card p-4">
      <h3 class="font-medium mb-4" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Backup</h3>
      <div class="flex items-center gap-4">
        <button class="btn-primary flex items-center gap-2">
          <RefreshCw class="w-4 h-4" />
          Backup Now
        </button>
        <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Retention: 30 days
        </p>
      </div>
    </div>
  </div>
</template>
