<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { MessageSquare, Mail, Bell, Send, Check } from 'lucide-vue-next'

const themeStore = useThemeStore()

const channels = ref([
  { id: 1, name: 'Telegram', icon: Send, enabled: true, config: 'Bot configured' },
  { id: 2, name: 'Email', icon: Mail, enabled: true, config: 'admin@example.com' },
  { id: 3, name: 'Push Notifications', icon: Bell, enabled: false, config: 'Not configured' }
])

const toggleChannel = (id) => {
  const channel = channels.value.find(c => c.id === id)
  if (channel) channel.enabled = !channel.enabled
}
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
        Notification Channels
      </h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        Configure how you receive alerts
      </p>
    </div>

    <div class="space-y-4">
      <div v-for="channel in channels" :key="channel.id" class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="channel.enabled ? 'bg-accent/10' : (themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg')">
              <component :is="channel.icon" class="w-5 h-5" :class="channel.enabled ? 'text-accent' : (themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted')" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ channel.name }}</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ channel.config }}</p>
            </div>
          </div>
          <button 
            @click="toggleChannel(channel.id)"
            class="relative w-12 h-6 rounded-full transition-colors"
            :class="channel.enabled ? 'bg-accent' : (themeStore.isDark ? 'bg-dark-border' : 'bg-light-border')"
          >
            <span 
              class="absolute top-1 w-4 h-4 rounded-full bg-white transition-transform"
              :class="channel.enabled ? 'translate-x-7' : 'translate-x-1'"
            ></span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
