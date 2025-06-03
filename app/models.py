from typing import Any, Dict, Optional
# from huggingface_hub import SpaceStage
from pydantic import BaseModel, Field

class DeployRequest(BaseModel):
    hf_token: str = Field(..., description="HF token with write permission")
    git_repo_url: str = Field(...)
    deploy_path: str = Field("/")
    space_name: str = Field(...)
    space_port: int = Field(7860)
    description: str = Field("")
    env_vars: Dict[str, str] = Field(default_factory=dict)
    private: bool = Field(False)

class DeployStatus(BaseModel):
    task_id: str
    status: str  # PENDING | IN_PROGRESS | SUCCESS | FAILED
    detail: Optional[Any] = None

