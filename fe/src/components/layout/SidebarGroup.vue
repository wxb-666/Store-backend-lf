<template>
  <section class="nav-group">
    <p v-if="titleKey" class="nav-group__title">{{ t(titleKey) }}</p>
    <button v-for="item in items" :key="item.id" class="nav-item" :class="{ 'is-active': item.id === activeItem }" :disabled="item.disabled" type="button" @click="emit('select', item.id)">
      <AppIcon :name="item.icon" />
      <span>{{ t(item.labelKey) }}</span>
    </button>
  </section>
</template>

<script setup lang="ts">
import AppIcon, { type IconName } from '../ui/AppIcon.vue'
import { t, type MessageKey } from '../../stores/locale'
type NavigationItem = { id: string; labelKey: MessageKey; icon: IconName; disabled?: boolean }
defineProps<{ titleKey?: MessageKey; items: NavigationItem[]; activeItem: string }>()
const emit = defineEmits<{ select: [label: string] }>()
</script>
