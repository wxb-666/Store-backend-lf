<template>
  <div class="orders-table-wrap">
    <table class="orders-table">
      <thead><tr><th class="select-column"><input v-model="allSelected" type="checkbox" :aria-label="t('orders.selectAll')" /></th><th>{{ t('orders.order') }}</th><th>{{ t('orders.purchaseOrder') }}</th><th>{{ t('orders.date') }} <span>↓</span></th><th>{{ t('orders.customer') }}</th><th>{{ t('orders.status') }}</th><th class="total-column">{{ t('orders.total') }}</th></tr></thead>
      <tbody><tr v-for="order in visibleOrders" :key="order.number"><td><input v-model="selectedOrderNumbers" :value="order.number" type="checkbox" :aria-label="t('orders.select') + ' ' + order.number" /></td><td><button class="order-number" type="button">{{ order.number }}</button></td><td></td><td>{{ t(order.dateKey) }}</td><td><template v-if="order.customer === 'no-customer'">{{ t('orders.noCustomer') }}</template><template v-else>{{ order.customer }}<small v-if="order.company">{{ order.company }}</small></template></td><td><span class="status-badge"><i />{{ t('orders.unfulfilled') }}</span></td><td class="total-column">{{ order.total }} USD</td></tr></tbody>
    </table>
    <p v-if="visibleOrders.length === 0" class="empty-state">{{ t('orders.empty') }}</p>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { t } from '../../stores/locale'
type Order = { number: string; dateKey: 'orders.yesterday245' | 'orders.yesterday217'; customer: string; company?: string; total: string }
const props = defineProps<{ query: string }>()
const orders: Order[] = [
  { number: '#D11', dateKey: 'orders.yesterday245', customer: 'no-customer', total: '$150.00' },
  { number: '#D10', dateKey: 'orders.yesterday217', customer: 'RubyKarine', company: 'Snowdevil', total: '$693.45' },
  { number: '#D9', dateKey: 'orders.yesterday217', customer: 'WinfieldRussell', total: '$3,163.40' },
  { number: '#D8', dateKey: 'orders.yesterday217', customer: 'RubyKarine', company: 'Snowdevil', total: '$1,994.85' },
  { number: '#D7', dateKey: 'orders.yesterday217', customer: 'WinfieldRussell', total: '$1,687.13' },
  { number: '#D6', dateKey: 'orders.yesterday217', customer: 'RubyKarine', company: 'Snowdevil', total: '$664.95' },
  { number: '#D5', dateKey: 'orders.yesterday217', customer: 'WinfieldRussell', total: '$1,196.91' },
  { number: '#D4', dateKey: 'orders.yesterday217', customer: 'no-customer', total: '$885.95' },
  { number: '#D3', dateKey: 'orders.yesterday217', customer: 'no-customer', total: '$885.95' },
  { number: '#D2', dateKey: 'orders.yesterday217', customer: 'no-customer', total: '$2,799.80' },
  { number: '#D1', dateKey: 'orders.yesterday217', customer: 'WinfieldRussell', total: '$200.00' },
]
const selectedOrderNumbers = ref<string[]>([])
const visibleOrders = computed(() => { const keyword = props.query.trim().toLowerCase(); return keyword ? orders.filter((order) => Object.values(order).some((value) => value?.toLowerCase().includes(keyword)) || t(order.dateKey).toLowerCase().includes(keyword)) : orders })
const allSelected = computed({ get: () => visibleOrders.value.length > 0 && visibleOrders.value.every((order) => selectedOrderNumbers.value.includes(order.number)), set: (checked: boolean) => { selectedOrderNumbers.value = checked ? visibleOrders.value.map((order) => order.number) : [] } })
</script>

<style scoped>
.orders-table-wrap { min-height: 0; overflow: auto; }.orders-table { width: 100%; min-width: 880px; border-spacing: 0; border-collapse: separate; font-size: 15px; }.orders-table th { height: 39px; padding: 0 15px; color: #333; font-weight: 500; text-align: left; background: #f5f5f5; }.orders-table th:first-child { border-radius: 13px 0 0 13px; }.orders-table th:last-child { border-radius: 0 13px 13px 0; }.orders-table td { height: 41px; padding: 0 15px; color: #151515; border-bottom: 1px solid #ececec; }.orders-table tbody tr:last-child td { border-bottom: 0; }.select-column { width: 36px; }.orders-table input { appearance: none; width: 20px; height: 20px; vertical-align: middle; background: white; border: 1px solid #c4c4c4; border-radius: 6px; }.orders-table input:checked { background: #111; border-color: #111; box-shadow: inset 0 0 0 5px white; }.order-number { padding: 0; color: #111; font-weight: 600; background: transparent; border: 0; }.order-number:hover { text-decoration: underline; }small { display: block; margin-top: 3px; color: #353535; font-size: 14px; }.status-badge { display: inline-flex; align-items: center; gap: 7px; padding: 4px 10px; background: #ffe36b; border-radius: 9px; }.status-badge i { width: 12px; height: 12px; border: 1.5px solid #645608; border-radius: 50%; }.total-column { text-align: right !important; }th span { margin-left: 3px; }.empty-state { padding: 54px; color: #666; text-align: center; }
</style>
