<template>
  <div class="orders-table-wrap">
    <table class="orders-table" :aria-busy="loading">
      <thead>
        <tr>
          <th class="select-column"><input v-model="allSelected" type="checkbox" :aria-label="t('orders.selectAll')" /></th>
          <th>Order number</th>
          <th :aria-sort="sortDirection === 'asc' ? 'ascending' : 'descending'">
            <button class="sort-heading" type="button" :aria-label="`Sort by payment time ${sortDirection === 'desc' ? 'ascending' : 'descending'}`" @click="toggleSort">
              Payment time<span class="sort-arrows" aria-hidden="true"><span :class="{ active: sortDirection === 'asc' }">▲</span><span :class="{ active: sortDirection === 'desc' }">▼</span></span>
            </button>
          </th>
          <th>Payment status</th><th>Payment method</th><th>Logistics status</th><th>Total amount</th><th>Number of products</th><th>Country/Region</th><th>Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.order_id">
          <td><input v-model="selectedOrderIds" :value="order.order_id" :aria-label="`${t('orders.select')} ${order.order_number}`" type="checkbox" /></td>
          <td><button class="order-number" type="button">{{ order.order_number }}</button></td>
          <td>{{ formatDate(order.payment_time) }}</td>
          <td><span class="status-value" :class="statusClass(order.payment_status)">{{ formatStatus(order.payment_status) }}</span></td>
          <td>{{ formatStatus(order.payment_method) }}</td>
          <td><span class="status-value logistics-value">{{ formatStatus(order.logistics_status) }}</span></td>
          <td>{{ formatAmount(order.total_amount, order.currency_code) }}</td>
          <td>
            <div class="product-cell" :class="{ 'is-open': activeProductOrderId === order.order_id }">
              <div class="product-preview" :aria-label="`${order.number_of_products} products`">
              <div class="product-images">
                <img
                  v-for="product in order.product_items.slice(0, 3)"
                  :key="product.product_id"
                  class="product-image"
                  :src="product.product_image || fallbackImage"
                  :alt="product.product_name"
                  :title="`${product.product_name} · ${product.product_number}`"
                  loading="lazy"
                  @error="useFallbackImage"
                />
                <span v-if="order.product_items.length === 0" class="product-image product-placeholder" aria-hidden="true">—</span>
              </div>
                <button
                  class="product-details-toggle"
                  type="button"
                  :aria-expanded="activeProductOrderId === order.order_id"
                  :aria-controls="`product-details-${order.order_id}`"
                  :aria-label="`${activeProductOrderId === order.order_id ? 'Hide' : 'Show'} products for ${order.order_number}`"
                  @click="toggleProductDetails(order, $event)"
                >
                  <span class="product-count">{{ order.number_of_products }}</span>
                  <span class="product-chevron" :class="{ 'is-open': activeProductOrderId === order.order_id }" aria-hidden="true"></span>
                </button>
              </div>
            </div>
          </td>
          <td>{{ order.country_region || '—' }}</td>
          <td><button class="operation-button" type="button">View</button></td>
        </tr>
      </tbody>
    </table>
    <p v-if="loading" class="table-message" role="status">Loading orders…</p>
    <p v-else-if="errorMessage" class="table-message error-message" role="alert">{{ errorMessage }} <button type="button" @click="loadOrders">Retry</button></p>
    <p v-else-if="orders.length === 0" class="table-message">{{ t('orders.empty') }}</p>
    <footer v-if="!errorMessage" class="pagination">
      <span class="total-count">{{ total }} {{ total === 1 ? 'order' : 'orders' }}</span>
      <div class="page-controls">
        <button type="button" :disabled="page <= 1 || loading" aria-label="Previous page" @click="page--">‹</button>
        <span>Page {{ page }} of {{ totalPages || 1 }}</span>
        <button type="button" :disabled="page >= totalPages || loading" aria-label="Next page" @click="page++">›</button>
      </div>
      <div ref="pageSizeFilter" class="page-size">
        <span>Rows per page</span>
        <div class="page-size-select">
          <button class="page-size-trigger" type="button" aria-haspopup="listbox" :aria-expanded="pageSizeOpen" @click="pageSizeOpen = !pageSizeOpen">
            {{ pageSize }}<span class="page-size-chevron" :class="{ 'is-open': pageSizeOpen }" aria-hidden="true"></span>
          </button>
          <div v-if="pageSizeOpen" class="page-size-menu" role="listbox" aria-label="Rows per page">
            <button v-for="size in [20, 50, 100]" :key="size" class="page-size-option" :class="{ 'is-selected': pageSize === size }" type="button" role="option" :aria-selected="pageSize === size" @click="selectPageSize(size)">
              {{ size }}
            </button>
          </div>
        </div>
      </div>
    </footer>
    <Teleport to="body">
      <div
        v-if="activeProductOrder"
        :id="`product-details-${activeProductOrder.order_id}`"
        class="product-details"
        :style="{ top: `${productDetailsPosition.top}px`, left: `${productDetailsPosition.left}px` }"
        aria-label="Order products"
      >
        <div v-for="product in activeProductOrder.product_items.slice(0, 3)" :key="product.product_id" class="product-detail">
          <div class="product-detail-image-wrap">
            <img class="product-detail-image" :src="product.product_image || fallbackImage" :alt="product.product_name" @error="useFallbackImage" />
            <span class="product-quantity">{{ product.product_number }}</span>
          </div>
          <div class="product-detail-copy">
            <strong>{{ product.product_name }}</strong>
            <span>SKU: {{ product.product_sku }}</span>
          </div>
        </div>
        <p v-if="activeProductOrder.product_items.length === 0" class="no-products">No product details available.</p>
      </div>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref, watch } from 'vue'
