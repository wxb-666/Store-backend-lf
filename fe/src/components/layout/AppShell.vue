<template>
  <div class="app-shell">
    <AppSidebar v-model:collapsed="collapsed" @navigate="emit('navigate', $event)" />
    <main class="app-shell__content"><slot /></main>
  </div>
</template>

<script setup lang="ts">
import AppSidebar from './AppSidebar.vue'

const collapsed = defineModel<boolean>('collapsed', { required: true })
const emit = defineEmits<{ navigate: [view: 'dashboard' | 'orders'] }>()
</script>

<style scoped>
.app-shell { display: flex; width: 100vw; height: 100vh; min-height: 580px; overflow: hidden; background: #080808; }
.app-shell__content { display: flex; flex: 1; flex-direction: column; min-width: 0; margin: 5px 6px 5px 0; overflow: hidden; background: white; border-radius: 22px; }
@media (max-width: 780px) { .app-shell { min-height: 100vh; }.app-shell__content { margin: 0; border-radius: 0; } }
</style>
