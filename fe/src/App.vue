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

        <!-- 居中的发布按钮 -->
        <button class="publish-btn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
          发布在线商店
        </button>

        <div class="contact">有问题吗？ (844) 982-1186</div>
      </header>

      <!-- 滚动内容区 -->
      <div class="scroll-area">
        <!-- 欢迎及AI助手区域 -->
        <section class="welcome-section">
          <h1 class="greeting-title">support 已初具规模<br/>接下来想做什么?</h1>

          <!-- AI 输入框 -->
          <div class="ai-input-box">
            <div class="input-left">
              <span class="avatar-pill">SU</span>
              <input type="text" placeholder="我的商店可以上线了吗？" />
            </div>
            <div class="ai-actions">
              <span class="action-item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg> 最近记录</span>
              <span class="divider"></span>
              <span class="action-icon">+</span>
              <span class="action-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg></span>
            </div>
          </div>
        </section>

        <!-- 底部卡片网格区域 -->
        <section class="task-grid">
          <!-- 卡片 1 -->
          <div class="task-card">
            <div class="card-img-placeholder gray-placeholder"></div>
            <h3>设置支付</h3>
            <p>激活 Shopify Payments，让客户可以通过卡、Shop Pay 等方式付款。</p>
            <button class="outline-btn">激活支付</button>
          </div>

          <!-- 卡片 2 -->
          <div class="task-card">
            <div class="card-img-placeholder domain-card">
              <span class="domain-text">helpharbor.store</span>
            </div>
            <h3>为 support 获取匹配的域名</h3>
            <p>我们找到了与您的商店匹配的域名。选择您心仪的域名并即刻拥有。</p>
            <button class="outline-btn">选择域名</button>
          </div>

          <!-- 卡片 3 (彩色背景) -->
          <div class="task-card highlight-card">
            <div class="highlight-top">
              <div class="card-progress">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/></svg>
                已完成 8 项任务中的 4 项
              </div>
              <div class="illustration-box">
                <!-- 绿色斜线纹路 -->
              </div>
            </div>
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
              <li><span class="circle"></span> 重写单板商品描述</li>
              <li><span class="circle"></span> 替换首页测试文案</li>
              <li><span class="circle"></span> 发布购物政策，澄清下单条件</li>
            </ul>
            <button class="outline-btn">开始</button>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import Sidebar from './components/Sidebar.vue'
</script>

<style scoped>
/* 全局外层（黑色背景露出） */
.app-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  background-color: #1a1a1a; /* 和侧边栏同色 */
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  overflow: hidden;
}

/* 右侧白色主内容区 */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  border-radius: 16px;
  margin: 8px 8px 8px 0; /* 留出边距露出黑底 */
  overflow: hidden;
}

/* 顶部状态栏 */
.top-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  font-size: 14px;
  position: relative;
}

.status {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 500;
  color: #111;
}

.status .dot {
  width: 8px;
  height: 8px;
  background-color: #10b981;
  border-radius: 50%;
}

.contact {
  color: #71717a;
  font-size: 13px;
}

/* 顶部发布按钮 */
.publish-btn {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 8px;
  background: #111;
  color: white;
  padding: 8px 24px;
  border-radius: 99px;
  font-size: 14px;
  font-weight: 500;
  border: none;
  cursor: pointer;
}

/* 滚动区域 */
.scroll-area {
  flex: 1;
  overflow-y: auto;
  padding: 40px;
  background-color: #ffffff;
}

/* 欢迎区域 */
.welcome-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
  margin: 0 auto 48px auto;
}

.greeting-title {
  font-size: 28px;
  text-align: center;
  margin-bottom: 24px;
  color: #111;
  line-height: 1.4;
  font-weight: 700;
}

/* AI 输入框 */
.ai-input-box {
  width: 100%;
  max-width: 680px;
  background: white;
  border: 1px solid #e4e4e7;
  border-radius: 16px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.04);
}

.input-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar-pill {
  background: #7c3aed;
  color: white;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: bold;
}

.ai-input-box input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 15px;
  color: #333;
}

.ai-actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
  color: #71717a;
  font-size: 13px;
}

.action-item {
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
}

.divider {
  width: 1px;
  height: 12px;
  background: #e4e4e7;
}

.action-icon {
  cursor: pointer;
  display: flex;
  align-items: center;
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
  border-radius: 12px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  border: 1px solid #e4e4e7;
  box-shadow: 0 2px 10px rgba(0,0,0,0.02);
}

.task-card h3 {
  font-size: 15px;
  margin: 16px 0 8px 0;
  color: #111;
  font-weight: 600;
}

.task-card p {
  font-size: 13px;
  color: #71717a;
  line-height: 1.5;
  flex: 1;
  margin-bottom: 16px;
}

.outline-btn {
  align-self: flex-start;
  padding: 6px 16px;
  background: white;
  border: 1px solid #e4e4e7;
  border-radius: 20px;
  font-size: 13px;
  cursor: pointer;
  font-weight: 500;
  color: #333;
  transition: all 0.2s;
}

.outline-btn:hover {
  background: #f4f4f5;
}

/* 卡片占位图和特殊样式 */
.card-img-placeholder {
  height: 120px;
  border-radius: 8px;
  background: #f4f4f5;
}

.domain-card {
  display: flex;
  align-items: center;
  justify-content: center;
}

.domain-text {
  background: white;
  padding: 6px 16px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 500;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  color: #3b82f6;
}

/* 浅绿卡片 */
.highlight-card {
  background: #ecfdf5;
  border-color: #d1fae5;
}

.highlight-top {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.card-progress {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #059669;
}

.illustration-box {
  height: 100px;
  border-radius: 8px;
  background: repeating-linear-gradient(
    -45deg,
    #a7f3d0,
    #a7f3d0 8px,
    transparent 8px,
    transparent 16px
  );
}

/* 任务列表卡片 */
.list-progress {
  font-size: 12px;
  color: #71717a;
  margin-bottom: 12px;
}

.checklist {
  list-style: none;
  padding: 0;
  margin: 0 0 16px 0;
}

.checklist li {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  margin-bottom: 12px;
  color: #52525b;
}

.circle {
  width: 14px;
  height: 14px;
  border: 1.5px solid #d4d4d8;
  border-radius: 50%;
}
</style>