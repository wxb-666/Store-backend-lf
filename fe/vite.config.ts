import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server:{
    host: '0.0.0.0',  // 确保容器外能访问
    watch: {
      usePolling: true, // 开启轮询
      interval: 500  // 检查间隔500毫秒
    }
  }
})
