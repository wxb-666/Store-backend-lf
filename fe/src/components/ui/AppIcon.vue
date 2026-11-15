<template>
  <svg :width="size" :height="size" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path v-if="name === 'home'" d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z M9 22v-8h6v8" />
    <path v-else-if="name === 'orders'" d="M4 7h16l-1 14H5L4 7Z M7 7l1-4h8l1 4 M9 11a3 3 0 0 0 6 0" />
    <path v-else-if="name === 'tag'" d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8Z M7 7h.01" />
    <path v-else-if="name === 'customers'" d="M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM2 21v-2a5 5 0 0 1 5-5h4a5 5 0 0 1 5 5v2M17 3.5a4 4 0 0 1 0 7M20 21v-2a5 5 0 0 0-3-4.6" />
    <path v-else-if="name === 'growth'" d="m4 18 6-6 4 3 6-8M15 7h5v5" />
    <path v-else-if="name === 'content'" d="M6 3h9l4 4v14H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2ZM14 3v5h5M8 13h8M8 17h6" />
    <path v-else-if="name === 'market'" d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Zm0-5a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM3 12h3m12 0h3M12 3v3m0 12v3" />
    <path v-else-if="name === 'finance'" d="M3 5h18v14H3zM3 10h18" />
    <path v-else-if="name === 'analytics'" d="M5 20v-5M10 20V9M15 20v-9M20 20V4" />
    <path v-else-if="name === 'store'" d="m4 9 2-5h12l2 5M5 9v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9M4 9h16M9 21v-6h6v6" />
    <path v-else-if="name === 'bot'" d="M12 3v4M3 10a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v7a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3v-7ZM8 13h.01M16 13h.01M8 17h8" />
    <path v-else-if="name === 'plus'" d="M12 5v14M5 12h14" />
    <path v-else-if="name === 'settings'" d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm7.4 0a1.7 1.7 0 0 0 .3 1.9l.1.1-2.8 2.8-.1-.1a1.7 1.7 0 0 0-1.9-.3 1.7 1.7 0 0 0-1 1.5v.1h-4v-.1a1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.9.3l-.1.1-2.8-2.8.1-.1a1.7 1.7 0 0 0 .3-1.9 1.7 1.7 0 0 0-1.5-1H3v-4h.1a1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.9l-.1-.1L7 4.2l.1.1a1.7 1.7 0 0 0 1.9.3 1.7 1.7 0 0 0 1-1.5V3h4v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.9-.3l.1-.1 2.8 2.8-.1.1a1.7 1.7 0 0 0-.3 1.9 1.7 1.7 0 0 0 1.5 1h.1v4h-.1a1.7 1.7 0 0 0-1.5 1Z" />
    <path v-else-if="name === 'search'" d="M16 16l4 4M10.8 17.6a6.8 6.8 0 1 0 0-13.6 6.8 6.8 0 0 0 0 13.6Z" />
    <path v-else-if="name === 'bell'" d="M18 9a6 6 0 0 0-12 0c0 7-3 8-3 8h18s-3-1-3-8M10 21h4" />
    <path v-else-if="name === 'panel'" d="M3 3h18v18H3zM9 3v18" />
    <path v-else-if="name === 'history'" d="M3 12a9 9 0 1 0 3-6.7L3 8M3 3v5h5M12 7v5l3 2" />
    <path v-else-if="name === 'mic'" d="M9 3h6v8a3 3 0 0 1-6 0V3ZM5 11a7 7 0 0 0 14 0M12 18v3" />
    <path v-else-if="name === 'rocket'" d="M14 5c3-3 6-2 6-2s1 3-2 6l-5 5-4-4 5-5ZM9 10l-4 1-2 4 4-2M14 15l-1 4-4 2 2-4" />
    <path v-else d="M12 20a8 8 0 1 0 0-16 8 8 0 0 0 0 16Zm-3-8 2 2 4-4" />
  </svg>
</template>

<script setup lang="ts">
export type IconName = 'analytics' | 'bell' | 'bot' | 'content' | 'customers' | 'finance' | 'growth' | 'history' | 'home' | 'market' | 'mic' | 'orders' | 'panel' | 'plus' | 'rocket' | 'search' | 'settings' | 'store' | 'tag'
withDefaults(defineProps<{ name: IconName; size?: number }>(), { size: 20 })
</script>
