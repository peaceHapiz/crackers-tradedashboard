<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Plus, Search, MoreHorizontal, Edit, Trash2 } from 'lucide-vue-next'

const themeStore = useThemeStore()
const searchQuery = ref('')

const users = ref([
  { id: 1, name: 'Admin User', email: 'admin@example.com', role: 'admin', status: 'active', createdAt: '2025-01-15' },
  { id: 2, name: 'John Trader', email: 'john@example.com', role: 'trader', status: 'active', createdAt: '2025-03-20' },
  { id: 3, name: 'Sarah Viewer', email: 'sarah@example.com', role: 'viewer', status: 'active', createdAt: '2025-06-10' },
  { id: 4, name: 'Mike Analyst', email: 'mike@example.com', role: 'trader', status: 'inactive', createdAt: '2025-04-05' }
])

const roleColors = {
  admin: 'bg-accent/10 text-accent',
  trader: 'bg-profit/10 text-profit',
  viewer: 'bg-blue-500/10 text-blue-500'
}

const statusColors = {
  active: 'bg-profit/10 text-profit',
  inactive: 'bg-dark-text-muted/10 text-dark-text-muted'
}
</script>

<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          User Accounts
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Manage user access and permissions
        </p>
      </div>
      <button class="btn-primary flex items-center gap-2">
        <Plus class="w-4 h-4" />
        Add User
      </button>
    </div>

    <!-- Filters -->
    <div class="flex items-center gap-4">
      <div class="flex items-center gap-2 px-3 py-2 rounded-md border flex-1 max-w-md"
        :class="themeStore.isDark ? 'bg-dark-surface border-dark-border' : 'bg-light-surface border-light-border'">
        <Search class="w-4 h-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
        <input 
          v-model="searchQuery"
          type="text"
          placeholder="Search users..."
          class="bg-transparent outline-none text-sm w-full"
          :class="themeStore.isDark ? 'text-dark-text placeholder:text-dark-text-muted' : 'text-light-text placeholder:text-light-text-muted'"
        />
      </div>
    </div>

    <!-- Users Table -->
    <div class="card overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b" :class="themeStore.isDark ? 'border-dark-border bg-dark-bg' : 'border-light-border bg-light-bg'">
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Name</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Email</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Role</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Status</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Created</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="user in users" 
            :key="user.id"
            class="border-b transition-colors"
            :class="[
              themeStore.isDark ? 'border-dark-border hover:bg-dark-bg/50' : 'border-light-border hover:bg-light-bg/50'
            ]"
          >
            <td class="py-3 px-4">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-full flex items-center justify-center text-white text-xs font-medium"
                  style="background: linear-gradient(135deg, #f97316, #fb923c);">
                  {{ user.name.split(' ').map(n => n[0]).join('') }}
                </div>
                <span class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
                  {{ user.name }}
                </span>
              </div>
            </td>
            <td class="py-3 px-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              {{ user.email }}
            </td>
            <td class="py-3 px-4">
              <span class="px-2 py-1 rounded-full text-xs font-medium capitalize" :class="roleColors[user.role]">
                {{ user.role }}
              </span>
            </td>
            <td class="py-3 px-4">
              <span class="px-2 py-1 rounded-full text-xs font-medium capitalize" :class="statusColors[user.status]">
                {{ user.status }}
              </span>
            </td>
            <td class="py-3 px-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              {{ user.createdAt }}
            </td>
            <td class="py-3 px-4">
              <div class="flex items-center justify-end gap-2">
                <button 
                  class="p-1.5 rounded-md transition-colors"
                  :class="themeStore.isDark ? 'hover:bg-dark-surface' : 'hover:bg-light-surface'"
                >
                  <Edit class="w-4 h-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
                </button>
                <button 
                  class="p-1.5 rounded-md transition-colors hover:bg-loss/10"
                >
                  <Trash2 class="w-4 h-4 text-loss" />
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
