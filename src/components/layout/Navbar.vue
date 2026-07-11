<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Sun, Moon, Bell, Search } from 'lucide-vue-next'

const themeStore = useThemeStore()
const searchQuery = ref('')
</script>

<template>
  <header 
    class="h-16 flex items-center justify-between px-6 border-b"
    :class="[
      themeStore.isDark 
        ? 'bg-dark-bg-alt border-dark-border' 
        : 'bg-light-bg-alt border-light-border'
    ]"
  >
    <!-- Search -->
    <div class="flex items-center gap-2">
      <div 
        class="flex items-center gap-2 px-3 py-2 rounded-md border w-64"
        :class="[
          themeStore.isDark 
            ? 'bg-dark-surface border-dark-border' 
            : 'bg-light-surface border-light-border'
        ]"
      >
        <Search class="w-4 h-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
        <input 
          v-model="searchQuery"
          type="text"
          placeholder="Search..."
          class="bg-transparent outline-none text-sm w-full"
          :class="themeStore.isDark ? 'text-dark-text placeholder:text-dark-text-muted' : 'text-light-text placeholder:text-light-text-muted'"
        />
      </div>
    </div>

    <!-- Right side -->
    <div class="flex items-center gap-3">
      <!-- Notifications -->
      <button 
        class="relative p-2 rounded-md transition-colors"
        :class="themeStore.isDark ? 'hover:bg-dark-surface' : 'hover:bg-light-surface'"
      >
        <Bell class="w-5 h-5" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
        <span class="absolute top-1 right-1 w-2 h-2 rounded-full bg-accent"></span>
      </button>

      <!-- Theme toggle -->
      <button 
        @click="themeStore.toggleTheme()"
        class="p-2 rounded-md transition-colors"
        :class="themeStore.isDark ? 'hover:bg-dark-surface' : 'hover:bg-light-surface'"
      >
        <component 
          :is="themeStore.isDark ? Sun : Moon" 
          class="w-5 h-5"
          :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'"
        />
      </button>

      <!-- User avatar -->
      <div 
        class="w-8 h-8 rounded-full flex items-center justify-center text-white text-sm font-medium"
        style="background: linear-gradient(135deg, #f97316, #fb923c);"
      >
        A
      </div>
    </div>
  </header>
</template>
