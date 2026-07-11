<script setup>
import Sidebar from './Sidebar.vue'
import Navbar from './Navbar.vue'
import { useThemeStore } from '@/store/theme'
import { onMounted } from 'vue'

const themeStore = useThemeStore()

onMounted(() => {
  themeStore.initTheme()
})
</script>

<template>
  <div class="flex h-screen overflow-hidden" :class="themeStore.isDark ? 'dark' : 'light'">
    <Sidebar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <Navbar />
      <main class="flex-1 overflow-auto p-6" :class="themeStore.isDark ? 'bg-dark-bg' : 'bg-light-bg'">
        <RouterView />
      </main>
    </div>
  </div>
</template>
