<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Bell, Mail, Send, Smartphone } from 'lucide-vue-next'

const themeStore = useThemeStore()

const settings = ref({
  emailAlerts: true,
  telegramAlerts: true,
  pushAlerts: false,
  dailySummary: true,
  weeklyReport: false
})
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
        Notification Settings
      </h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        Configure global notification preferences
      </p>
    </div>

    <div class="space-y-4">
      <div class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <Mail class="w-5 h-5" :class="settings.emailAlerts ? 'text-accent' : (themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted')" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Email Alerts</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Receive alerts via email</p>
            </div>
          </div>
          <button 
            @click="settings.emailAlerts = !settings.emailAlerts"
            class="relative w-12 h-6 rounded-full transition-colors"
            :class="settings.emailAlerts ? 'bg-accent' : (themeStore.isDark ? 'bg-dark-border' : 'bg-light-border')"
          >
            <span class="absolute top-1 w-4 h-4 rounded-full bg-white transition-transform"
              :class="settings.emailAlerts ? 'translate-x-7' : 'translate-x-1'"></span>
          </button>
        </div>
      </div>

      <div class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <Send class="w-5 h-5" :class="settings.telegramAlerts ? 'text-accent' : (themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted')" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Telegram Alerts</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Receive alerts via Telegram</p>
            </div>
          </div>
          <button 
            @click="settings.telegramAlerts = !settings.telegramAlerts"
            class="relative w-12 h-6 rounded-full transition-colors"
            :class="settings.telegramAlerts ? 'bg-accent' : (themeStore.isDark ? 'bg-dark-border' : 'bg-light-border')"
          >
            <span class="absolute top-1 w-4 h-4 rounded-full bg-white transition-transform"
              :class="settings.telegramAlerts ? 'translate-x-7' : 'translate-x-1'"></span>
          </button>
        </div>
      </div>

      <div class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <Smartphone class="w-5 h-5" :class="settings.pushAlerts ? 'text-accent' : (themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted')" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Push Notifications</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Browser push notifications</p>
            </div>
          </div>
          <button 
            @click="settings.pushAlerts = !settings.pushAlerts"
            class="relative w-12 h-6 rounded-full transition-colors"
            :class="settings.pushAlerts ? 'bg-accent' : (themeStore.isDark ? 'bg-dark-border' : 'bg-light-border')"
          >
            <span class="absolute top-1 w-4 h-4 rounded-full bg-white transition-transform"
              :class="settings.pushAlerts ? 'translate-x-7' : 'translate-x-1'"></span>
          </button>
        </div>
      </div>

      <div class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <Bell class="w-5 h-5" :class="settings.dailySummary ? 'text-accent' : (themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted')" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Daily Summary</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Receive daily performance summary</p>
            </div>
          </div>
          <button 
            @click="settings.dailySummary = !settings.dailySummary"
            class="relative w-12 h-6 rounded-full transition-colors"
            :class="settings.dailySummary ? 'bg-accent' : (themeStore.isDark ? 'bg-dark-border' : 'bg-light-border')"
          >
            <span class="absolute top-1 w-4 h-4 rounded-full bg-white transition-transform"
              :class="settings.dailySummary ? 'translate-x-7' : 'translate-x-1'"></span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
