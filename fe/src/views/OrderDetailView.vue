<template>
  <section class="order-detail-view">
    <header class="detail-header">
      <div class="heading-group">
        <button class="back-button" type="button" @click="backToOrders">‹ <span>All orders</span></button>
      </div>
      <div class="header-actions">
        <button class="secondary-button" type="button" disabled>Invoice</button>
        <button class="secondary-button" type="button" disabled>Action</button>
        <button class="primary-button" type="button" disabled>Delivery</button>
      </div>
    </header>

    <div class="detail-content" :aria-busy="loading">
      <p v-if="loading" class="state-message" role="status">Loading order details…</p>
      <div v-else-if="errorMessage" class="state-message error-message" role="alert">
        <p>{{ errorMessage }}</p>
        <button class="secondary-button" type="button" @click="loadOrder">Retry</button>
      </div>
      <template v-else-if="order">
        <div class="detail-columns">
          <div class="primary-column">
            <article class="detail-card overview-card">
              <h2>Order overview</h2>
              <div class="product-heading"><span>Product</span><span>Specifications</span><span>Selling price × quantity</span></div>
              <div v-for="item in order.order_items" :key="item.id" class="product-row">
                <div class="product-info">
                  <img :src="item.product_image || fallbackImage" :alt="item.product_name" @error="useFallbackImage" />
                  <div class="product-copy"><strong>{{ item.product_name }}</strong><span>SKU: {{ item.product_sku }}</span></div>
                </div>
                <span class="specification">{{ item.specifications || '—' }}</span>
                <span class="line-price">{{ formatAmount(item.product_price, order.order_info.currency_code) }} × {{ item.product_number }}</span>
              </div>
              <p v-if="order.order_items.length === 0" class="empty-items">No product details available.</p>
            </article>

            <article class="detail-card address-card">
              <div class="card-heading"><h2>Shipping address</h2></div>
              <dl class="address-fields">
                <div><dt>Name</dt><dd>{{ value(order.customer_info.customer_name) }}</dd></div>
                <div><dt>Address</dt><dd>{{ value(order.customer_info.address) }}</dd></div>
                <div><dt>Apartment</dt><dd>{{ value(order.customer_info.apartment) }}</dd></div>
                <div><dt>City</dt><dd>{{ value(order.customer_info.city) }}</dd></div>
                <div><dt>Country/Region</dt><dd>{{ value(order.customer_info.country_region) }}</dd></div>
                <div><dt>Province/State</dt><dd>{{ value(order.customer_info.province_state) }}</dd></div>
                <div><dt>Postcode</dt><dd>{{ value(order.customer_info.postcode) }}</dd></div>
                <div><dt>Phone</dt><dd>{{ value(order.customer_info.phone) }}</dd></div>
                <div class="extra-field"><dt>Extra information</dt><dd>{{ value(order.customer_info.extra_information) }}</dd></div>
              </dl>
            </article>
          </div>

          <aside class="secondary-column">
            <article class="detail-card information-card">
              <h2>Order information</h2>
              <div class="status-summary">
                <p><span>Order status</span><span class="status-chip">{{ formatStatus(order.order_info.order_status) }}</span></p>
                <p><span>Payment status</span><span class="status-chip" :class="{ 'is-paid': order.payment_info.payment_status?.toLowerCase() === 'paid' }">{{ formatStatus(order.payment_info.payment_status) }}</span></p>
                <p class="total-summary"><span>Total amount</span><strong>{{ formatAmount(order.order_info.total_amount, order.order_info.currency_code) }}</strong></p>
              </div>
              <dl class="order-fields">
                <div><dt>Order number</dt><dd>{{ order.order_info.order_number }}</dd></div>
                <div><dt>Payment number</dt><dd>{{ value(order.payment_info.payment_number) }}</dd></div>
                <div><dt>Payment method</dt><dd>{{ formatStatus(order.payment_info.payment_method) }}</dd></div>
                <div><dt>Generation time</dt><dd>{{ formatDate(order.order_info.generation_time) }}</dd></div>
                <div><dt>Payment time</dt><dd>{{ formatDate(order.payment_info.payment_time) }}</dd></div>
                <div><dt>Logistics status</dt><dd>{{ formatStatus(order.logistics_info.logistics_status) }}</dd></div>
                <div><dt>Logistic order number</dt><dd>{{ value(order.logistics_info.logistic_order_number) }}</dd></div>
              </dl>
            </article>

            <article class="detail-card customer-card">
              <div class="card-heading"><h2>Client</h2><span class="customer-tag">Customer</span></div>
              <dl class="customer-fields">
                <div><dt>Name</dt><dd>{{ value(order.customer_info.customer_name) }}</dd></div>
              </dl>
              <h3>Contact information</h3>
              <dl class="customer-fields"><div><dt>Mailbox</dt><dd>{{ value(order.customer_info.mailbox) }}</dd></div></dl>
            </article>
          </aside>
        </div>
      </template>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onUnmounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { fetchOrderDetail, type OrderDetail } from '../api/orders'

