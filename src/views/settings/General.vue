<script setup>
import { useThemeStore } from '@/store/theme'
import { Sun, Moon, Globe, DollarSign } from 'lucide-vue-next'

const themeStore = useThemeStore()
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
        General Settings
      </h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        Customize your dashboard preferences
      </p>
    </div>

    <div class="space-y-4">
      <!-- Theme -->
      <div class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <component :is="themeStore.isDark ? Moon : Sun" class="w-5 h-5" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Theme</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                Choose your preferred color scheme
              </p>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <button 
              @click="themeStore.isDark || themeStore.toggleTheme()"
              class="px-4 py-2 rounded-l-md border text-sm font-medium transition-colors"
              :class="themeStore.isDark ? 'bg-accent text-white border-accent' : 'bg-transparent border-dark-border text-dark-text-muted'"
            >
              Dark
            </button>
            <button 
              @click="themeStore.isDark && themeStore.toggleTheme()"
              class="px-4 py-2 rounded-r-md border text-sm font-medium transition-colors"
              :class="!themeStore.isDark ? 'bg-accent text-white border-accent' : 'bg-transparent border-dark-border text-dark-text-muted'"
            >
              Light
            </button>
          </div>
        </div>
      </div>

      <!-- Timezone -->
      <div class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <Globe class="w-5 h-5" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Timezone</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                Set your local timezone for accurate timestamps
              </p>
            </div>
          </div>
          <select class="px-3 py-2 rounded-md border text-sm"
            :class="themeStore.isDark ? 'bg-dark-bg border-dark-border text-dark-text' : 'bg-light-bg border-light-border text-light-text'">
            <option>UTC+07:00 Asia/Bangkok</option>
            <option>UTC+00:00 Europe/London</option>
            <option>UTC-05:00 America/New_York</option>
          </select>
        </div>
      </div>

      <!-- Currency -->
      <div class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <DollarSign class="w-5 h-5" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Currency Display</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                Preferred currency for amounts
              </p>
            </div>
          </div>
          <select class="px-3 py-2 rounded-md border text-sm"
            :class="themeStore.isDark ? 'bg-dark-bg border-dark-border text-dark-text' : 'bg-light-bg border-light-border text-light-text'">
            <option>USD ($)</option>
            <option>EUR (€)</option>
            <option>GBP (£)</option>
          </select>
        </div>
      </div>
    </div>
  </div>
</template>
