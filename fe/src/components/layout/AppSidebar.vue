<template>
  <aside class="sidebar" :class="{ 'is-collapsed': collapsed }">
    <div class="sidebar__top">
      <div class="shopify-mark" aria-label="Shopify">S</div>
      <button class="icon-button sidebar-toggle" :title="collapsed ? '展开导航' : '折叠导航'" type="button" @click="collapsed = !collapsed"><AppIcon name="panel" :size="20" /></button>
    </div>
    <button class="search-trigger" type="button" aria-label="搜索"><AppIcon name="search" :size="19" /><span v-if="!collapsed">搜索</span><kbd v-if="!collapsed">Ctrl K</kbd></button>
    <nav class="sidebar__navigation" aria-label="主导航">
      <SidebarGroup :items="mainNavigation" :collapsed="collapsed" :active-item="activeItem" @select="activeItem = $event" />
      <SidebarGroup title="销售渠道" :items="salesChannels" :collapsed="collapsed" :active-item="activeItem" @select="activeItem = $event" />
      <SidebarGroup title="应用" :items="apps" :collapsed="collapsed" :active-item="activeItem" @select="activeItem = $event" />
    </nav>
    <div class="sidebar__footer">
      <button class="nav-item" :class="{ 'is-icon-only': collapsed }" type="button" title="设置"><AppIcon name="settings" /><span v-if="!collapsed">设置</span></button>
      <div class="account" :class="{ 'is-icon-only': collapsed }"><span class="account__avatar">SUP</span><template v-if="!collapsed"><strong>support</strong><span class="account__badge">dev</span><button class="icon-button account__bell" type="button" aria-label="通知"><AppIcon name="bell" :size="19" /></button></template></div>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import AppIcon, { type IconName } from '../ui/AppIcon.vue'
import SidebarGroup from './SidebarGroup.vue'
const collapsed = defineModel<boolean>('collapsed', { required: true })
const activeItem = ref('主页')
type NavigationItem = { label: string; icon: IconName }
const mainNavigation: NavigationItem[] = [{ label: '主页', icon: 'home' }, { label: '订单', icon: 'orders' }, { label: '产品', icon: 'tag' }, { label: '客户', icon: 'customers' }, { label: '增长', icon: 'growth' }, { label: '折扣', icon: 'tag' }, { label: '内容', icon: 'content' }, { label: '市场', icon: 'market' }, { label: '财务', icon: 'finance' }, { label: '分析', icon: 'analytics' }]
const salesChannels: NavigationItem[] = [{ label: '在线商店', icon: 'store' }, { label: '智能体', icon: 'bot' }]
const apps: NavigationItem[] = [{ label: '添加', icon: 'plus' }]
</script>

<style scoped>
.sidebar { display: flex; flex: 0 0 280px; flex-direction: column; min-width: 0; height: 100%; padding: 20px 16px 16px; color: #b8b8b8; background: #0c0c0c; transition: flex-basis .24s ease; }
.sidebar.is-collapsed { flex-basis: 70px; padding-inline: 10px; }.sidebar__top { display: flex; align-items: center; justify-content: space-between; height: 34px; margin: 0 4px 24px; }.shopify-mark { display: grid; width: 28px; height: 31px; color: white; font-size: 18px; font-weight: 800; line-height: 1; place-items: center; background: #96bf48; border-radius: 4px 4px 8px 8px; transform: rotate(-8deg); }.icon-button { display: inline-grid; padding: 6px; color: inherit; background: transparent; border: 0; border-radius: 7px; place-items: center; }.icon-button:hover { color: white; background: #2a2a2a; }.sidebar-toggle { margin-left: auto; }
.search-trigger { display: flex; align-items: center; width: 100%; height: 36px; gap: 9px; padding: 0 11px; margin-bottom: 18px; color: #bebebe; text-align: left; background: #303030; border: 0; border-radius: 12px; }.search-trigger span { flex: 1; font-size: 14px; }.search-trigger kbd { color: #bbb; font: inherit; font-size: 13px; }.is-collapsed .search-trigger { justify-content: center; padding: 0; background: transparent; }.is-collapsed .search-trigger:hover { background: #292929; }
.sidebar__navigation { flex: 1; min-height: 0; overflow-y: auto; scrollbar-width: none; }.sidebar__navigation::-webkit-scrollbar { display: none; }.sidebar__navigation :deep(.nav-group + .nav-group) { margin-top: 18px; }.sidebar__navigation :deep(.nav-group__title) { padding: 5px 7px 10px; margin: 0; color: #999; font-size: 13px; }.sidebar__navigation :deep(.nav-group__title::after) { margin-left: 5px; content: '›'; }.sidebar__navigation :deep(.nav-group__divider) { height: 1px; margin: 13px 7px; background: #2b2b2b; }
.sidebar__navigation :deep(.nav-item), .nav-item { display: flex; align-items: center; width: 100%; gap: 11px; min-height: 38px; padding: 0 9px; color: #bebebe; font-size: 15px; text-align: left; background: transparent; border: 0; border-radius: 12px; }.sidebar__navigation :deep(.nav-item:hover), .nav-item:hover { color: #fff; background: #252525; }.sidebar__navigation :deep(.nav-item.is-active) { color: #fff; background: linear-gradient(180deg, #353535, #2d2d2d); box-shadow: inset 0 1px #4a4a4a; }.sidebar__navigation :deep(.nav-item.is-icon-only), .nav-item.is-icon-only { justify-content: center; padding: 0; }
.sidebar__footer { padding-top: 12px; border-top: 1px solid #292929; }.account { display: flex; align-items: center; gap: 7px; min-height: 43px; padding: 8px 6px 0; color: #ddd; font-size: 15px; white-space: nowrap; }.account.is-icon-only { justify-content: center; padding-inline: 0; }.account__avatar { display: grid; width: 26px; height: 24px; color: white; font-size: 8px; font-weight: 800; background: #8659eb; border-radius: 7px; place-items: center; }.account__badge { padding: 3px 8px; color: #aaa; font-size: 12px; background: #333; border-radius: 10px; }.account__bell { margin-left: auto; }
</style>
