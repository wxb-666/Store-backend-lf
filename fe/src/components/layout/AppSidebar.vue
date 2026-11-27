
<template>
  <aside class="sidebar">
    <div class="sidebar__top">
      <span v-if="storeName" class="store-name" :title="storeName">
        {{ storeName }}
      </span>
    </div>

    <button
      class="search-trigger"
      type="button"
      aria-label="Search"
    >
      <AppIcon name="search" :size="19" />
      <span>Search</span>
      <kbd>Ctrl K</kbd>
    </button>

    <nav class="sidebar__navigation" aria-label="Main navigation">
      <SidebarGroup
        class="top-navigation"
        :items="topNavigation"
        :active-item="activeItem"
        @select="handleSelect"
      />

      <SidebarGroup
        class="order-entry"
        :items="orderEntry"
        :active-item="activeItem"
        @select="handleSelect"
      />

      <SidebarGroup
        v-if="activeItem === 'orders'"
        class="order-links"
        :items="orderNavigation"
        :active-item="activeOrderItem"
        @select="handleOrderSelect"
      />

      <!-- Product 一级导航 -->
      <SidebarGroup
        class="product-entry"
        :items="productEntry"
        :active-item="activeItem"
        @select="handleSelect"
      />

      <!-- Product 二级导航 -->
      <SidebarGroup
        v-if="activeItem === 'products'"
        class="product-links"
        :items="productNavigation"
        :active-item="activeProductItem"
        @select="handleProductSelect"
      />
    </nav>

    <div class="sidebar__footer">
      <div class="settings-control">
        <button
          class="nav-item"
          type="button"
          :aria-expanded="showStoreNameInput"
          @click="showStoreNameInput = !showStoreNameInput"
        >
          <AppIcon name="settings" />
          <span>Settings</span>
        </button>

        <Transition name="store-name-panel">
          <label v-if="showStoreNameInput" class="store-name-input">
            <span>Store name</span>
            <input
              v-model.trim="storeName"
              type="text"
              maxlength="40"
              placeholder="Enter store name"
              aria-label="Store name"
            />
          </label>
        </Transition>
      </div>

      <div class="account">
        <span class="account__avatar">SUP</span>
        <strong>support</strong>
        <button
          class="icon-button account__bell"
          type="button"
          aria-label="Notifications"
        >
          <AppIcon name="bell" :size="19" />
        </button>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AppIcon, { type IconName } from '../ui/AppIcon.vue'
import SidebarGroup from './SidebarGroup.vue'

const route = useRoute()
const router = useRouter()

const activeItem = computed(() =>
  route.path === '/home'
    ? 'home'
    : route.path.includes('orders')
      ? 'orders'
      : route.path.startsWith('/products')
        ? 'products'
        : ''
)

const activeOrderItem = computed(() =>
  route.path === '/all_orders'
    ? 'all-orders'
    : route.path === '/abandoned_orders'
      ? 'abandoned-orders'
      : route.path === '/risk_orders'
        ? 'risk-orders'
        : ''
)

const activeProductItem = computed(() => {
  if (route.path === '/products') return 'product-list'
  if (route.path === '/products/stock') return 'stock-list'
  if (route.path === '/products/category') return 'products-category'
  return ''
})

const storeName = ref('')
const showStoreNameInput = ref(false)

type NavigationItem = {
  id: string
  label: string
  icon: IconName
  disabled?: boolean
}

const topNavigation: NavigationItem[] = [
  { id: 'home', label: 'Home', icon: 'home' },
]

const orderEntry: NavigationItem[] = [
  { id: 'orders', label: 'Orders', icon: 'orders' },
]

const orderNavigation: NavigationItem[] = [
  { id: 'all-orders', label: 'All orders', icon: 'orders' },
  {
    id: 'abandoned-orders',
    label: 'Abandoned orders',
    icon: 'orders',
  },
  {
    id: 'risk-orders',
    label: 'Risk orders',
    icon: 'orders',
  },
]

const productEntry: NavigationItem[] = [
  { id: 'products', label: 'Products', icon: 'tag' },
]

const productNavigation: NavigationItem[] = [
  { id: 'product-list', label: 'Product list', icon: 'tag' },
  { id: 'stock-list', label: 'Stock list', icon: 'tag' },
  {
    id: 'products-category',
    label: 'Products category',
    icon: 'tag',
  },
]

const handleSelect = (label: string) => {
  if (label === 'home') {
    void router.push({ name: 'home' })
  }

  if (label === 'orders') {
    void router.push({ name: 'allOrders' })
  }

  if (label === 'products') {
    void router.push({ name: 'productList' })
  }
}

const handleOrderSelect = (label: string) => {
  if (label === 'all-orders') {
    void router.push({ name: 'allOrders' })
  }
}

const handleProductSelect = (label: string) => {
  if (label === 'product-list') {
    void router.push({ name: 'productList' })
  }

  if (label === 'stock-list') {
    void router.push({ name: 'stockList' })
  }

  if (label === 'products-category') {
    void router.push({ name: 'productsCategory' })
  }
}
</script>

