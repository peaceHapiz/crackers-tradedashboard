<script setup>
import { ref, computed } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { 
  LayoutDashboard, 
  Users, 
  BarChart3, 
  FileText, 
  Bell, 
  Settings,
  ChevronLeft,
  ChevronRight
} from 'lucide-vue-next'
import { useThemeStore } from '@/store/theme'

const route = useRoute()
const themeStore = useThemeStore()
const isCollapsed = ref(false)

const menuItems = [
  {
    name: 'Overview',
    path: '/',
    icon: LayoutDashboard
  },
  {
    name: 'Accounts',
    path: '/accounts',
    icon: Users,
    children: [
      { name: 'User Accounts', path: '/accounts' },
      { name: 'MT5 Accounts', path: '/accounts/mt5' },
      { name: 'Verification', path: '/accounts/verification' }
    ]
  },
  {
    name: 'Analytics',
    path: '/analytics',
    icon: BarChart3,
    children: [
      { name: 'Charts PnL', path: '/analytics' },
      { name: 'Charts Profit', path: '/analytics/profit' },
      { name: 'Statistics', path: '/analytics/statistics' },
      { name: 'Reports', path: '/analytics/reports' },
      { name: 'Export', path: '/analytics/export' }
    ]
  },
  {
    name: 'Logs',
    path: '/logs/candle',
    icon: FileText,
    children: [
      { name: 'Candle Logs', path: '/logs/candle' },
      { name: 'Trade Logs', path: '/logs/trade' },
      { name: 'Audit Logs', path: '/logs/audit' },
      { name: 'Errors', path: '/logs/errors' }
    ]
  },
  {
    name: 'Alerts',
    path: '/alerts',
    icon: Bell,
    children: [
      { name: 'Rule List', path: '/alerts' },
      { name: 'Alert History', path: '/alerts/history' },
      { name: 'Channels', path: '/alerts/channels' }
    ]
  },
  {
    name: 'Settings',
    path: '/settings',
    icon: Settings,
    children: [
      { name: 'General', path: '/settings' },
      { name: 'Database', path: '/settings/database' },
      { name: 'Providers', path: '/settings/providers' },
      { name: 'Notifications', path: '/settings/notifications' }
    ]
  }
]

const expandedMenus = ref({})

const isActive = (path) => {
  return route.path === path
}

const isParentActive = (item) => {
  if (route.path === item.path) return true
  if (item.children) {
    return item.children.some(child => route.path === child.path)
  }
  return false
}

const toggleMenu = (name) => {
  expandedMenus.value[name] = !expandedMenus.value[name]
}

const isExpanded = (name) => {
  return expandedMenus.value[name] || isParentActive({ name, children: menuItems.find(m => m.name === name)?.children })
}
</script>

<template>
  <aside 
    class="h-full transition-all duration-300 flex flex-col border-r"
    :class="[
      isCollapsed ? 'w-16' : 'w-64',
      themeStore.isDark ? 'bg-dark-bg-alt border-dark-border' : 'bg-light-bg-alt border-light-border'
    ]"
  >
    <!-- Logo -->
    <div class="h-16 flex items-center justify-between px-4 border-b"
      :class="themeStore.isDark ? 'border-dark-border' : 'border-light-border'">
      <span v-if="!isCollapsed" class="text-lg font-semibold bg-gradient-to-r from-accent to-accent-secondary bg-clip-text text-transparent">
        Trading Dashboard
      </span>
      <button 
        @click="isCollapsed = !isCollapsed"
        class="p-1.5 rounded-md transition-colors"
        :class="themeStore.isDark ? 'hover:bg-dark-surface' : 'hover:bg-light-surface'"
      >
        <component :is="isCollapsed ? ChevronRight : ChevronLeft" class="w-4 h-4" />
      </button>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 overflow-y-auto py-4">
      <ul class="space-y-1 px-2">
        <li v-for="item in menuItems" :key="item.name">
          <!-- Parent item with children -->
          <template v-if="item.children">
            <button 
              @click="toggleMenu(item.name)"
              class="w-full flex items-center gap-3 px-3 py-2.5 rounded-md transition-colors"
              :class="[
                isParentActive(item) 
                  ? 'bg-gradient-to-r from-accent/20 to-transparent text-accent' 
                  : themeStore.isDark 
                    ? 'text-dark-text-muted hover:text-dark-text hover:bg-dark-surface' 
                    : 'text-light-text-muted hover:text-light-text hover:bg-light-surface'
              ]"
            >
              <component :is="item.icon" class="w-5 h-5 flex-shrink-0" />
              <span v-if="!isCollapsed" class="flex-1 text-left text-sm font-medium">{{ item.name }}</span>
              <ChevronRight 
                v-if="!isCollapsed" 
                class="w-4 h-4 transition-transform"
                :class="{ 'rotate-90': isExpanded(item.name) }"
              />
            </button>
            
            <!-- Submenu -->
            <ul 
              v-if="!isCollapsed && isExpanded(item.name)" 
              class="mt-1 ml-4 pl-3 border-l space-y-1"
              :class="themeStore.isDark ? 'border-dark-border' : 'border-light-border'"
            >
              <li v-for="child in item.children" :key="child.path">
                <RouterLink 
                  :to="child.path"
                  class="block px-3 py-2 text-sm rounded-md transition-colors"
                  :class="[
                    isActive(child.path)
                      ? 'text-accent font-medium'
                      : themeStore.isDark
                        ? 'text-dark-text-muted hover:text-dark-text'
                        : 'text-light-text-muted hover:text-light-text'
                  ]"
                >
                  {{ child.name }}
                </RouterLink>
              </li>
            </ul>
          </template>
          
          <!-- Single item without children -->
          <template v-else>
            <RouterLink 
              :to="item.path"
              class="flex items-center gap-3 px-3 py-2.5 rounded-md transition-colors"
              :class="[
                isActive(item.path)
                  ? 'bg-gradient-to-r from-accent/20 to-transparent text-accent'
                  : themeStore.isDark
                    ? 'text-dark-text-muted hover:text-dark-text hover:bg-dark-surface'
                    : 'text-light-text-muted hover:text-light-text hover:bg-light-surface'
              ]"
            >
              <component :is="item.icon" class="w-5 h-5 flex-shrink-0" />
              <span v-if="!isCollapsed" class="text-sm font-medium">{{ item.name }}</span>
            </RouterLink>
          </template>
        </li>
      </ul>
    </nav>

    <!-- Footer -->
    <div class="p-4 border-t" :class="themeStore.isDark ? 'border-dark-border' : 'border-light-border'">
      <div v-if="!isCollapsed" class="text-xs" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        v0.0.1 • Mock Data
      </div>
    </div>
  </aside>
</template>
