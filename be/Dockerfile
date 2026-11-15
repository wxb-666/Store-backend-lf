# 后端开发镜像。后续接入 API 后，可在此安装依赖并替换启动命令。
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY . ./

EXPOSE 8000

# 当前后端尚未实现 API，保留容器运行环境以便后续开发。
CMD ["python", "-c", "import time; time.sleep(10**9)"]
