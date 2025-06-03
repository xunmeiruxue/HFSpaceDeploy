# 使用Python 3.11作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 安装依赖，包括 git 和 redis-server
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 复制并安装 Python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码和启动脚本
COPY . .
COPY start.sh .
RUN chmod +x start.sh # 赋予脚本执行权限

# 创建非 root 用户，并赋予 /app 目录和脚本权限
RUN adduser --disabled-password --gecos "" appuser \
    && chown -R appuser:appuser /app \
    && chown appuser:appuser start.sh

# 切换到非 root 用户
USER appuser

# 暴露端口
EXPOSE 7860

# 使用启动脚本启动 Redis 和 Python 应用
CMD ["./start.sh"]
