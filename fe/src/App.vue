<template>
  <AppShell @navigate="activeView = $event">
    <DashboardView v-if="activeView === 'dashboard'" />
    <OrdersView v-else />
  </AppShell>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import AppShell from './components/layout/AppShell.vue'
import DashboardView from './views/DashboardView.vue'
import OrdersView from './views/OrdersView.vue'

const activeView = ref<'dashboard' | 'orders'>('dashboard')
</script>
