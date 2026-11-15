# 前端开发镜像：依赖在构建阶段安装，源码由 Compose 挂载以支持热更新。
FROM node:24-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . ./

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
