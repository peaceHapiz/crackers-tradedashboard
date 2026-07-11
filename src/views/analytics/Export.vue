<script setup>
import { useThemeStore } from '@/store/theme'
import { Download, FileSpreadsheet, FileText } from 'lucide-vue-next'

const themeStore = useThemeStore()
</script>

<template>
  <div class="space-y-6">
    <div>
      <h1 class="text-2xl font-semibold" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">
        Export Data
      </h1>
      <p class="mt-1 text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
        Download trading data in various formats
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="card p-6">
        <div class="flex items-center gap-4 mb-4">
          <div class="p-3 rounded-md bg-profit/10">
            <FileSpreadsheet class="w-6 h-6 text-profit" />
          </div>
          <div>
            <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Export to CSV</h3>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              Download trade history as spreadsheet
            </p>
          </div>
        </div>
        <button class="btn-secondary w-full">
          <Download class="w-4 h-4 inline mr-2" />
          Download CSV
        </button>
      </div>

      <div class="card p-6">
        <div class="flex items-center gap-4 mb-4">
          <div class="p-3 rounded-md bg-loss/10">
            <FileText class="w-6 h-6 text-loss" />
          </div>
          <div>
            <h3 class="font-medium" :class="themeStore.isDark ? 'text-dark-text' : 'text-light-text'">Export to PDF</h3>
            <p class="text-sm" :class="themeStore.isDark ? 'text-dark-text-muted' : 'text-light-text-muted'">
              Generate formatted report document
            </p>
          </div>
        </div>
        <button class="btn-secondary w-full">
          <Download class="w-4 h-4 inline mr-2" />
          Download PDF
        </button>
      </div>
    </div>
  </div>
</template>
