
<template>
    <section class="orders-view">
        <!-- 页面头部 -->
        <header class="orders-header">
            <h1>
                <AppIcon name="orders" :size="23" />
                Orders
            </h1>

            <div>
                <button class="export-button" type="button">
                    Export
                </button>
            </div>
        </header>

        <!-- 页面主体 -->
        <div class="orders-content">
            <OrdersToolbar
                v-model:query="query"
                v-model:payment-method="paymentMethod"
                v-model:domain="domain"
            />

            <OrdersTable
                :query="query"
                :payment-method="paymentMethod"
                :domain="domain"
            />
        </div>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import AppIcon from '../components/ui/AppIcon.vue'
import OrdersTable from '../components/orders/OrdersTable.vue'
import OrdersToolbar from '../components/orders/OrdersToolbar.vue'

// 定义组件名称
defineOptions({ name: 'OrdersView' })

// 定义响应式数据
const query = ref('')
const paymentMethod = ref('')
const domain = ref('')
</script>

<style scoped>
/* 页面整体布局 */
.orders-view {
  position: relative;
  display: flex;
  flex: 1;
  flex-direction: column;
  min-width: 0;
  overflow: hidden;
}

/* 页面头部 */
.orders-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 80px;
  padding: 18px 32px;
  border-bottom: 1px solid #f1f1f1;
}

.orders-header h1 {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 0;
  color: #161616;
  font-size: 20px;
  font-weight: 600;
}

.orders-header div {
  display: flex;
  gap: 8px;
}

.orders-header button {
  min-height: 36px;
  padding: 0 16px;
  border-radius: 19px;
}

/* 导出按钮 */
.export-button {
  color: #303030;
  background: white;
  border: 1px solid #e1e1e1;
  box-shadow: 0 2px 5px rgb(0 0 0 / 4%);
}

/* 页面主体 */
.orders-content {
  flex: 1;
  min-height: 0;
  padding: 10px 20px 100px;
  overflow: auto;
}

.orders-content > :first-child {
  margin-bottom: 14px;
}

/* 输入区域 */
.composer-area {
  position: absolute;
  right: 0;
  bottom: 18px;
  left: 0;
  display: flex;
  justify-content: center;
  pointer-events: none;
}

.composer-area :deep(.composer) {
  pointer-events: auto;
}

/* 移动端适配 */
@media (max-width: 780px) {
  .orders-header {
    min-height: 64px;
    padding-inline: 18px;
  }

  .orders-content {
    padding-inline: 12px;
  }

  .export-button {
    display: none;
  }
}
</style>
