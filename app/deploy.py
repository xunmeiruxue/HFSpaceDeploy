from __future__ import annotations
import shutil, tempfile, textwrap, time
from pathlib import Path
from typing import Dict
import git
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

from .utils import _chmod_and_retry


def deploy_space(*, hf_token: str, git_repo_url: str, deploy_path: str, space_name: str, space_port: int, description: str, env_vars: Dict[str, str], private: bool) -> str:
    deploy_path = deploy_path.strip(".").strip("/")
    api = HfApi(token=hf_token)
    try:
        username = api.whoami().get("name", None)
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
        try:
            if not deploy_path:
                git.Repo.clone_from(
                    git_repo_url,
                    tmp,
                    depth=1,
                    multi_options=["--single-branch"]
                )
            else:
                repo = git.Repo.clone_from(
                    git_repo_url, tmp,
                    depth=1,
                    no_checkout=True,
                    filter=["tree:0"],
                    sparse=True,
                    multi_options=["--single-branch"],
                )
                repo.git.sparse_checkout("init", "--no-cone")
                repo.git.sparse_checkout("set", "--no-cone", f"/{deploy_path}/**")
                repo.git.checkout()

                # 平移文件到根目录
                src = Path(tmp, deploy_path)
                for item in src.iterdir():
                    shutil.move(item, tmp)  # 根目录目前是空的
                shutil.rmtree(src)
        except git.GitCommandError as exc:
            raise RepoCloneError(str(exc)) from exc

        git_dir = Path(tmp, ".git")
        if git_dir.exists() and git_dir.is_dir():
            shutil.rmtree(git_dir, onerror=_chmod_and_retry)

        if not Path(tmp, "Dockerfile").exists():
            raise DockerfileMissingError()

        readme = Path(tmp, "README.md")
        header = (
            f"---\n"
            f"title: \"{space_name}\"\n"
            f"emoji: \"🚀\"\n"
            f"colorFrom: blue\n"
            f"colorTo: green\n"
            f"sdk: docker\n"
            f"app_port: {space_port}\n"
            f"---\n"
        )
        badge = (
            f"### 🚀 一键部署\n"
            f"[![Deploy with HFSpaceDeploy](https://img.shields.io/badge/Deploy_with-HFSpaceDeploy-green?style=social&logo=rocket)](https://github.com/kfcx/HFSpaceDeploy)\n\n"
            f"本项目由[HFSpaceDeploy](https://github.com/kfcx/HFSpaceDeploy)一键部署\n"
        )
        readme.write_text(f"{header}\n{badge}\n{description}\n", encoding="utf-8")
        api.upload_folder(folder_path=tmp, repo_id=repo_id, repo_type="space", ignore_patterns=[".git"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    deadline = time.time() + 15 * 60
    while time.time() < deadline:
        stage = api.get_space_runtime(repo_id).stage
        if stage == "RUNNING":
            return f"https://huggingface.co/spaces/{repo_id}"
        if stage == "BUILD_ERROR":
            raise SpaceDeployError("Space failed during build/runtime")
        time.sleep(5)
    raise SpaceBuildTimeoutError()
