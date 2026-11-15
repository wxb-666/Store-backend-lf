# FastAPI 后端开发镜像。
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 先安装依赖，以便在业务代码变更时复用 Docker 构建缓存。
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

# 默认命令便于单独运行镜像；开发环境由 docker-compose.yml 的 command 启用热重载。
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
