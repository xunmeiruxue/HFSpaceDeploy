from __future__ import annotations
import shutil, subprocess, tempfile, textwrap, time
from pathlib import Path
from typing import Dict
from huggingface_hub import HfApi
from huggingface_hub.errors import HfHubHTTPError
from .exceptions import (
    DockerfileMissingError,
    RepoCloneError,
    SpaceBuildTimeoutError,
    SpaceCreationError,
    SpaceDeployError,
)

__all__ = [
    "deploy_space",
    "SpaceDeployError",
]

def deploy_space(*, hf_token: str, git_repo_url: str, space_name: str, space_port: int, description: str, env_vars: Dict[str, str], private: bool) -> str:
    api = HfApi(token=hf_token)
    try:
        username = api.whoami()
        repo_id = f"{username}/{space_name}"
        api.create_repo(
            repo_id=repo_id,
            repo_type="space",
            space_sdk="docker",
            private=private,
            # space_variables=[{}],
            space_secrets=[{"key": k, "value": v} for k, v in env_vars.items()],
            exist_ok=False,
        )
    except HfHubHTTPError as exc:
        raise SpaceCreationError(exc) from exc

    tmp = tempfile.mkdtemp(prefix="hf_space_")
    try:
        res = subprocess.run(["git", "clone", "--depth", "1", git_repo_url, tmp], capture_output=True, text=True)
        if res.returncode:
            raise RepoCloneError(res.stderr)
        Path(tmp, ".git").with_suffix("").unlink(missing_ok=True)
        if not Path(tmp, "Dockerfile").exists():
            raise DockerfileMissingError()
        readme = Path(tmp, "README.md")
        header = textwrap.dedent(
            f"""---\ntitle: \"{space_name}\"\nemoji: \"🚀\"\ncolorFrom: blue\ncolorTo: green\nsdk: docker\napp_port: {space_port}\n---\n"""
        )
        readme.write_text(f"{header}\n{description}\n")
        api.upload_folder(folder_path=tmp, repo_id=repo_id, repo_type="space", ignore_patterns=[".git"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    deadline = time.time() + 15 * 60
    while time.time() < deadline:
        stage = api.get_space_runtime(repo_id).stage
        if stage == "RUNNING":
            return f"https://huggingface.co/spaces/{repo_id}"
        if stage == "ERROR":
            raise SpaceDeployError("Space failed during build/runtime")
        time.sleep(5)
    raise SpaceBuildTimeoutError()
