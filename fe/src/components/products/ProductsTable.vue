
<template>
  <div class="products-table-wrap">
    <table class="products-table">
      <thead>
        <tr>
          <th class="checkbox-column">
            <input v-model="allSelected" type="checkbox" aria-label="Select all products" />
          </th>
          <th class="image-column">Product image</th>
          <th>Product name</th>
          <th>Selling price</th>
          <th>Stock</th>
          <th>Categories</th>
          <th>Operation</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="product in paginatedProducts" :key="product.id">
          <td>
            <input
              v-model="selectedIds"
              type="checkbox"
              :value="product.id"
              :aria-label="`Select ${product.name}`"
            />
          </td>

          <td>
            <div class="product-image" :class="product.imageClass">
              <span>{{ product.imageText }}</span>
            </div>
          </td>

          <td class="product-name-cell">
            <strong>{{ product.name }}</strong>
            <small v-if="product.status === 'removed'" class="removed-status">
              ○ Removed
            </small>
          </td>

          <td class="price-cell">
            {{ formatPrice(product.price) }}
          </td>

          <td class="stock-cell">
            {{ product.stock }}
          </td>

          <td>
            <div class="tag-list">
              <span
                v-for="item in product.tags"
                :key="item"
                class="product-tag"
              >
                {{ item }}
              </span>
              <span v-if="product.tags.length === 0">—</span>
            </div>
          </td>

          <td>
            <div class="operation-list">
              <button type="button">Copy</button>
              <button type="button">Preview</button>
              <button type="button">Top</button>
            </div>
          </td>
        </tr>

        <tr v-if="paginatedProducts.length === 0">
          <td colspan="7" class="empty-cell">
            No products found.
          </td>
        </tr>
      </tbody>
    </table>

    <footer class="pagination">
      <span>{{ filteredProducts.length }} products</span>

      <div class="page-controls">
        <button
          type="button"
          :disabled="page <= 1"
          aria-label="Previous page"
          @click="page--"
        >
          ‹
        </button>

        <span>Page {{ page }} of {{ totalPages }}</span>

        <button
          type="button"
          :disabled="page >= totalPages"
          aria-label="Next page"
          @click="page++"
        >
          ›
        </button>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'

type ProductStatus = 'on-sale' | 'removed'

interface Product {
  id: number
  name: string
  spu: string
  slug: string
  domain: string
  price: number
  stock: string
  tags: string[]
  status: ProductStatus
  imageText: string
  imageClass: string
}

const props = defineProps<{
  activeTab: 'all' | 'on-sale' | 'removed'
  tag: string
  minPrice: string
  maxPrice: string
  domain: string
  query: string
}>()

// 模拟商品数据：后续接入 API 时替换这部分数据
const products = ref<Product[]>([
  {
    id: 1,
    name: 'Fried Hair Cat Print Tote Bag',
    spu: 'SPU-10001',
    slug: 'fried-hair-cat-print-tote-bag',
    domain: 'store-a.com',
    price: 9.99,
    stock: 'No use inventory',
    tags: ['New in'],
    status: 'removed',
    imageText: '✦',
    imageClass: 'image-cream',
  },
  {
    id: 2,
    name: "Women's Casual Printed Hooded Sweatshirt",
    spu: 'SPU-10002',
    slug: 'womens-casual-printed-hooded-sweatshirt',
    domain: 'store-a.com',
    price: 29.99,
    stock: 'No use inventory',
    tags: ['New in', 'Christmas'],
    status: 'on-sale',
    imageText: '✿',
    imageClass: 'image-pink',
  },
  {
    id: 3,
    name: "Women's Christmas Print T-Shirt",
    spu: 'SPU-10003',
    slug: 'womens-christmas-print-t-shirt',
    domain: 'store-b.com',
    price: 25.99,
    stock: 'No use inventory',
    tags: ['New in', 'Christmas'],
    status: 'on-sale',
    imageText: '✧',
    imageClass: 'image-green',
  },
  {
    id: 4,
    name: "Women's Christmas Print T-Shirt",
    spu: 'SPU-10004',
    slug: 'womens-christmas-print-t-shirt-red',
    domain: 'store-a.com',
    price: 25.99,
    stock: 'No use inventory',
    tags: ['New in', 'Christmas'],
    status: 'on-sale',
    imageText: '✿',
    imageClass: 'image-red',
  },
  {
    id: 5,
    name: "Women's Christmas Print Casual Sweatshirt",
    spu: 'SPU-10005',
    slug: 'womens-christmas-print-casual-sweatshirt',
    domain: 'store-b.com',
    price: 29.99,
    stock: 'No use inventory',
    tags: ['Christmas'],
    status: 'on-sale',
    imageText: '✦',
    imageClass: 'image-beige',
  },
  {
    id: 6,
    name: "Women's Winter Christmas Print Cardigan",
    spu: 'SPU-10006',
    slug: 'womens-winter-christmas-print-cardigan',
    domain: 'store-a.com',
    price: 42.99,
    stock: 'No use inventory',
    tags: ['New in', 'Christmas'],
    status: 'on-sale',
    imageText: '✧',
    imageClass: 'image-blue',
  },
  {
    id: 7,
    name: "Women's Christmas Print T-Shirt",
    spu: 'SPU-10007',
    slug: 'womens-christmas-print-t-shirt-green',
    domain: 'store-c.com',
    price: 25.99,
    stock: 'No use inventory',
    tags: ['Sale'],
    status: 'on-sale',
    imageText: '✿',
    imageClass: 'image-red',
  },
  {
    id: 8,
    name: 'Classic Printed Canvas Tote Bag',
    spu: 'SPU-10008',
    slug: 'classic-printed-canvas-tote-bag',
    domain: 'store-b.com',
    price: 15.99,
    stock: 'No use inventory',
    tags: ['Sale'],
    status: 'on-sale',
    imageText: '✦',
    imageClass: 'image-cream',
  },
])

