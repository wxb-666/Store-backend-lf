<template>
  <aside class="sidebar">
    <div class="logo-area">
      <!-- 用 SVG 画一个极其标准的品牌图标 -->
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#a1a1aa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <path d="M16 10a4 4 0 0 1-8 0"></path>
      </svg>
    </div>

    <div class="search-box">
      <div class="search-left">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        搜索
      </div>
      <span class="shortcut">Ctrl K</span>
    </div>

    <nav class="nav-menu">
      <div class="menu-group">
        <a href="#" class="menu-item active">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          主页
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
          订单
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>
          产品
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          客户
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
          增长
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>
          折扣
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          内容
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>
          市场
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg>
          财务
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
          分析
        </a>
      </div>

      <div class="menu-group">
        <div class="group-title">销售渠道 <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></div>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          在线商店
        </a>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8" y2="16"></line><line x1="16" y1="16" x2="16" y2="16"></line></svg>
          智能体
        </a>
      </div>

      <div class="menu-group">
        <div class="group-title">应用 <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg></div>
        <a href="#" class="menu-item">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          添加
        </a>
      </div>
    </nav>

    <div class="sidebar-footer">
      <a href="#" class="menu-item">
        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
        设置
      </a>
      <div class="user-profile">
        <span class="avatar">SU</span>
        <span class="name">support</span>
        <span class="badge">dev</span>
        <svg class="bell" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #1a1a1a;
  color: #a1a1aa;
  display: flex;
  flex-direction: column;
  padding: 12px;
  height: 100vh;
  flex-shrink: 0;
}

.logo-area {
  padding: 8px 12px 16px 12px;
  display: flex;
  align-items: center;
}

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
  color: #a1a1aa;
}

.search-left {
  display: flex;
  align-items: center;
  gap: 8px;
}

.shortcut {
  font-size: 11px;
  color: #71717a;
}

.nav-menu {
  flex: 1;
  overflow-y: auto;
  /* 隐藏滚动条 */
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
  margin-bottom: 2px;
  transition: all 0.2s;
}

.menu-item .icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
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

.group-title {
  padding: 16px 12px 8px 12px;
  font-size: 12px;
  color: #71717a;
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
}

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