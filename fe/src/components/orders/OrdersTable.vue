<template>
  <div class="orders-table-wrap">
    <table class="orders-table">
      <thead><tr><th class="select-column"><input v-model="allSelected" type="checkbox" :aria-label="t('orders.selectAll')" /></th><th>Order number</th><th>Payment time</th><th>Payment status</th><th>Payment method</th><th>Logitics status</th><th>Total amout</th><th>Number of products</th><th>Country/Region</th><th>Operation</th></tr></thead>
      <tbody><tr v-for="order in visibleOrders" :key="order.number"><td><input v-model="selectedOrderNumbers" :value="order.number" :aria-label="t('orders.select') + ' ' + order.number" type="checkbox" /></td><td><button class="order-number" type="button">{{ order.number }}</button></td><td>{{ order.paymentTime }}</td><td>{{ order.paymentStatus }}</td><td>{{ order.paymentMethod }}</td><td>{{ order.logisticsStatus }}</td><td>{{ order.totalAmount }}</td><td>{{ order.productCount }}</td><td>{{ order.countryRegion }}</td><td>{{ order.operation }}</td></tr></tbody>
    </table>
    <p v-if="visibleOrders.length === 0" class="empty-state">{{ t('orders.empty') }}</p>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { t } from '../../stores/locale'
type Order = { number: string; paymentTime: string; paymentStatus: string; paymentMethod: string; logisticsStatus: string; totalAmount: string; productCount: number; countryRegion: string; operation: string }
const props = defineProps<{ query: string }>()
const orders: Order[] = [
  { number: '#D11', paymentTime: '2026-11-17 04:45', paymentStatus: 'Paid', paymentMethod: 'Credit card', logisticsStatus: 'Unfulfilled', totalAmount: '$150.00', productCount: 1, countryRegion: 'United States', operation: 'View' },
  { number: '#D10', paymentTime: '2026-11-17 02:17', paymentStatus: 'Paid', paymentMethod: 'PayPal', logisticsStatus: 'Unfulfilled', totalAmount: '$693.45', productCount: 3, countryRegion: 'Canada', operation: 'View' },
  { number: '#D9', paymentTime: '2026-11-17 02:17', paymentStatus: 'Paid', paymentMethod: 'Credit card', logisticsStatus: 'Fulfilled', totalAmount: '$3,163.40', productCount: 5, countryRegion: 'United States', operation: 'View' },
  { number: '#D8', paymentTime: '2026-11-16 18:32', paymentStatus: 'Paid', paymentMethod: 'Shop Pay', logisticsStatus: 'Fulfilled', totalAmount: '$1,994.85', productCount: 4, countryRegion: 'United Kingdom', operation: 'View' },
  { number: '#D7', paymentTime: '2026-11-16 15:46', paymentStatus: 'Paid', paymentMethod: 'Credit card', logisticsStatus: 'Unfulfilled', totalAmount: '$1,687.13', productCount: 2, countryRegion: 'Australia', operation: 'View' },
  { number: '#D6', paymentTime: '2026-11-16 11:20', paymentStatus: 'Paid', paymentMethod: 'PayPal', logisticsStatus: 'Fulfilled', totalAmount: '$664.95', productCount: 2, countryRegion: 'Germany', operation: 'View' },
  { number: '#D5', paymentTime: '2026-11-16 09:14', paymentStatus: 'Paid', paymentMethod: 'Shop Pay', logisticsStatus: 'Unfulfilled', totalAmount: '$1,196.91', productCount: 3, countryRegion: 'France', operation: 'View' },
  { number: '#D4', paymentTime: '2026-11-15 21:08', paymentStatus: 'Paid', paymentMethod: 'Credit card', logisticsStatus: 'Fulfilled', totalAmount: '$885.95', productCount: 1, countryRegion: 'Japan', operation: 'View' },
  { number: '#D3', paymentTime: '2026-11-15 17:50', paymentStatus: 'Paid', paymentMethod: 'Credit card', logisticsStatus: 'Unfulfilled', totalAmount: '$885.95', productCount: 2, countryRegion: 'Singapore', operation: 'View' },
  { number: '#D2', paymentTime: '2026-11-15 14:05', paymentStatus: 'Paid', paymentMethod: 'PayPal', logisticsStatus: 'Fulfilled', totalAmount: '$2,799.80', productCount: 6, countryRegion: 'United States', operation: 'View' },
  { number: '#D1', paymentTime: '2026-11-15 10:36', paymentStatus: 'Paid', paymentMethod: 'Shop Pay', logisticsStatus: 'Unfulfilled', totalAmount: '$200.00', productCount: 1, countryRegion: 'Canada', operation: 'View' },
]
const selectedOrderNumbers = ref<string[]>([])
const visibleOrders = computed(() => { const keyword = props.query.trim().toLowerCase(); return keyword ? orders.filter((order) => Object.values(order).some((value) => String(value).toLowerCase().includes(keyword))) : orders })
const allSelected = computed({ get: () => visibleOrders.value.length > 0 && visibleOrders.value.every((order) => selectedOrderNumbers.value.includes(order.number)), set: (checked: boolean) => { selectedOrderNumbers.value = checked ? visibleOrders.value.map((order) => order.number) : [] } })
</script>

<style scoped>
.orders-table-wrap { min-height: 0; overflow: auto; }.orders-table { width: 100%; min-width: 1440px; border-spacing: 0; border-collapse: separate; font-size: 15px; }.orders-table th { height: 39px; padding: 0 15px; color: #333; font-weight: 500; text-align: left; white-space: nowrap; background: #f5f5f5; }.orders-table th:first-child { border-radius: 13px 0 0 13px; }.orders-table th:last-child { border-radius: 0 13px 13px 0; }.orders-table td { height: 41px; padding: 0 15px; color: #151515; white-space: nowrap; border-bottom: 1px solid #ececec; }.orders-table tbody tr:last-child td { border-bottom: 0; }.select-column { width: 36px; }.orders-table input { appearance: none; width: 20px; height: 20px; vertical-align: middle; background: white; border: 1px solid #c4c4c4; border-radius: 6px; }.orders-table input:checked { background: #111; border-color: #111; box-shadow: inset 0 0 0 5px white; }.order-number { padding: 0; color: #111; font-weight: 600; background: transparent; border: 0; }.order-number:hover { text-decoration: underline; }.empty-state { padding: 54px; color: #666; text-align: center; }
</style>