<style scoped>
.sidebar { display: flex; flex: 0 0 250px; flex-direction: column; min-width: 0; height: 100%; padding: 20px 16px 16px; color: #b8b8b8; background: #0c0c0c; }
.sidebar__top { display: flex; align-items: center; min-width: 0; height: 34px; gap: 12px; margin: 0 4px 24px; }
.store-name { overflow: hidden; color: #f1f1f1; font-size: 20px; font-weight: 600; text-overflow: ellipsis; white-space: nowrap; }
.icon-button { display: inline-grid; padding: 6px; color: inherit; background: transparent; border: 0; border-radius: 7px; place-items: center; }
.icon-button:hover { color: white; background: #2a2a2a; }
.search-trigger { display: flex; align-items: center; width: 100%; height: 36px; gap: 9px; padding: 0 11px; margin-bottom: 18px; color: #bebebe; text-align: left; background: #303030; border: 0; border-radius: 12px; }.search-trigger span { flex: 1; font-size: 14px; }.search-trigger kbd { color: #bbb; font: inherit; font-size: 13px; }
.sidebar__navigation { flex: 1; min-height: 0; overflow-y: auto; scrollbar-width: none; }.sidebar__navigation::-webkit-scrollbar { display: none; }.sidebar__navigation :deep(.nav-group + .nav-group) { margin-top: 18px; }.sidebar__navigation :deep(.nav-group__title) { padding: 5px 7px 10px; margin: 0; color: #999; font-size: 13px; }.sidebar__navigation :deep(.nav-group__title::after) { margin-left: 5px; content: '›'; }.sidebar__navigation :deep(.nav-group__divider) { height: 1px; margin: 13px 7px; background: #2b2b2b; }
.sidebar__navigation :deep(.nav-item), .nav-item { display: flex; align-items: center; width: 100%; gap: 11px; min-height: 38px; padding: 0 9px; color: #bebebe; font-size: 15px; text-align: left; background: transparent; border: 0; border-radius: 12px; }.sidebar__navigation :deep(.nav-item:hover), .nav-item:hover { color: #fff; background: #252525; }.sidebar__navigation :deep(.nav-item.is-active) { color: #fff; background: linear-gradient(180deg, #353535, #2d2d2d); box-shadow: inset 0 1px #4a4a4a; }
.order-entry { margin-top: 0 !important; }.order-links { margin: 2px 0 6px 18px !important; }.order-links :deep(.nav-item) { min-height: 34px; font-size: 14px; }.order-links :deep(.nav-item svg) { display: none; }.after-order-navigation { margin-top: 4px !important; }
.sidebar__footer { padding-top: 12px; border-top: 1px solid #292929; }.settings-control { position: relative; }.store-name-input { position: absolute; bottom: calc(100% + 7px); left: 0; z-index: 10; display: grid; width: 100%; gap: 6px; padding: 10px; color: #aaa; font-size: 12px; background: #292929; border: 1px solid #494949; border-radius: 9px; box-shadow: 0 10px 24px rgb(0 0 0 / 28%); }.store-name-input input { width: 100%; height: 34px; padding: 0 10px; color: #f1f1f1; font: inherit; font-size: 14px; background: #1d1d1d; border: 1px solid #414141; border-radius: 6px; outline: 0; }.store-name-input input::placeholder { color: #888; }.store-name-input input:focus { border-color: #777; box-shadow: 0 0 0 2px rgb(255 255 255 / 8%); }.store-name-panel-enter-active, .store-name-panel-leave-active { transition: opacity .16s ease, transform .16s ease; }.store-name-panel-enter-from, .store-name-panel-leave-to { opacity: 0; transform: translateY(6px) scale(.97); }.account { display: flex; align-items: center; gap: 7px; min-height: 43px; padding: 8px 6px 0; color: #ddd; font-size: 15px; white-space: nowrap; }.account__avatar { display: grid; width: 26px; height: 24px; color: white; font-size: 8px; font-weight: 800; background: #8659eb; border-radius: 7px; place-items: center; }.account__badge { padding: 3px 8px; color: #aaa; font-size: 12px; background: #333; border-radius: 10px; }.account__bell { margin-left: auto; }
.sidebar__navigation :deep(.nav-item:disabled) { color: #777; cursor: not-allowed; }
.sidebar__navigation :deep(.nav-item:disabled:hover) { color: #777; background: transparent; }
.order-links :deep(.nav-item:disabled), .order-links :deep(.nav-item:disabled:hover) { color: #bebebe; cursor: default; }
.product-links {
  margin: 2px 0 6px 18px !important;
}

.product-links :deep(.nav-item) {
  min-height: 34px;
  font-size: 14px;
}

.product-links :deep(.nav-item svg) {
  display: none;
}

.product-entry {
  margin-top: 4px !important;
}
</style>
