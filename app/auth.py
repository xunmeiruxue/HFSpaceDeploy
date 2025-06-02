from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from .config import get_settings

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def require_api_key(api_key: str | None = Security(api_key_header)) -> str:
    settings = get_settings()
    if api_key is None or api_key not in settings.api_key:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Invalid or missing API key",
        )
    return api_key  # returned value can be injected downstream if needed