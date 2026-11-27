
<template>
  <section class="products-view">
    <header class="products-header">
      <h1>Product list</h1>

      <div class="header-actions">
        <button class="secondary-button" type="button">Import</button>
        <button class="secondary-button" type="button">Export</button>
        <button class="primary-button" type="button">Import Shopify products</button>
        <button class="primary-button" type="button">
          <AppIcon name="plus" :size="16" />
          Add product
        </button>
      </div>
    </header>

    <div class="products-content">
      <div class="products-panel">
        <nav class="product-tabs" aria-label="Product status">
          <button
            v-for="tab in tabs"
            :key="tab.value"
            type="button"
            :class="{ active: activeTab === tab.value }"
            @click="activeTab = tab.value"
          >
            {{ tab.label }}
          </button>
        </nav>

        <ProductsToolbar
          v-model:tag="tag"
          v-model:min-price="minPrice"
          v-model:max-price="maxPrice"
          v-model:domain="domain"
          v-model:query="query"
        />

        <ProductsTable
          :active-tab="activeTab"
          :tag="tag"
          :min-price="minPrice"
          :max-price="maxPrice"
          :domain="domain"
          :query="query"
        />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import AppIcon from '../components/ui/AppIcon.vue'
import ProductsToolbar from '../components/products/ProductsToolbar.vue'
import ProductsTable from '../components/products/ProductsTable.vue'

type ProductTab = 'all' | 'on-sale' | 'removed'

const tabs: { label: string; value: ProductTab }[] = [
  { label: 'All', value: 'all' },
  { label: 'On sell', value: 'on-sale' },
  { label: 'Has been removed', value: 'removed' },
]

const activeTab = ref<ProductTab>('all')

const tag = ref('')
const minPrice = ref('')
const maxPrice = ref('')
const domain = ref('')
const query = ref('')
</script>

<style scoped>
.products-view {
  display: flex;
  flex: 1;
  flex-direction: column;
  min-width: 0;
  overflow: hidden;
  background: #f6f6f7;
}

.products-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 80px;
  gap: 20px;
  padding: 16px 28px;
}

.products-header h1 {
  margin: 0;
  color: #202020;
  font-size: 21px;
  font-weight: 600;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.header-actions button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 38px;
  gap: 6px;
  padding: 0 16px;
  border-radius: 6px;
  font-size: 14px;
  white-space: nowrap;
}

.secondary-button {
  color: #303030;
  background: #fff;
  border: 1px solid #dedede;
  box-shadow: 0 1px 2px rgb(0 0 0 / 4%);
}

.primary-button {
  color: #fff;
  background: #f58a32;
  border: 1px solid #f58a32;
}

.primary-button:hover {
  background: #e97924;
}

.products-content {
  flex: 1;
  min-height: 0;
  padding: 0 24px 24px;
  overflow: auto;
}

.products-panel {
  min-height: 100%;
  padding: 0 20px 20px;
  background: #fff;
  border: 1px solid #e8e8e8;
  border-radius: 10px;
  box-shadow: 0 1px 3px rgb(0 0 0 / 4%);
}

.product-tabs {
  display: flex;
  align-items: center;
  height: 54px;
  gap: 34px;
  padding: 0 12px;
  border-bottom: 1px solid #e8e8e8;
}

.product-tabs button {
  position: relative;
  height: 100%;
  padding: 0 5px;
  color: #555;
  font-size: 14px;
  background: transparent;
  border: 0;
}

.product-tabs button.active {
  color: #e97827;
  font-weight: 600;
}

.product-tabs button.active::after {
  position: absolute;
  right: 0;
  bottom: -1px;
  left: 0;
  height: 2px;
  background: #ed8737;
  content: '';
}

@media (max-width: 900px) {
  .products-header {
    align-items: flex-start;
    flex-direction: column;
    padding: 18px;
  }

  .header-actions {
    flex-wrap: wrap;
  }

  .products-content {
    padding-inline: 12px;
  }
}

@media (max-width: 600px) {
  .products-panel {
    padding-inline: 12px;
  }

  .header-actions button {
    padding-inline: 10px;
  }
}
</style>