import { fetchOrders, type OrderListItem } from '../../api/orders'
import { t } from '../../stores/locale'

const props = defineProps<{ query: string; paymentMethod: string; domain: string }>()
const orders = ref<OrderListItem[]>([])
const selectedOrderIds = ref<number[]>([])
const sortDirection = ref<'asc' | 'desc'>('desc')
const page = ref(1)
const pageSize = ref(20)
const total = ref(0)
const loading = ref(false)
const errorMessage = ref('')
const pageSizeOpen = ref(false)
const pageSizeFilter = ref<HTMLElement | null>(null)
const activeProductOrderId = ref<number | null>(null)
const productDetailsPosition = ref({ top: 0, left: 0 })
const activeProductOrder = computed(() => orders.value.find((order) => order.order_id === activeProductOrderId.value) ?? null)
const totalPages = computed(() => Math.ceil(total.value / pageSize.value))
const fallbackImage = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"%3E%3Crect width="48" height="48" fill="%23f1f1f1"/%3E%3Cpath d="M10 34l9-10 6 6 5-5 8 9H10z" fill="%23c8c8c8"/%3E%3Ccircle cx="17" cy="16" r="3" fill="%23c8c8c8"/%3E%3C/svg%3E'
let activeController: AbortController | undefined

watch(() => [props.query, props.paymentMethod, props.domain, page.value, pageSize.value, sortDirection.value], () => { activeProductOrderId.value = null; void loadOrders() }, { immediate: true })
onMounted(() => {
  document.addEventListener('pointerdown', closeProductDetailsOnOutside)
  window.addEventListener('scroll', closeProductDetails, true)
  window.addEventListener('resize', closeProductDetails)
})
onUnmounted(() => {
  activeController?.abort()
  document.removeEventListener('pointerdown', closeProductDetailsOnOutside)
  window.removeEventListener('scroll', closeProductDetails, true)
  window.removeEventListener('resize', closeProductDetails)
})

async function loadOrders() {
  activeController?.abort()
  const controller = new AbortController()
  activeController = controller
  loading.value = true
  errorMessage.value = ''
  try {
    const result = await fetchOrders({
      page: page.value,
      pageSize: pageSize.value,
      query: props.query.trim() || undefined,
      paymentMethod: props.paymentMethod || undefined,
      domain: props.domain.trim() || undefined,
      sortOrder: sortDirection.value,
    }, controller.signal)
    if (controller.signal.aborted) return
    orders.value = result.items
    total.value = result.total
    selectedOrderIds.value = selectedOrderIds.value.filter((id) => result.items.some((order) => order.order_id === id))
  } catch (error) {
    if (controller.signal.aborted) return
    errorMessage.value = error instanceof Error ? error.message : 'Unable to load orders. Please try again.'
    orders.value = []
    total.value = 0
  } finally {
    if (!controller.signal.aborted) loading.value = false
  }
}

