<template>
  <section class="dashboard"><DashboardHeader /><div class="dashboard__content"><StorePreview /><WelcomePanel /><TaskGrid /></div></section>
</template>

<script setup lang="ts">
import DashboardHeader from '../components/dashboard/DashboardHeader.vue'
import StorePreview from '../components/dashboard/StorePreview.vue'
import TaskGrid from '../components/dashboard/TaskGrid.vue'
import WelcomePanel from '../components/dashboard/WelcomePanel.vue'
</script>

<style scoped>
.dashboard { display: flex; flex: 1; flex-direction: column; min-width: 0; overflow: hidden; }.dashboard__content { flex: 1; min-height: 0; padding: 48px 48px 70px; overflow: auto; scrollbar-color: #797979 transparent; scrollbar-width: thin; }@media (max-width: 780px) { .dashboard__content { padding: 32px 20px 48px; } }
</style>
