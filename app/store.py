import json
from typing import Optional
from redis import StrictRedis
from .config import get_settings
from .models import DeployStatus

_settings = get_settings()
redis_client = StrictRedis.from_url(
    _settings.redis_url,
    decode_responses=True,
    # 连接池配置
    max_connections=50,          # 最大连接数
    retry_on_timeout=True,       # 超时重试
    socket_timeout=15,            # socket 超时
    socket_connect_timeout=15,    # 连接超时
    health_check_interval=300,    # 健康检查间隔
)

class TaskStore:
    prefix = "task:"

    @classmethod
    def _key(cls, task_id: str) -> str:
        return f"{cls.prefix}{task_id}"

    @classmethod
    def save(cls, status: DeployStatus) -> None:
        redis_client.hset(
            cls._key(status.task_id),
            mapping={
                "status": status.status,
                "detail": json.dumps(status.detail) if status.detail else "",
            },
        )
        redis_client.expire(cls._key(status.task_id), 7 * 24 * 3600)

    @classmethod
    def load(cls, task_id: str) -> Optional[DeployStatus]:
        data = redis_client.hgetall(cls._key(task_id))
        if not data:
            return None
        detail = json.loads(data.get("detail", "null")) if data.get("detail") else None
        return DeployStatus(task_id=task_id, status=data.get("status", "UNKNOWN"), detail=detail)
