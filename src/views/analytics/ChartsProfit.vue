<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { BarChart3, Filter } from 'lucide-vue-next'

const themeStore = useThemeStore()
const selectedThreshold = ref(100)
</script>

<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Profit Charts
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Profit analysis by day and threshold
        </p>
      </div>
      <div class="flex items-center gap-2">
        <select v-model="selectedThreshold" class="px-3 py-2 rounded-md border text-sm"
          :class="themeStore.isDark ? 'bg-dark-surface border-dark-border text-dark-text' : 'bg-light-surface border-light-border text-light-text'">
          <option :value="50">Profit > $50</option>
          <option :value="100">Profit > $100</option>
          <option :value="200">Profit > $200</option>
          <option :value="500">Profit > $500</option>
        </select>
      </div>
    </div>

    <div class="card p-6">
      <div class="h-96 flex items-center justify-center" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
        <div class="text-center">
          <BarChart3 class="w-12 h-12 mx-auto mb-2" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
          <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
            Bar chart visualization (Profit > ${{ selectedThreshold }})
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