const props = defineProps<{ orderId: string }>()
const route = useRoute()
const router = useRouter()
const domain = computed(() => typeof route.query.domain === 'string' ? route.query.domain : '')
const order = ref<OrderDetail | null>(null)
const loading = ref(false)
const errorMessage = ref('')
const fallbackImage = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"%3E%3Crect width="48" height="48" fill="%23f1f1f1"/%3E%3Cpath d="M10 34l9-10 6 6 5-5 8 9H10z" fill="%23c8c8c8"/%3E%3Ccircle cx="17" cy="16" r="3" fill="%23c8c8c8"/%3E%3C/svg%3E'
let activeController: AbortController | undefined

watch(() => [props.orderId, domain.value], () => { void loadOrder() }, { immediate: true })
onUnmounted(() => activeController?.abort())

async function loadOrder() {
  activeController?.abort()
  const controller = new AbortController()
  activeController = controller
  order.value = null
  errorMessage.value = ''
  if (!domain.value) {
    loading.value = false
    errorMessage.value = 'The store domain is missing from this order link.'
    return
  }
  const orderId = Number(props.orderId)
  if (!Number.isSafeInteger(orderId) || orderId < 1) {
    loading.value = false
    errorMessage.value = 'The order ID is invalid.'
    return
  }
  loading.value = true
  try {
    order.value = await fetchOrderDetail(orderId, domain.value, controller.signal)
  } catch (error) {
    if (controller.signal.aborted) return
    errorMessage.value = error instanceof Error ? error.message : 'Unable to load order details.'
  } finally {
    if (!controller.signal.aborted) loading.value = false
  }
}

