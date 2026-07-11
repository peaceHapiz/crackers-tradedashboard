<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Server, Key, Plus, Trash2 } from 'lucide-vue-next'

const themeStore = useThemeStore()

const providers = ref([
  { id: 1, name: 'ICMarkets', type: 'MT5 Broker', apiKey: 'sk_****1234', status: 'active' },
  { id: 2, name: 'Exness', type: 'MT5 Broker', apiKey: 'sk_****5678', status: 'active' },
  { id: 3, name: 'XM', type: 'MT5 Broker', apiKey: 'sk_****9012', status: 'inactive' }
])
</script>

<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Providers
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Connected brokers and signal providers
        </p>
      </div>
      <button class="btn-primary flex items-center gap-2">
        <Plus class="w-4 h-4" />
        Add Provider
      </button>
    </div>

    <div class="space-y-4">
      <div v-for="provider in providers" :key="provider.id" class="card p-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <Server class="w-5 h-5" :class="provider.status === 'active' ? 'text-profit' : (themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted')" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ provider.name }}</h3>
              <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ provider.type }}</p>
            </div>
          </div>
          <div class="flex items-center gap-4">
            <div class="text-right">
              <div class="flex items-center gap-1">
                <Key class="w-3 h-3" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
                <code class="text-xs font-mono" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ provider.apiKey }}</code>
              </div>
              <span class="text-xs capitalize" :class="provider.status === 'active' ? 'text-profit' : 'text-dark-text-muted'">
                {{ provider.status }}
              </span>
            </div>
            <button class="p-1.5 rounded-md transition-colors hover:bg-loss/10">
              <Trash2 class="w-4 h-4 text-loss" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
