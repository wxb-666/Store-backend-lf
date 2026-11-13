<template>
  <aside class="sidebar">
    <div class="logo-area">
      <div class="logo-icon">🛍️</div>
    </div>

    <div class="search-box">
      <span>🔍 搜索</span>
      <span class="shortcut">Ctrl K</span>
    </div>

    <nav class="nav-menu">
      <div class="menu-group">
        <a href="#" class="menu-item active"><span>🏠</span> 主页</a>
        <a href="#" class="menu-item"><span>📦</span> 订单</a>
        <a href="#" class="menu-item"><span>🏷️</span> 产品</a>
        <a href="#" class="menu-item"><span>👥</span> 客户</a>
        <a href="#" class="menu-item"><span>📈</span> 增长</a>
        <a href="#" class="menu-item"><span>🏷️</span> 折扣</a>
        <a href="#" class="menu-item"><span>📝</span> 内容</a>
        <a href="#" class="menu-item"><span>🎯</span> 市场</a>
        <a href="#" class="menu-item"><span>💵</span> 财务</a>
        <a href="#" class="menu-item"><span>📊</span> 分析</a>
      </div>

      <div class="menu-group">
        <div class="group-title">销售渠道 ></div>
        <a href="#" class="menu-item"><span>🏪</span> 在线商店</a>
        <a href="#" class="menu-item"><span>🤖</span> 智能体</a>
      </div>

      <div class="menu-group">
        <div class="group-title">应用 ></div>
        <a href="#" class="menu-item"><span>➕</span> 添加</a>
      </div>
    </nav>

    <div class="sidebar-footer">
      <a href="#" class="menu-item"><span>⚙️</span> 设置</a>
      <div class="user-profile">
        <span class="avatar">SU</span>
        <span class="name">support</span>
        <span class="badge">dev</span>
        <span class="bell">🔔</span>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 240px;
  background-color: #1a1a1a;
  color: #a3a3a3;
  display: flex;
  flex-direction: column;
  padding: 12px;
  height: 100vh;
}

.logo-area {
  padding: 8px 12px 16px 12px;
  font-size: 24px;
}

.search-box {
  background: #2d2d2d;
  border-radius: 8px;
  padding: 8px 12px;
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  margin-bottom: 16px;
  cursor: pointer;
}

.shortcut {
  font-size: 12px;
  color: #737373;
}

.nav-menu {
  flex: 1;
  overflow-y: auto;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 12px;
  color: #e5e5e5;
  text-decoration: none;
  font-size: 14px;
  border-radius: 8px;
  margin-bottom: 2px;
}

.menu-item:hover, .menu-item.active {
  background-color: #333333;
}

.group-title {
  padding: 12px 12px 4px 12px;
  font-size: 12px;
  color: #737373;
}

.sidebar-footer {
  border-top: 1px solid #333;
  padding-top: 12px;
}

.user-profile {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  gap: 8px;
  font-size: 14px;
  color: #e5e5e5;
  margin-top: 8px;
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
  font-size: 12px;
  font-weight: bold;
}

.badge {
  background: #333;
  color: #a3a3a3;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 10px;
}

.bell {
  margin-left: auto;
  cursor: pointer;
}
</style>