function backToOrders() { void router.push({ name: 'allOrders' }) }
function value(text: string | null) { return text?.trim() || '—' }
function formatStatus(text: string | null) {
  if (!text) return '—'
  const labels: Record<string, string> = { paypal: 'PayPal', paypal_rest: 'PayPal', credit_card: 'Credit card', shop_pay: 'Shop Pay', paid: 'Paid', pending: 'Pending', refunded: 'Refunded', unfulfilled: 'Unfulfilled', fulfilled: 'Fulfilled', delivered: 'Delivered', in_progress: 'In progress' }
  return labels[text.toLowerCase()] || text.replaceAll('_', ' ').replace(/\b\w/g, (letter) => letter.toUpperCase())
}
function formatDate(text: string | null) {
  if (!text) return '—'
  const date = new Date(text)
  if (Number.isNaN(date.getTime())) return text
  const pad = (part: number) => String(part).padStart(2, '0')
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`
}
function formatAmount(amount: string, currency: string) {
  try { return new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(Number(amount)) }
  catch { return `${currency} ${amount}` }
}
function useFallbackImage(event: Event) { (event.target as HTMLImageElement).src = fallbackImage }
</script>

<style scoped>
.order-detail-view { display: flex; flex: 1; flex-direction: column; min-width: 0; min-height: 0; overflow: hidden; background: #f7f7f7; }
.detail-header { display: flex; align-items: center; justify-content: space-between; min-height: 82px; gap: 20px; padding: 14px 28px; background: #fff; border-bottom: 1px solid #ededed; }
.heading-group { display: flex; align-items: center; }.back-button { justify-self: start; padding: 0; color: #666; font-size: 16px; background: transparent; border: 0; }.back-button:hover { color: #111; }.back-button span { text-decoration: underline; text-underline-offset: 2px; }
.header-actions { display: flex; gap: 8px; }
.secondary-button, .primary-button { min-height: 36px; padding: 0 15px; border-radius: 9px; }.secondary-button { color: #000; background: #fff; border: 1px solid #dedede; }.primary-button { color: #fff; background: #000; border: 1px solid #000; }.header-actions button:disabled { opacity: 1; cursor: default; }
.detail-content { flex: 1; min-height: 0; padding: 22px 26px 40px; overflow: auto; }.detail-columns { display: grid; grid-template-columns: minmax(0, 1.65fr) minmax(320px, 1fr); align-items: start; gap: 18px; max-width: 1600px; margin: 0 auto; }.primary-column, .secondary-column { display: grid; align-content: start; gap: 16px; min-width: 0; }
.detail-card { min-width: 0; padding: 18px 20px; background: #fff; border: 1px solid #e6e6e6; border-radius: 12px; box-shadow: 0 1px 3px rgb(0 0 0 / 4%); }.detail-card h2 { margin: 0; color: #252525; font-size: 16px; font-weight: 600; }.product-heading, .product-row { display: grid; grid-template-columns: minmax(0, 1.6fr) minmax(120px, .9fr) minmax(130px, .7fr); align-items: center; gap: 14px; }.product-heading { padding: 18px 8px 10px; color: #707070; font-size: 13px; }.product-row { min-height: 76px; padding: 10px 8px; border-top: 1px solid #ededed; }.product-info { display: flex; align-items: center; min-width: 0; gap: 12px; }.product-info img { flex: 0 0 auto; width: 48px; height: 48px; object-fit: cover; background: #f4f4f4; border: 1px solid #e8e8e8; border-radius: 7px; }.product-copy { display: grid; min-width: 0; gap: 5px; }.product-copy strong { overflow-wrap: anywhere; color: #d9803c; font-size: 13px; font-weight: 600; }.product-copy span, .specification, .line-price { overflow-wrap: anywhere; color: #555; font-size: 13px; }.empty-items { padding: 18px 8px; margin: 0; color: #777; border-top: 1px solid #ededed; }
.card-heading { display: flex; align-items: center; gap: 8px; }.customer-tag { padding: 4px 8px; color: #38694b; font-size: 11px; font-weight: 600; background: #edf7ef; border: 1px solid #cfe5d3; border-radius: 12px; }.address-fields, .order-fields, .customer-fields { margin: 14px 0 0; }.address-fields > div, .order-fields > div, .customer-fields > div { display: grid; grid-template-columns: minmax(125px, .65fr) minmax(0, 1.5fr); gap: 12px; padding: 10px 0; border-bottom: 1px solid #ededed; }.address-fields > div:last-child, .order-fields > div:last-child, .customer-fields > div:last-child { border-bottom: 0; }.address-fields dt, .order-fields dt, .customer-fields dt { color: #737373; font-size: 13px; }.address-fields dd, .order-fields dd, .customer-fields dd { min-width: 0; margin: 0; color: #333; font-size: 13px; overflow-wrap: anywhere; }.extra-field dd { white-space: pre-wrap; }
.status-summary { display: grid; gap: 10px; padding: 16px 0; margin-top: 12px; border-bottom: 1px solid #e8e8e8; }.status-summary p { display: flex; align-items: center; gap: 7px; margin: 0; color: #555; font-size: 13px; }.status-chip { padding: 3px 9px; color: #555; background: #f5f5f5; border: 1px solid #e6e6e6; border-radius: 12px; }.status-chip.is-paid { color: #176b47; background: #eaf6ee; border-color: #c8e9d4; }.status-summary .total-summary { align-items: baseline; padding-top: 3px; }.total-summary strong { color: #202020; font-size: 20px; }.information-card .order-fields { margin-top: 4px; }.customer-card h3 { margin: 17px 0 0; color: #333; font-size: 14px; font-weight: 600; }
.state-message { display: grid; justify-items: center; gap: 12px; padding: 60px 20px; color: #666; text-align: center; }.state-message p { margin: 0; }.error-message { color: #a42a22; }
@media (max-width: 980px) { .detail-columns { grid-template-columns: minmax(0, 1fr); }.secondary-column { grid-template-columns: repeat(2, minmax(0, 1fr)); align-items: start; } }
@media (max-width: 700px) { .detail-header { align-items: flex-start; flex-direction: column; padding: 14px 18px; }.header-actions { flex-wrap: wrap; }.detail-content { padding: 14px 12px 28px; }.detail-card { padding: 15px; }.product-heading { display: none; }.product-row { grid-template-columns: minmax(0, 1fr); gap: 10px; }.secondary-column { grid-template-columns: minmax(0, 1fr); }.address-fields > div, .order-fields > div, .customer-fields > div { grid-template-columns: minmax(105px, .7fr) minmax(0, 1.3fr); } }
</style>
