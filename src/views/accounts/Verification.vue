<script setup>
import { ref } from 'vue'
import { useThemeStore } from '@/store/theme'
import { Shield, CheckCircle, XCircle, Clock, Smartphone, Key } from 'lucide-vue-next'

const themeStore = useThemeStore()

const verifications = ref([
  { id: 1, user: 'Admin User', email: 'admin@example.com', kycStatus: 'verified', twoFA: true },
  { id: 2, user: 'John Trader', email: 'john@example.com', kycStatus: 'pending', twoFA: true },
  { id: 3, user: 'Sarah Viewer', email: 'sarah@example.com', kycStatus: 'verified', twoFA: false },
  { id: 4, user: 'Mike Analyst', email: 'mike@example.com', kycStatus: 'rejected', twoFA: false }
])

const kycStatusConfig = {
  verified: { label: 'Verified', icon: CheckCircle, color: 'text-profit', bg: 'bg-profit/10' },
  pending: { label: 'Pending', icon: Clock, color: 'text-accent', bg: 'bg-accent/10' },
  rejected: { label: 'Rejected', icon: XCircle, color: 'text-loss', bg: 'bg-loss/10' }
}
</script>

<template>
  <div class="space-y-6">
    <!-- Page Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
          Verification
        </h1>
        <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
          KYC status and two-factor authentication
        </p>
      </div>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="card p-4">
        <div class="flex items-center gap-3">
          <div class="p-2.5 rounded-md bg-profit/10">
            <CheckCircle class="w-5 h-5 text-profit" />
          </div>
          <div>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Verified</p>
            <p class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">2</p>
          </div>
        </div>
      </div>
      <div class="card p-4">
        <div class="flex items-center gap-3">
          <div class="p-2.5 rounded-md bg-accent/10">
            <Clock class="w-5 h-5 text-accent" />
          </div>
          <div>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Pending</p>
            <p class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">1</p>
          </div>
        </div>
      </div>
      <div class="card p-4">
        <div class="flex items-center gap-3">
          <div class="p-2.5 rounded-md bg-loss/10">
            <XCircle class="w-5 h-5 text-loss" />
          </div>
          <div>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Rejected</p>
            <p class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">1</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Verification Table -->
    <div class="card overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b" :class="themeStore.isDark ? 'border-dark-border bg-dark-bg' : 'border-light-border bg-light-bg'">
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">User</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Email</th>
            <th class="text-left py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">KYC Status</th>
            <th class="text-center py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">2FA</th>
            <th class="text-right py-3 px-4 font-medium" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="verification in verifications" 
            :key="verification.id"
            class="border-b transition-colors"
            :class="[
              themeStore.isDark ? 'border-dark-border hover:bg-dark-bg/50' : 'border-light-border hover:bg-light-bg/50'
            ]"
          >
            <td class="py-3 px-4">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-full flex items-center justify-center text-white text-xs font-medium"
                  style="background: linear-gradient(135deg, #f97316, #fb923c);">
                  {{ verification.user.split(' ').map(n => n[0]).join('') }}
                </div>
                <span class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
                  {{ verification.user }}
                </span>
              </div>
            </td>
            <td class="py-3 px-4" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              {{ verification.email }}
            </td>
            <td class="py-3 px-4">
              <div class="flex items-center gap-2">
                <component 
                  :is="kycStatusConfig[verification.kycStatus].icon"
                  class="w-4 h-4"
                  :class="kycStatusConfig[verification.kycStatus].color"
                />
                <span 
                  class="px-2 py-1 rounded-full text-xs font-medium"
                  :class="[kycStatusConfig[verification.kycStatus].bg, kycStatusConfig[verification.kycStatus].color]"
                >
                  {{ kycStatusConfig[verification.kycStatus].label }}
                </span>
              </div>
            </td>
            <td class="py-3 px-4 text-center">
              <div class="flex justify-center">
                <span 
                  class="flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium"
                  :class="verification.twoFA ? 'bg-profit/10 text-profit' : 'bg-dark-text-muted/10 text-dark-text-muted'"
                >
                  <Key class="w-3 h-3" />
                  {{ verification.twoFA ? 'Enabled' : 'Disabled' }}
                </span>
              </div>
            </td>
            <td class="py-3 px-4 text-right">
              <button class="btn-secondary text-xs py-1.5">
                <Smartphone class="w-3 h-3 inline mr-1" />
                Manage
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
