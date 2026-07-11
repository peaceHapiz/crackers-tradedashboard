<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Plus, Bell, Edit, Trash2, Pause, Play } from 'lucide-vue-next'
import mockAlerts from '@/mock/alerts.json'

const themeStore = useThemeStore()
const rules = ref(mockAlerts)
</script>

<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Alert Rules
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Configure trading alerts and notifications
        </p>
      </div>
      <button class="btn-primary flex items-center gap-2">
        <Plus class="w-4 h-4" />
        Create Rule
      </button>
    </div>

    <div class="space-y-4">
      <div v-for="rule in rules" :key="rule.id" class="card p-4">
        <div class="flex items-start justify-between">
          <div class="flex items-start gap-3">
            <div class="p-2 rounded-md" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
              <Bell class="w-5 h-5" :class="rule.status === 'active' ? 'text-accent' : 'text-dark-text-muted'" />
            </div>
            <div>
              <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ rule.ruleName }}</h3>
              <p class="text-sm mt-1" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                Condition: <code class="px-1.5 py-0.5 rounded text-xs"
                  :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">{{ rule.condition }}</code>
              </p>
              <div class="flex items-center gap-4 mt-2 text-xs" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
                <span>Triggered: {{ rule.triggeredCount }} times</span>
                <span v-if="rule.lastTriggered">Last: {{ rule.lastTriggered }}</span>
              </div>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="px-2 py-1 rounded-full text-xs font-medium capitalize"
              :class="rule.status === 'active' ? 'bg-profit/10 text-profit' : 'bg-dark-text-muted/10 text-dark-text-muted'">
              {{ rule.status }}
            </span>
            <button class="p-1.5 rounded-md transition-colors"
              :class="themeStore.isDark ? 'hover:bg-dark-bg' : 'hover:bg-light-bg'">
              <component :is="rule.status === 'active' ? Pause : Play" class="w-4 h-4"
                :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
            </button>
            <button class="p-1.5 rounded-md transition-colors"
              :class="themeStore.isDark ? 'hover:bg-dark-bg' : 'hover:bg-light-bg'">
              <Edit class="w-4 h-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
            </button>
            <button class="p-1.5 rounded-md transition-colors hover:bg-loss/10">
              <Trash2 class="w-4 h-4 text-loss" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
