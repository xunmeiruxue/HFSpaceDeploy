#!/bin/sh

# 以后台模式启动 Redis Server，禁用持久化
# 注意：以 appuser 身份运行，确保它有权限在默认位置或 /tmp 中创建必要文件
redis-server --daemonize yes --loglevel warning --save "" --appendonly no --pidfile /tmp/redis.pid

# 等待 Redis 启动 (可选，但有时有帮助)
sleep 2

# 在前台启动 Python 应用 (这个命令会保持容器运行)
exec python main.py
