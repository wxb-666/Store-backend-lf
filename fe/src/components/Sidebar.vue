<template>
  <aside
    class="sidebar"
    :style="{ width: isCollapsed ? '64px' : '240px' }"
  >
    <!-- 顶部区域 -->
    <div class="sidebar-top">
      <div class="logo-area" v-if="!isCollapsed">
        <div class="logo-icon">🛍️</div>
      </div>

      <!-- 折叠按钮 -->
      <div class="toggle-wrapper group relative">
        <button class="toggle-btn" @click="toggleCollapse">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="9" y1="3" x2="9" y2="21"></line>
          </svg>
        </button>
        <!-- Tooltip 提示 -->
        <div class="tooltip">
          {{ isCollapsed ? '展开导航' : '折叠导航' }} <span class="kbd">CTRL</span> <span class="kbd">B</span>
        </div>
      </div>
    </div>

    <!-- 搜索框 (收起时只显示放大镜) -->
    <div class="search-box" :class="{ 'just-icon': isCollapsed }">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <template v-if="!isCollapsed">
        <span class="search-text">搜索</span>
        <span class="shortcut">Ctrl K</span>
      </template>
    </div>

    <!-- 导航菜单 -->
    <nav class="nav-menu">
      <div class="menu-group">
        <a href="#" class="menu-item" :class="{ active: true, 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          <span v-if="!isCollapsed">主页</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
          <span v-if="!isCollapsed">订单</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>
          <span v-if="!isCollapsed">产品</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          <span v-if="!isCollapsed">客户</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
          <span v-if="!isCollapsed">增长</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>
          <span v-if="!isCollapsed">折扣</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          <span v-if="!isCollapsed">内容</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>
          <span v-if="!isCollapsed">市场</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg>
          <span v-if="!isCollapsed">财务</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
          <span v-if="!isCollapsed">分析</span>
        </a>
      </div>

      <div class="menu-group">
        <div class="group-title" v-if="!isCollapsed">销售渠道</div>
        <!-- 收起时，用一条分割线代替分类标题 -->
        <div v-else class="divider-line"></div>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          <span v-if="!isCollapsed">在线商店</span>
        </a>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8" y2="16"></line><line x1="16" y1="16" x2="16" y2="16"></line></svg>
          <span v-if="!isCollapsed">智能体</span>
        </a>
      </div>

      <div class="menu-group">
        <div class="group-title" v-if="!isCollapsed">应用</div>
        <div v-else class="divider-line"></div>
        <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span v-if="!isCollapsed">添加</span>
        </a>
      </div>
    </nav>

    <div class="sidebar-footer">
      <a href="#" class="menu-item" :class="{ 'center-icon': isCollapsed }">
        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
        <span v-if="!isCollapsed">设置</span>
      </a>

      <!-- 底部个人信息 (如果是收起状态，只显示头像) -->
      <div class="user-profile" :class="{ 'center-icon': isCollapsed }">
        <span class="avatar">SU</span>
        <template v-if="!isCollapsed">
          <span class="name">support</span>
          <span class="badge">dev</span>
          <svg class="bell" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
        </template>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
// 使用 v-model 进行数据双向绑定
const props = defineProps<{ collapsed: boolean }>()
const emit = defineEmits(['update:collapsed'])

const toggleCollapse = () => {
  emit('update:collapsed', !props.collapsed)
}

// 方便模板中调用
import { computed } from 'vue'
const isCollapsed = computed(() => props.collapsed)
</script>

<style scoped>
/* 外层容器，保留背景，增加宽度过渡 */
.sidebar {
  background-color: #1a1a1a;
  color: #a1a1aa;
  display: flex;
  flex-direction: column;
  padding: 12px;
  height: 100vh;
  flex-shrink: 0;
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden; /* 防止文字换行折行 */
}

/* 顶部 Logo 和折叠按钮 */
.sidebar-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  padding: 4px 0;
}

.logo-area {
  display: flex;
  align-items: center;
}

.logo-icon {
  font-size: 22px;
}

/* 折叠按钮与悬浮提示 */
.toggle-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.toggle-btn {
  background: transparent;
  border: none;
  color: #a1a1aa;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  border-radius: 8px;
  transition: all 0.2s;
}

.toggle-btn:hover {
  background: #27272a;
  color: #fff;
}

.tooltip {
  position: absolute;
  left: 100%;
  top: 50%;
  transform: translateY(-50%);
  margin-left: 12px;
  background: #ffffff;
  color: #111;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transition: opacity 0.2s, visibility 0.2s;
  z-index: 50;
}

/* 鼠标悬停时显示提示 */
.group:hover .tooltip {
  opacity: 1;
  visibility: visible;
}

/* Tooltip 里的快捷键按键样式 */
.kbd {
  background: #f4f4f5;
  border: 1px solid #e4e4e7;
  border-radius: 4px;
  padding: 2px 4px;
  font-family: monospace;
  font-size: 10px;
}

/* 搜索框 */
.search-box {
  background: #2c2c2e;
  border-radius: 8px;
  padding: 8px 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  margin-bottom: 16px;
  cursor: pointer;
  transition: all 0.3s;
}

/* 收起时的搜索框，居中显示图标 */
.search-box.just-icon {
  justify-content: center;
  padding: 8px;
  background: transparent;
}

.search-box.just-icon:hover {
  background: #2c2c2e;
}

.search-text {
  flex: 1;
  margin-left: 8px;
}

.shortcut {
  font-size: 11px;
  color: #71717a;
}

/* 导航菜单 */
.nav-menu {
  flex: 1;
  overflow-y: auto;
  scrollbar-width: none;
}
.nav-menu::-webkit-scrollbar {
  display: none;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 12px;
  color: #a1a1aa;
  text-decoration: none;
  font-size: 13px;
  border-radius: 8px;
  margin-bottom: 4px;
  transition: all 0.2s;
  white-space: nowrap;
}

.menu-item .icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}

/* 收起时图标居中 */
.menu-item.center-icon {
  justify-content: center;
  padding: 10px;
}

.menu-item:hover {
  background-color: #27272a;
  color: #e4e4e7;
}

.menu-item.active {
  background-color: #27272a;
  color: #ffffff;
  border: 1px solid #3f3f46;
}

/* 分组标题和收起时的分割线 */
.group-title {
  padding: 16px 12px 8px 12px;
  font-size: 11px;
  color: #71717a;
}

.divider-line {
  height: 1px;
  background: #27272a;
  margin: 12px 8px;
}

/* 底部区域 */
.sidebar-footer {
  border-top: 1px solid #27272a;
  padding-top: 12px;
  margin-top: 12px;
}

.user-profile {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  gap: 8px;
  font-size: 13px;
  color: #e4e4e7;
  margin-top: 4px;
}

/* 收起时个人资料居中 */
.user-profile.center-icon {
  justify-content: center;
  padding: 8px 0;
}

.avatar {
  background: #8b5cf6;
  color: white;
  width: 24px;
  height: 24px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: bold;
  flex-shrink: 0;
}

.badge {
  background: #27272a;
  color: #a1a1aa;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 10px;
}

.bell {
  margin-left: auto;
  cursor: pointer;
  color: #a1a1aa;
}
</style>