function toggleSort() { sortDirection.value = sortDirection.value === 'desc' ? 'asc' : 'desc' }
function toggleProductDetails(order: OrderListItem, event: MouseEvent) {
  if (activeProductOrderId.value === order.order_id) {
    activeProductOrderId.value = null
    return
  }
  const trigger = event.currentTarget as HTMLElement
  const bounds = trigger.getBoundingClientRect()
  const count = Math.max(1, Math.min(order.product_items.length, 3))
  const estimatedHeight = count * 100 + 40
  const panelWidth = 340
  const below = bounds.bottom + 8
  const top = below + estimatedHeight <= window.innerHeight - 12
    ? below
    : Math.max(12, bounds.top - estimatedHeight - 8)
  const left = Math.max(12, Math.min(bounds.right - panelWidth, window.innerWidth - panelWidth - 12))
  productDetailsPosition.value = { top, left }
  activeProductOrderId.value = order.order_id
}
function closeProductDetails() { activeProductOrderId.value = null }
function closeProductDetailsOnOutside(event: PointerEvent) {
  const target = event.target
  if (target instanceof Element && target.closest('.product-details, .product-details-toggle')) return
  if (!(target instanceof Node && pageSizeFilter.value?.contains(target))) pageSizeOpen.value = false
  closeProductDetails()
}
function selectPageSize(size: number) {
  pageSize.value = size
  page.value = 1
  pageSizeOpen.value = false
}
const allSelected = computed({
  get: () => orders.value.length > 0 && orders.value.every((order) => selectedOrderIds.value.includes(order.order_id)),
  set: (checked: boolean) => { selectedOrderIds.value = checked ? [...new Set([...selectedOrderIds.value, ...orders.value.map((order) => order.order_id)])] : selectedOrderIds.value.filter((id) => !orders.value.some((order) => order.order_id === id)) },
})
function formatDate(value: string | null) {
  if (!value) return '—'
  const date = new Date(value)
  if (Number.isNaN(date.getTime())) return value
  const pad = (part: number) => String(part).padStart(2, '0')
  return `${date.getFullYear()}:${pad(date.getMonth() + 1)}:${pad(date.getDate())} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`
}
function formatAmount(amount: string, currency: string) {
  const value = Number(amount)
  try { return new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(value) } catch { return `${currency} ${amount}` }
}
function formatStatus(value: string | null) {
  if (!value) return '—'
  const labels: Record<string, string> = { paypal: 'PayPal', paypal_rest: 'PayPal', credit_card: 'Credit card', shop_pay: 'Shop Pay', paid: 'Paid', pending: 'Pending', refunded: 'Refunded', unfulfilled: 'Unfulfilled', fulfilled: 'Fulfilled', delivered: 'Delivered' }
  return labels[value.toLowerCase()] || value.replaceAll('_', ' ').replace(/\b\w/g, (letter) => letter.toUpperCase())
}
function statusClass(value: string | null) { return value?.toLowerCase() === 'paid' ? 'paid-value' : '' }
function useFallbackImage(event: Event) { const target = event.target as HTMLImageElement; target.src = fallbackImage }
</script>

