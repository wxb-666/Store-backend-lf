<template>
  <div class="app-container">
    <!-- 左侧导航栏 -->
    <Sidebar />

    <!-- 右侧主内容区 -->
    <main class="main-content">
      <!-- 顶部状态栏 -->
      <header class="top-header">
        <div class="status">
          <span class="dot"></span> 可以销售
        </div>
        <div class="contact">有问题吗？ (844) 982-1186</div>
      </header>

      <!-- 滚动内容区 -->
      <div class="scroll-area">
        <!-- 欢迎及AI助手区域 -->
        <section class="welcome-section">
          <div class="store-preview-card">
             <!-- 模拟预览图 -->
            <div class="preview-image">
              <span class="privacy-tag">🔒 私密</span>
            </div>
            <button class="publish-btn">🚀 发布在线商店</button>
          </div>

          <h1 class="greeting-title">support 已初具规模<br/>接下来想做什么?</h1>

          <div class="ai-input-box">
            <input type="text" placeholder="我的商店可以上线了吗？" />
            <div class="ai-actions">
              <span>↺ 最近记录</span>
              <span>+</span>
              <span>🎤</span>
            </div>
          </div>
        </section>

        <!-- 底部卡片网格区域 -->
        <section class="task-grid">
          <!-- 卡片 1 -->
          <div class="task-card">
            <div class="card-icon payment-icon"></div>
            <h3>设置支付</h3>
            <p>激活 Shopify Payments，让客户可以通过卡、Shop Pay 等方式付款。</p>
            <button class="outline-btn">激活支付</button>
          </div>

          <!-- 卡片 2 -->
          <div class="task-card">
            <div class="card-icon domain-icon">
              <span class="domain-text">helpharbor.store</span>
            </div>
            <h3>为 support 获取匹配的域名</h3>
            <p>我们找到了与您的商店匹配的域名。选择您心仪的域名并即刻拥有。</p>
            <button class="outline-btn">选择域名</button>
          </div>

          <!-- 卡片 3 (彩色背景) -->
          <div class="task-card highlight-card">
            <div class="card-progress">↻ 已完成 8 项任务中的 4 项</div>
            <div class="illustration"></div>
            <h3>B2B 与 DTC，一站搞定</h3>
            <p>下一个任务：B2B 与 DTC，一站搞定</p>
            <button class="outline-btn">继续</button>
          </div>

          <!-- 卡片 4 (任务列表) -->
          <div class="task-card list-card">
            <div class="list-progress">○ 已完成 3 项任务中的 0 项</div>
            <h3>小改动，大提升。</h3>
            <p>Sidekick 发现了几个快速见效的方法，可将访客转化为客户。</p>
            <ul class="checklist">
              <li><span>○</span> 重写单板商品描述</li>
              <li><span>○</span> 替换首页测试文案</li>
              <li><span>○</span> 发布购物政策，澄清下单条件</li>
            </ul>
            <button class="outline-btn">开始</button>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
// 这里可以引入拆分的组件
import Sidebar from './components/Sidebar.vue'
</script>

<style scoped>
/* 基础布局 */
.app-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  background-color: #f3f4f6;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #333;
}

/* 右侧主内容 */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  border-radius: 12px 0 0 12px;
  margin: 8px 8px 8px 0; /* 留出左侧边栏的间隙 */
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  overflow: hidden;
}

.top-header {
  display: flex;
  justify-content: space-between;
  padding: 16px 24px;
  font-size: 14px;
  border-bottom: 1px solid #e5e7eb;
}

.status {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 500;
}

.status .dot {
  width: 8px;
  height: 8px;
  background-color: #10b981;
  border-radius: 50%;
}

.contact {
  color: #6b7280;
}

/* 滚动区域 */
.scroll-area {
  flex: 1;
  overflow-y: auto;
  padding: 40px;
  background-color: #f9fafb;
}

/* 欢迎区域 */
.welcome-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
  margin: 0 auto 40px auto;
}

.store-preview-card {
  width: 320px;
  background: white;
  border-radius: 12px;
  padding: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  margin-bottom: 24px;
}

.preview-image {
  height: 160px;
  background: linear-gradient(135deg, #d4e0eb, #a4bfd8);
  border-radius: 8px;
  position: relative;
}

.privacy-tag {
  position: absolute;
  bottom: 8px;
  left: 8px;
  background: rgba(255,255,255,0.8);
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.publish-btn {
  width: 100%;
  margin-top: 8px;
  padding: 10px;
  background: #1a1a1a;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
}

.greeting-title {
  font-size: 28px;
  text-align: center;
  margin-bottom: 24px;
  color: #111;
}

.ai-input-box {
  width: 100%;
  max-width: 600px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 24px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}

.ai-input-box input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 15px;
}

.ai-actions {
  display: flex;
  gap: 12px;
  color: #9ca3af;
  font-size: 14px;
}

/* 卡片网格布局 */
.task-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  max-width: 1100px;
  margin: 0 auto;
}

.task-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  border: 1px solid #e5e7eb;
}

.task-card h3 {
  font-size: 16px;
  margin: 16px 0 8px 0;
}

.task-card p {
  font-size: 14px;
  color: #6b7280;
  line-height: 1.5;
  flex: 1;
  margin-bottom: 16px;
}

.outline-btn {
  align-self: flex-start;
  padding: 8px 16px;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 20px;
  font-size: 14px;
  cursor: pointer;
  font-weight: 500;
}

.outline-btn:hover {
  background: #f3f4f6;
}

/* 各种卡片特殊样式 */
.card-icon {
  height: 100px;
  background: #f3f4f6;
  border-radius: 8px;
}

.highlight-card {
  background: #e0f2f1; /* 浅绿色底 */
  border-color: #b2dfdb;
}

.highlight-card .illustration {
  height: 100px;
  background: repeating-linear-gradient(45deg, #10b981, #10b981 10px, transparent 10px, transparent 20px);
  border-radius: 8px;
  opacity: 0.2;
}

.list-progress {
  font-size: 13px;
  color: #6b7280;
  margin-bottom: 8px;
}

.checklist {
  list-style: none;
  padding: 0;
  margin: 0 0 16px 0;
}

.checklist li {
  display: flex;
  gap: 8px;
  font-size: 14px;
  margin-bottom: 8px;
  color: #4b5563;
}
</style>