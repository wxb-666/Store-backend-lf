import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import OrdersView from '../views/OrdersView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/home' },
    { path: '/home', name: 'home', component: DashboardView },
    { path: '/all_orders', name: 'allOrders', component: OrdersView },
    // Keep unimplemented order sections safe until their pages are ready.
    { path: '/abandoned_orders', redirect: { name: 'allOrders' } },
    { path: '/risk_orders', redirect: { name: 'allOrders' } },
    { path: '/:pathMatch(.*)*', redirect: '/home' },
  ],
})

export default router
