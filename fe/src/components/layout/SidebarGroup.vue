<template>
  <section class="nav-group">
    <p v-if="title && !collapsed" class="nav-group__title">{{ title }}</p>
    <div v-else-if="title" class="nav-group__divider" />
    <button v-for="item in items" :key="item.label" class="nav-item" :class="{ 'is-active': item.label === activeItem, 'is-icon-only': collapsed }" :title="collapsed ? item.label : undefined" type="button" @click="emit('select', item.label)">
      <AppIcon :name="item.icon" />
      <span v-if="!collapsed">{{ item.label }}</span>
    </button>
  </section>
</template>

<script setup lang="ts">
import AppIcon, { type IconName } from '../ui/AppIcon.vue'
type NavigationItem = { label: string; icon: IconName }
defineProps<{ title?: string; items: NavigationItem[]; collapsed: boolean; activeItem: string }>()
const emit = defineEmits<{ select: [label: string] }>()
</script>