const selectedIds = ref<number[]>([])
const page = ref(1)
const pageSize = 8

const filteredProducts = computed(() => {
  const keyword = props.query.trim().toLowerCase()
  const domainKeyword = props.domain.trim().toLowerCase()
  const min = props.minPrice === '' ? null : Number(props.minPrice)
  const max = props.maxPrice === '' ? null : Number(props.maxPrice)

  return products.value.filter((product) => {
    if (props.activeTab !== 'all' && product.status !== props.activeTab) {
      return false
    }

    if (props.tag && !product.tags.includes(props.tag)) {
      return false
    }

    if (min !== null && product.price < min) {
      return false
    }

    if (max !== null && product.price > max) {
      return false
    }

    if (domainKeyword && !product.domain.toLowerCase().includes(domainKeyword)) {
      return false
    }

    if (keyword) {
      const searchableText = [
        product.name,
        product.spu,
        product.slug,
      ].join(' ').toLowerCase()

      if (!searchableText.includes(keyword)) {
        return false
      }
    }

    return true
  })
})

const totalPages = computed(() => {
  return Math.max(1, Math.ceil(filteredProducts.value.length / pageSize))
})

const paginatedProducts = computed(() => {
  const start = (page.value - 1) * pageSize
  return filteredProducts.value.slice(start, start + pageSize)
})

const allSelected = computed({
  get: () =>
    paginatedProducts.value.length > 0 &&
    paginatedProducts.value.every((product) => selectedIds.value.includes(product.id)),
  set: (checked: boolean) => {
    const currentPageIds = paginatedProducts.value.map((product) => product.id)

    selectedIds.value = checked
      ? [...new Set([...selectedIds.value, ...currentPageIds])]
      : selectedIds.value.filter((id) => !currentPageIds.includes(id))
  },
})

watch(
  () => [
    props.activeTab,
    props.tag,
    props.minPrice,
    props.maxPrice,
    props.domain,
    props.query,
  ],
  () => {
    page.value = 1
    selectedIds.value = []
  },
)

watch(totalPages, (value) => {
  if (page.value > value) page.value = value
})

function formatPrice(price: number) {
  return `$${price.toFixed(2)}`
}
</script>

<style scoped>
.products-table-wrap {
  min-width: 0;
  overflow: auto;
  background: #fff;
  border: 1px solid #ededed;
  border-radius: 7px;
}

.products-table {
  width: 100%;
  min-width: 900px;
  border-spacing: 0;
  border-collapse: separate;
  font-size: 14px;
}

.products-table th {
  height: 56px;
  padding: 0 15px;
  color: #303030;
  font-weight: 500;
  text-align: left;
  white-space: nowrap;
  background: #fafafa;
  border-bottom: 1px solid #e9e9e9;
}

.products-table td {
  height: 78px;
  padding: 9px 15px;
  color: #444;
  white-space: nowrap;
  border-bottom: 1px solid #ededed;
}

.products-table tbody tr:last-child td {
  border-bottom: 0;
}

.products-table tbody tr:hover {
  background: #fffaf4;
}

.checkbox-column {
  width: 48px;
}

.image-column {
  width: 100px;
}

.products-table input[type='checkbox'] {
  width: 17px;
  height: 17px;
  vertical-align: middle;
  accent-color: #f58a32;
  cursor: pointer;
}

.product-image {
  display: grid;
  width: 48px;
  height: 52px;
  overflow: hidden;
  color: #795f4c;
  font-size: 28px;
  border: 1px solid #e1e1e1;
  border-radius: 5px;
  place-items: center;
}

.image-cream { background: #f4eadb; }
.image-pink { background: #f5e3e7; }
.image-green { background: #e6eee2; }
.image-red { background: #eadbd8; }
.image-beige { background: #eee4d4; }
.image-blue { background: #e4eaf0; }

.product-name-cell {
  min-width: 250px;
}

.product-name-cell strong {
  display: block;
  max-width: 380px;
  overflow: hidden;
  color: #303030;
  font-weight: 500;
  text-overflow: ellipsis;
}

.removed-status {
  display: block;
  margin-top: 5px;
  color: #999;
  font-size: 12px;
}

.price-cell {
  min-width: 120px;
}

.stock-cell {
  min-width: 150px;
  color: #777 !important;
}

.tag-list {
  display: flex;
  align-items: center;
  gap: 5px;
}

.product-tag {
  display: inline-block;
  max-width: 120px;
  overflow: hidden;
  padding: 3px 8px;
  color: #2385a9;
  font-size: 12px;
  text-overflow: ellipsis;
  background: #e9f6fb;
  border: 1px solid #a9d9e9;
  border-radius: 4px;
}

.operation-list {
  display: flex;
  align-items: center;
  gap: 12px;
}

.operation-list button {
  padding: 0;
  color: #d98545;
  font-size: 13px;
  background: transparent;
  border: 0;
  cursor: pointer;
}

.operation-list button:hover {
  color: #b85c20;
  text-decoration: underline;
}

.empty-cell {
  height: 120px !important;
  color: #888 !important;
  text-align: center;
}

.pagination {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 56px;
  padding: 8px 14px;
  color: #666;
  font-size: 13px;
  border-top: 1px solid #ededed;
}

.page-controls {
  display: flex;
  align-items: center;
  gap: 14px;
}

.page-controls button {
  width: 28px;
  height: 28px;
  color: #444;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.page-controls button:disabled {
  color: #bbb;
  cursor: not-allowed;
}
</style>
