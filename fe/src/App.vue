<template>
  <AppShell>
    <RouterView v-slot="{ Component }">
      <KeepAlive include="OrdersView">
        <component :is="Component" />
      </KeepAlive>
    </RouterView>
  </AppShell>
</template>

<script setup lang="ts">
import AppShell from './components/layout/AppShell.vue'
</script>
