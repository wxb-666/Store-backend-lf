<template>
  <div class="app-shell"><AppSidebar v-model:collapsed="isSidebarCollapsed" /><main class="dashboard"><DashboardHeader /><div class="dashboard__content"><StorePreview /><WelcomePanel /><TaskGrid /></div></main></div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import DashboardHeader from '../components/dashboard/DashboardHeader.vue'
import StorePreview from '../components/dashboard/StorePreview.vue'
import TaskGrid from '../components/dashboard/TaskGrid.vue'
import WelcomePanel from '../components/dashboard/WelcomePanel.vue'
import AppSidebar from '../components/layout/AppSidebar.vue'
const isSidebarCollapsed = ref(false)
</script>

<style scoped>
.app-shell { display: flex; width: 100vw; height: 100vh; min-height: 580px; overflow: hidden; background: #080808; }.dashboard { display: flex; flex: 1; flex-direction: column; min-width: 0; margin: 5px 6px 5px 0; overflow: hidden; background: white; border-radius: 22px; }.dashboard__content { flex: 1; min-height: 0; padding: 48px 48px 70px; overflow: auto; scrollbar-color: #797979 transparent; scrollbar-width: thin; }@media (max-width: 780px) { .app-shell { min-height: 100vh; }.dashboard { margin: 0; border-radius: 0; }.dashboard__content { padding: 32px 20px 48px; } }
</style>
