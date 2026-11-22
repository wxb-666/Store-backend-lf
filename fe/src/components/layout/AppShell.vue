<template>
  <div class="app-shell">
    <AppSidebar />
    <main class="app-shell__content"><slot /></main>
  </div>
</template>

<script setup lang="ts">
import AppSidebar from './AppSidebar.vue'

</script>

<style scoped>
.app-shell { display: flex; width: 125vw; height: 125vh; min-height: 725px; overflow: hidden; background: #080808; transform: scale(.8); transform-origin: top left; }
.app-shell__content { display: flex; flex: 1; flex-direction: column; min-width: 0; margin: 5px 6px 5px 0; overflow: hidden; background: white; border-radius: 22px; }
@media (max-width: 780px) { .app-shell { width: 100vw; height: 100vh; min-height: 100vh; transform: none; }.app-shell__content { margin: 0; border-radius: 0; } }
</style>
