<template>
  <section class="nav-group">
    <p v-if="title" class="nav-group__title">{{ title }}</p>

    <button
      v-for="item in items"
      :key="item.id"
      class="nav-item"
      :class="{ 'is-active': item.id === activeItem }"
      :disabled="item.disabled"
      type="button"
      @click="emit('select', item.id)"
    >
      <AppIcon :name="item.icon" />
      <span>{{ item.label }}</span>
    </button>
  </section>
</template>

<script setup lang="ts">
import AppIcon, { type IconName } from '../ui/AppIcon.vue'

type NavigationItem = {
  id: string
  label: string
  icon: IconName
  disabled?: boolean
}

defineProps<{
  title?: string
  items: NavigationItem[]
  activeItem: string
}>()

const emit = defineEmits<{
  select: [label: string]
}>()
</script>