<style scoped>
.orders-table-wrap { min-height: 0; overflow: auto; background: #fff; border: 1px solid #ededed; border-radius: 12px; }
.orders-table { width: 100%; min-width: 1440px; border-spacing: 0; border-collapse: separate; font-size: 14px; }
.orders-table th { height: 44px; padding: 0 15px; color: #333; font-weight: 500; text-align: left; white-space: nowrap; background: #f5f5f5; }
.orders-table th:first-child { border-radius: 12px 0 0 0; }
.orders-table th:last-child { border-radius: 0 12px 0 0; }
.orders-table td { height: 70px; padding: 8px 15px; color: #303030; white-space: nowrap; border-bottom: 1px solid #ececec; }
.orders-table tbody tr:last-child td { border-bottom: 0; }
.select-column { width: 46px; }
.orders-table input[type='checkbox'] { appearance: none; width: 18px; height: 18px; vertical-align: middle; background: white; border: 1px solid #c4c4c4; border-radius: 5px; }
.orders-table input[type='checkbox']:checked { background: #111; border-color: #111; box-shadow: inset 0 0 0 4px white; }
.sort-heading { display: inline-flex; align-items: center; gap: 6px; padding: 0; color: inherit; font: inherit; background: transparent; border: 0; cursor: pointer; }
.sort-heading:focus-visible { outline: 2px solid #ff8733; outline-offset: 3px; border-radius: 2px; }
.sort-arrows { display: inline-flex; flex-direction: column; color: #b8b8b8; font-size: 9px; line-height: 8px; }
.sort-arrows .active { color: #f58232; }
.order-number { padding: 0; color: #111; font-weight: 600; background: transparent; border: 0; }
.order-number:hover, .operation-button:hover { text-decoration: underline; }
.status-value { display: inline-flex; align-items: center; min-height: 26px; padding: 2px 10px; border: 1px solid #dedede; border-radius: 14px; }
.paid-value { color: #176b47; background: #eaf6ee; border-color: #c8e9d4; }
.logistics-value { color: #424242; }
.product-preview, .product-images { display: flex; align-items: center; }
.product-preview { gap: 10px; }
.product-images { gap: 5px; }
.product-image { display: block; width: 42px; height: 42px; object-fit: cover; background: #f4f4f4; border: 1px solid #e4e4e4; border-radius: 5px; }
.product-placeholder { display: grid; color: #888; font-size: 18px; place-items: center; }
.product-count { color: #333; font-weight: 600; }
.operation-button { padding: 0; color: #eb873f; background: transparent; border: 0; }
.table-message { margin: 0; padding: 40px 20px; color: #666; text-align: center; }
.error-message { color: #b42318; }
.error-message button { margin-left: 8px; color: inherit; background: transparent; border: 0; text-decoration: underline; }
.pagination { display: flex; align-items: center; justify-content: space-between; min-height: 58px; padding: 0 16px; color: #666; font-size: 13px; border-top: 1px solid #ececec; }
.page-controls { display: flex; align-items: center; gap: 10px; }
.page-controls button, .page-size-trigger { min-width: 32px; height: 32px; color: #444; background: white; border: 1px solid #dedede; border-radius: 6px; }
.page-controls button { display: inline-flex; align-items: center; justify-content: center; padding: 0; font-size: 20px; line-height: 1; }
.page-controls button:disabled { color: #aaa; cursor: not-allowed; }
.page-size { display: flex; align-items: center; gap: 8px; }
.page-size-select { position: relative; }
.page-size-trigger { display: inline-flex; min-width: 74px; height: 32px; align-items: center; justify-content: space-between; gap: 6px; padding: 0 8px 0 10px; color: #222; font: inherit; cursor: pointer; }
.page-size-chevron { width: 7px; height: 7px; margin-top: -4px; border-right: 1.5px solid #555; border-bottom: 1.5px solid #555; transform: rotate(45deg); transition: transform 120ms ease; }
.page-size-chevron.is-open { margin-top: 4px; transform: rotate(225deg); }
.page-size-menu { position: absolute; z-index: 30; right: 0; bottom: calc(100% + 6px); display: grid; width: 100%; gap: 2px; padding: 5px; background: #fff; border: 1px solid #e2e2e2; border-radius: 10px; box-shadow: 0 6px 18px rgb(0 0 0 / 12%); }
.page-size-option { min-height: 32px; padding: 0 9px; color: #333; font: inherit; text-align: left; background: transparent; border: 0; border-radius: 7px; cursor: pointer; }
.page-size-option:hover, .page-size-option.is-selected { background: #f2f2f2; }
.page-size-option.is-selected { font-weight: 600; }
.product-cell { position: relative; display: inline-block; }
.product-cell.is-open { z-index: 20; }
.product-count { display: inline-flex; min-width: 26px; height: 26px; align-items: center; justify-content: center; padding: 0 5px; color: #333; font-weight: 600; background: #fff; border: 1px solid #d7d7d7; border-radius: 4px; }
.product-details-toggle { display: inline-flex; width: 48px; min-width: 48px; height: 32px; align-items: center; justify-content: center; gap: 7px; padding: 0; color: #444; background: transparent; border: 1px solid #d7d7d7; border-radius: 5px; }
.product-details-toggle .product-count { display: inline; min-width: 0; height: auto; padding: 0; color: inherit; background: transparent; border: 0; border-radius: 0; }
.product-details-toggle:hover { background: #f7f7f7; }
.product-details-toggle:focus-visible { outline: 2px solid #f58232; outline-offset: 3px; border-radius: 3px; }
.product-chevron { width: 8px; height: 8px; margin: -4px 2px 0; border-right: 1.5px solid currentColor; border-bottom: 1.5px solid currentColor; transform: rotate(45deg); transition: transform 120ms ease; }
.product-chevron.is-open { margin-top: 4px; transform: rotate(225deg); }
.product-details { position: fixed; z-index: 9999; top: 0; right: auto; left: 0; display: grid; width: 340px; max-height: calc(100vh - 24px); gap: 12px; overflow-y: auto; padding: 14px; white-space: normal; background: #fff; border: 1px solid #e5e5e5; border-radius: 8px; box-shadow: 0 8px 24px rgb(0 0 0 / 14%); }
.product-detail { display: flex; align-items: center; gap: 12px; min-width: 0; }
.product-detail-image-wrap { position: relative; flex: 0 0 auto; }
.product-detail-image { display: block; width: 52px; height: 52px; object-fit: cover; background: #f4f4f4; border: 1px solid #e4e4e4; border-radius: 4px; }
.product-quantity { position: absolute; top: -6px; right: -6px; display: grid; min-width: 20px; height: 20px; padding: 0 4px; color: #fff; font-size: 11px; font-weight: 600; place-items: center; background: #f58232; border-radius: 10px; }
.product-detail-copy { display: grid; min-width: 0; gap: 3px; color: #606060; font-size: 11px; line-height: 1.4; }
.product-detail-copy strong { overflow-wrap: anywhere; color: #d9803c; font-size: 12px; font-weight: 600; }
.product-detail-copy span { overflow-wrap: anywhere; }
.no-products { margin: 0; color: #666; font-size: 13px; }
</style>
