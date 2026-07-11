<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Plus, Search, RefreshCw, Plug, PlugZap } from 'lucide-vue-next'
import mockAccounts from '@/mock/accounts.json'

const themeStore = useThemeStore()
const searchQuery = ref('')
const accounts = ref(mockAccounts.accounts)

const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value)
}

const formatPercent = (value) => {
  return value.toFixed(2) + '%'
}
</script>

<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          MT5 Accounts
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          Connected MetaTrader 5 accounts
        </p>
      </div>
      <div class="flex items-center gap-3">
        <button class="btn-secondary flex items-center gap-2">
          <RefreshCw class="w-4 h-4" />
          Refresh
        </button>
        <button class="btn-primary flex items-center gap-2">
          <Plus class="w-4 h-4" />
          Connect Account
        </button>
      </div>
    </div>

    <!-- Filters -->
    <div class="flex items-center gap-4">
      <div class="flex items-center gap-2 px-3 py-2 rounded-md border flex-1 max-w-md"
        :class="themeStore.isDark ? 'bg-dark-surface border-dark-border' : 'bg-light-surface border-light-border'">
        <Search class="w-4 h-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'" />
        <input 
          v-model="searchQuery"
          type="text"
          placeholder="Search by login or broker..."
          class="bg-transparent outline-none text-sm w-full"
          :class="themeStore.isDark ? 'text-dark-text placeholder:text-dark-text-muted' : 'text-light-text placeholder:text-light-text-muted'"
        />
      </div>
    </div>

    <!-- Accounts Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div 
        v-for="account in accounts" 
        :key="account.id"
        class="card p-4"
      >
        <!-- Header -->
        <div class="flex items-start justify-between mb-4">
          <div>
            <p class="font-mono text-lg font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
              {{ account.login }}
            </p>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              {{ account.broker }}
            </p>
          </div>
          <div class="flex items-center gap-1.5">
            <span 
              class="w-2 h-2 rounded-full"
              :class="account.status === 'connected' ? 'bg-profit' : 'bg-loss'"
            ></span>
            <span 
              class="text-xs font-medium capitalize"
              :class="account.status === 'connected' ? 'text-profit' : 'text-loss'"
            >
              {{ account.status }}
            </span>
          </div>
        </div>

        <!-- Stats -->
        <div class="space-y-3">
          <div class="flex justify-between items-center">
            <span class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Balance</span>
            <span class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
              {{ formatCurrency(account.balance) }}
            </span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Equity</span>
            <span class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
              {{ formatCurrency(account.equity) }}
            </span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Margin Level</span>
            <span class="font-medium" :class="account.marginLevel > 200 ? 'text-profit' : account.marginLevel > 100 ? 'text-accent' : 'text-loss'">
              {{ formatPercent(account.marginLevel) }}
            </span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Floating PnL</span>
            <span class="font-medium" :class="account.unrealizedPnL >= 0 ? 'text-profit' : 'text-loss'">
              {{ account.unrealizedPnL >= 0 ? '+' : '' }}{{ formatCurrency(account.unrealizedPnL) }}
            </span>
          </div>
        </div>

        <!-- Divider -->
        <div class="my-4 border-t" :class="themeStore.isDark ? 'border-dark-border' : 'border-light-border'"></div>

        <!-- Footer -->
        <div class="flex items-center justify-between">
          <span class="text-xs" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
            {{ account.server }} • {{ account.leverage }}
          </span>
          <button 
            class="p-1.5 rounded-md transition-colors"
            :class="themeStore.isDark ? 'hover:bg-dark-bg' : 'hover:bg-light-bg'"
          >
            <component 
              :is="account.status === 'connected' ? Plug : PlugZap" 
              class="w-4 h-4"
              :class="account.status === 'connected' ? 'text-profit' : 'text-loss'"
            />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
