from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class DeployRequest(BaseModel):
    hf_token: str = Field(..., description="HF token with write permission")
    git_repo_url: str = Field(...)
    deploy_path: str = Field("/")
    space_name: str = Field(...)
    space_port: int = Field(7860)
    description: str = Field("")
    # 修改：将 env_vars 重命名为 space_secrets，并添加 space_variables
    space_secrets: Dict[str, str] = Field(default_factory=dict, description="Secrets (e.g., API keys)")
    space_variables: Dict[str, str] = Field(default_factory=dict, description="Public variables")
    private: bool = Field(False)

class DeployStatus(BaseModel):
    task_id: str
    status: str  # PENDING | IN_PROGRESS | SUCCESS | FAILED
    detail: Optional[Any] = None
