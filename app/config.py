from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Global configuration loaded from environment variables."""
    redis_url: str = Field("redis://localhost:6379")
    api_key: str = Field("123456")

    model_config = SettingsConfigDict(
        env_file        = BASE_DIR / ".env",
        env_file_encoding = "utf-8",
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()
