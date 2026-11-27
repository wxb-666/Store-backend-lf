
<template>
  <form class="products-toolbar" @submit.prevent="submitSearch">
    <!-- Product tag -->
    <select v-model="tag" class="filter-control tag-select" aria-label="Product tag">
      <option value="">Product tag</option>
      <option value="New in">New in</option>
      <option value="Christmas">Christmas</option>
      <option value="Sale">Sale</option>
    </select>

    <!-- Minimum price -->
    <label class="filter-control price-control">
      <span class="currency-symbol">$</span>
      <input
        v-model="minPrice"
        type="number"
        min="0"
        step="0.01"
        placeholder="Minimum"
        aria-label="Minimum price"
      />
    </label>

    <!-- Maximum price -->
    <label class="filter-control price-control">
      <span class="currency-symbol">$</span>
      <input
        v-model="maxPrice"
        type="number"
        min="0"
        step="0.01"
        placeholder="Maximum"
        aria-label="Maximum price"
      />
    </label>

    <!-- Product label: actually used for domain filtering -->
    <input
      v-model="domain"
      class="filter-control domain-control"
      type="text"
      placeholder="Product label"
      aria-label="Product label"
    />

    <!-- Keyword search -->
    <div class="filter-control search-control">
      <AppIcon name="search" :size="18" />
      <input
        v-model="draftQuery"
        type="search"
        placeholder="Please enter product name, spu, slug, etc"
        aria-label="Product keyword search"
      />
      <button type="submit">Search</button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import AppIcon from '../ui/AppIcon.vue'

const tag = defineModel<string>('tag', { required: true })
const minPrice = defineModel<string>('minPrice', { required: true })
const maxPrice = defineModel<string>('maxPrice', { required: true })
const domain = defineModel<string>('domain', { required: true })
const query = defineModel<string>('query', { required: true })

const draftQuery = ref(query.value)

watch(query, (value) => {
  draftQuery.value = value
})

function submitSearch() {
  query.value = draftQuery.value.trim()
}
</script>

<style scoped>
.products-toolbar {
  display: grid;
  grid-template-columns:
    minmax(145px, 1.05fr)
    minmax(105px, 0.55fr)
    minmax(105px, 0.55fr)
    minmax(150px, 1fr)
    minmax(300px, 2.5fr);
  align-items: center;
  gap: 10px;
  padding: 16px 0;
}

.filter-control {
  display: flex;
  align-items: center;
  width: 100%;
  min-width: 0;
  height: 38px;
  padding: 0 11px;
  color: #555;
  font-size: 14px;
  background: #fff;
  border: 1px solid #d8d8d8;
  border-radius: 5px;
  box-shadow: 0 1px 2px rgb(0 0 0 / 3%);
}

.filter-control:focus-within {
  border-color: #888;
  box-shadow: 0 0 0 2px rgb(0 0 0 / 6%);
  outline: none;
}

.tag-select {
  cursor: pointer;
}

.price-control {
  gap: 4px;
}

.currency-symbol {
  flex: 0 0 auto;
  color: #888;
}

.filter-control input {
  width: 100%;
  min-width: 0;
  height: 100%;
  padding: 0;
  color: #303030;
  font: inherit;
  background: transparent;
  border: 0;
  outline: 0;
}

.filter-control input::placeholder {
  color: #999;
  opacity: 1;
}

.price-control input {
  appearance: auto;
}

.domain-control {
  outline: none;
}

.search-control {
  gap: 9px;
  padding-right: 4px;
}

.search-control > svg {
  flex: 0 0 auto;
  color: #888;
}

.search-control input {
  flex: 1;
}

.search-control button {
  flex: 0 0 auto;
  height: 32px;
  padding: 0 16px;
  color: #fff;
  font-size: 14px;
  background: #000;
  border: 1px solid #000;
  border-radius: 4px;
  cursor: pointer;
}

.search-control button:hover {
  background: #252525;
}

@media (max-width: 1100px) {
  .products-toolbar {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .search-control {
    grid-column: 1 / -1;
  }
}

@media (max-width: 650px) {
  .products-toolbar {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .search-control {
    grid-column: 1 / -1;
  }
}
</style>