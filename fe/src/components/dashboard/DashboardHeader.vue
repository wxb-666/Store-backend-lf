<template>
  <header class="dashboard-header">
    <div class="selling-status"><span />可以销售</div>
    <a href="tel:8449821186">有问题吗？ <strong>(844) 982-1186</strong></a>
  </header>
</template>

<style scoped>
.dashboard-header { display: flex; align-items: center; justify-content: space-between; min-height: 72px; padding: 18px 32px; }
.selling-status { display: inline-flex; align-items: center; gap: 9px; color: #303030; font-size: 15px; }
.selling-status span { width: 10px; height: 10px; background: #49d936; border-radius: 50%; box-shadow: 0 0 0 5px #effceb; }
a { color: #606060; font-size: 14px; text-decoration: none; } a strong { color: #303030; text-decoration: underline; }
@media (max-width: 640px) { .dashboard-header { min-height: 60px; padding-inline: 18px; } a { display: none; } }
</style>
