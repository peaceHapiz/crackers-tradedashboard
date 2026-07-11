<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Search } from 'lucide-vue-next'

const themeStore = useThemeStore()
const searchQuery = ref('')

const audits = ref([
  { id: 1, user: 'Admin', action: 'Updated account settings', timestamp: '2026-07-11 14:30:00', ip: '192.168.1.100' },
  { id: 2, user: 'John Trader', action: 'Connected MT5 account', timestamp: '2026-07-11 10:15:00', ip: '192.168.1.105' },
  { id: 3, user: 'Admin', action: 'Created new alert rule', timestamp: '2026-07-10 16:45:00', ip: '192.168.1.100' }
])
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Audit Logs</h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">System activity history</p>
    </div>

    <div class="flex items-center gap-2 px-3 py-2 rounded-md border max-w-md"
      :class="themeStore.isDark ? 'bg-dark-surface border-dark-border' : 'bg-light-surface border-light-border'">
      <Search class="w-4 h-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
      <input v-model="searchQuery" type="text" placeholder="Search..."
        class="bg-transparent outline-none text-sm w-full"
        :class="themeStore.isDark ? 'text-dark-text placeholder:text-dark-text-muted' : 'text-light-text placeholder:text-light-text-muted'" />
    </div>

    <div class="card overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b" :class="themeStore.isDark ? 'border-dark-border bg-dark-bg' : 'border-light-border bg-light-bg'">
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">User</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Action</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">IP</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Time</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="audit in audits" :key="audit.id" class="border-b"
            :class="themeStore.isDark ? 'border-dark-border' : 'border-light-border'">
            <td class="py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">{{ audit.user }}</td>
            <td class="py-3 px-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ audit.action }}</td>
            <td class="py-3 px-4 font-mono text-xs" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ audit.ip }}</td>
            <td class="py-3 px-4 text-xs" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">{{ audit.timestamp }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
