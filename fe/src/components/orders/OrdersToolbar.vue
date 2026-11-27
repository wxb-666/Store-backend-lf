<template>
  <form class="orders-toolbar" @submit.prevent="submitSearch">
    <div class="date-range filter-field">
      <span class="date-placeholder">Start date</span>
      <span class="date-divider" aria-hidden="true">~</span>
      <span class="date-placeholder">End date</span>
      <AppIcon class="calendar-icon" name="calendar" :size="15" />
    </div>

    <div class="filter-field country-field">Country/Region</div>

    <div ref="methodFilter" class="select-filter">
      <button class="filter-field select-field" type="button" aria-haspopup="listbox" :aria-expanded="paymentMethodOpen" @click="paymentMethodOpen = !paymentMethodOpen">
        <span :class="{ 'is-placeholder': !paymentMethod }">{{ paymentMethod || 'Payment method' }}</span>
        <AppIcon class="select-chevron" name="chevron-down" :size="18" />
      </button>
      <div v-if="paymentMethodOpen" class="select-menu" role="listbox" aria-label="Payment method">
        <button v-for="option in paymentMethodOptions" :key="option.value || 'all'" class="select-option" :class="{ 'is-selected': paymentMethod === option.value }" type="button" role="option" :aria-selected="paymentMethod === option.value" @click="selectPaymentMethod(option.value)">
          {{ option.label }}
        </button>
      </div>
    </div>

    <label class="filter-field status-field">
      <input v-model="domain" type="search" placeholder="Payment status" aria-label="Payment status" />
    </label>

    <div class="search-field filter-field">
      <AppIcon name="search" :size="19" />
      <input v-model="draftQuery" type="search" placeholder="Please enter order number, slug, etc." aria-label="Order search" />
      <button type="submit">Search</button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref, watch } from 'vue'
import AppIcon from '../ui/AppIcon.vue'

const query = defineModel<string>('query', { required: true })
const paymentMethod = defineModel<string>('paymentMethod', { required: true })
const domain = defineModel<string>('domain', { required: true })
const draftQuery = ref(query.value)
const paymentMethodOpen = ref(false)
const methodFilter = ref<HTMLElement | null>(null)
const paymentMethodOptions = [
  { label: 'Credit card', value: 'Credit card' },
  { label: 'PayPal', value: 'PayPal' },
  { label: 'Shop Pay', value: 'Shop Pay' },
  { label: 'All', value: '' },
]

watch(query, (value) => { draftQuery.value = value })

function closeSelectMenus(event: PointerEvent) {
  if (event.target instanceof Node && !methodFilter.value?.contains(event.target)) paymentMethodOpen.value = false
}

function handleMenuKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape') {
    paymentMethodOpen.value = false
  }
}

function selectPaymentMethod(method: string) {
  paymentMethod.value = method
  paymentMethodOpen.value = false
}

onMounted(() => {
  document.addEventListener('pointerdown', closeSelectMenus)
  document.addEventListener('keydown', handleMenuKeydown)
})

onUnmounted(() => {
  document.removeEventListener('pointerdown', closeSelectMenus)
  document.removeEventListener('keydown', handleMenuKeydown)
})

function submitSearch() {
  query.value = draftQuery.value.trim()
}
</script>

<style scoped>
.orders-toolbar { display: grid; grid-template-columns: 230px 170px 180px 180px minmax(320px, 1fr); align-items: center; gap: 10px; margin-bottom: 14px; }
.filter-field { display: flex; align-items: center; height: 43px; min-width: 0; padding: 0 12px; color: #555; font-size: 14px; line-height: 20px; background: #fff; border: 1px solid #d8d8d8; border-radius: 8px; box-shadow: 0 1px 2px rgb(0 0 0 / 3%); }
.filter-field:focus-within { border-color: #777; box-shadow: 0 0 0 2px rgb(0 0 0 / 8%); }
.date-range { gap: 9px; padding-inline: 12px; border-radius: 5px; }
.date-range { justify-content: flex-start; }
.date-placeholder { overflow: hidden; color: #555; font-size: inherit; white-space: nowrap; }
.date-divider { flex: 0 0 auto; color: #888; }
.calendar-icon { flex: 0 0 auto; margin-left: auto; color: #777; }
.select-filter { position: relative; min-width: 0; }
.select-field { width: 100%; justify-content: space-between; gap: 10px; border-radius: 5px; text-align: left; cursor: pointer; }
.select-field > span { overflow: hidden; color: #555; font-size: inherit; text-overflow: ellipsis; white-space: nowrap; }
.select-field > span:not(.is-placeholder) { color: #000; }
.select-field > span.is-placeholder { color: #555; }
.select-chevron { flex: 0 0 auto; color: #777; }
.select-menu { position: absolute; z-index: 20; top: calc(100% + 6px); right: 0; left: 0; display: grid; gap: 2px; padding: 5px; background: #fff; border: 1px solid #e2e2e2; border-radius: 8px; box-shadow: 0 6px 18px rgb(0 0 0 / 12%); }
.select-option { min-height: 36px; padding: 0 10px; color: #333; font: inherit; text-align: left; background: transparent; border: 0; border-radius: 5px; cursor: pointer; }
.select-option:hover, .select-option.is-selected { background: #f2f2f2; }
.select-option.is-selected { font-weight: 600; }
.filter-field > input { width: 100%; min-width: 0; height: 100%; padding: 0; color: #000; font: inherit; background: transparent; border: 0; outline: 0; }
.filter-field > input::placeholder { color: #555; opacity: 1; }
.search-field { gap: 9px; padding-right: 5px; color: #555; }
.search-field input { flex: 1; }
.search-field button { height: 33px; padding: 0 15px; color: #fff; font-size: 14px; font-weight: 500; white-space: nowrap; background: #252525; border: 1px solid #252525; border-radius: 6px; cursor: pointer; }
.search-field button:hover { background: #414141; }
@media (max-width: 1120px) { .orders-toolbar { grid-template-columns: 230px 170px 180px; }.search-field { grid-column: 1 / -1; } }
@media (max-width: 700px) { .orders-toolbar { grid-template-columns: minmax(0, 1fr); gap: 8px; }.search-field { grid-column: auto; }.date-range { min-width: 0; } }
</style>
