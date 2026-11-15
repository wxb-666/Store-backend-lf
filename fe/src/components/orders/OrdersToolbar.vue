<template>
  <div class="orders-toolbar">
    <button class="all-filter" type="button">{{ t('orders.all') }} <span class="chevrons" aria-hidden="true"><span>⌃</span><span>⌄</span></span></button>
    <label><AppIcon name="search" :size="20" /><input v-model="query" type="search" :placeholder="t('orders.searchPlaceholder')" /></label>
    <button class="columns-button" type="button" :aria-label="t('orders.editColumns')">▥</button>
  </div>
</template>

<script setup lang="ts">
import AppIcon from '../ui/AppIcon.vue'
import { t } from '../../stores/locale'
const query = defineModel<string>('query', { required: true })
</script>

<style scoped>
.orders-toolbar { display: flex; align-items: center; min-height: 47px; padding: 0 15px; background: white; border: 1px solid #e4e4e4; border-radius: 14px; box-shadow: 0 2px 7px rgb(0 0 0 / 4%); }.all-filter, .columns-button { padding: 5px 1px; color: #242424; font-size: 14px; background: transparent; border: 0; }.all-filter { display: inline-flex; align-items: center; gap: 5px; margin-right: 25px; }.chevrons { display: flex; flex-direction: column; align-items: center; justify-content: center; width: 10px; font-size: 11px; line-height: 7px; }.chevrons span { display: block; height: 7px; }label { display: flex; align-items: center; flex: 1; gap: 10px; color: #5e5e5e; }input { width: 100%; border: 0; outline: 0; color: #222; font-size: 15px; }input::placeholder { color: #525252; }.columns-button { font-size: 21px; transform: rotate(90deg); }
</style>
