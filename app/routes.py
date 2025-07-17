from fastapi import BackgroundTasks, FastAPI, HTTPException, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
import uuid
from app.models import DeployRequest, DeployStatus
from app.store import TaskStore
from app.deploy import deploy_space, SpaceDeployError
from app.auth import require_api_key

app = FastAPI(title="HF Space Deployer", version="1.0.0")

# Static files and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.add_middleware(GZipMiddleware)
templates = Jinja2Templates(directory="app/templates")


def _parse_vars_from_text(text: str) -> dict:
    """Helper to parse key-value pairs from a multiline string."""
    variables = {}
    if text and text.strip():
        for line in text.strip().split('\n'):
            if '=' in line:
                key, value = line.split('=', 1)
                variables[key.strip()] = value.strip()
    return variables


# Web Interface Routes
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/web/deploy")
async def web_deploy(
        request: Request,
        hf_token: str = Form(...),
        git_repo_url: str = Form(...),
        space_name: str = Form(...),
        description: str = Form(""),
        space_port: int = Form(7860),
        private: bool = Form(False),
        # 修改：添加 space_variables_text 并重命名 env_vars_text
        space_variables_text: str = Form(""),
        space_secrets_text: str = Form(""),
        deploy_path: str = Form("/"),
        bg: BackgroundTasks = BackgroundTasks()
):
    # 修改：分别解析公开变量和机密
    space_variables = _parse_vars_from_text(space_variables_text)
    space_secrets = _parse_vars_from_text(space_secrets_text)

    deploy_req = DeployRequest(
        hf_token=hf_token,
        git_repo_url=git_repo_url,
        space_name=space_name,
        description=description,
        space_port=space_port,
        private=private,
        # 修改：传递两种类型的变量
        space_variables=space_variables,
        space_secrets=space_secrets,
        deploy_path=deploy_path
    )

    task_id = str(uuid.uuid4())
    TaskStore.save(DeployStatus(task_id=task_id, status="PENDING"))
    bg.add_task(_run_task, task_id, deploy_req)

    return RedirectResponse(url=f"/deploy/{task_id}", status_code=303)


@app.get("/deploy/{task_id}", response_class=HTMLResponse)
async def deploy_status_page(request: Request, task_id: str):
    status = TaskStore.load(task_id)
    if not status:
        raise HTTPException(status_code=404, detail="Task not found")

    return templates.TemplateResponse("deploy_status.html", {
        "request": request,
        "task_id": task_id,
        "status": status.status
    })


# API Routes
@app.post("/deploy", response_model=DeployStatus, status_code=202)
async def deploy(req: DeployRequest, bg: BackgroundTasks):
    task_id = str(uuid.uuid4())
    TaskStore.save(DeployStatus(task_id=task_id, status="PENDING"))
    # 注意：这里的 req 会自动根据更新后的 DeployRequest 模型进行验证
    bg.add_task(_run_task, task_id, req)
    return TaskStore.load(task_id)


@app.get("/deploy/status/{task_id}", response_model=DeployStatus)
async def status(task_id: str):
    status = TaskStore.load(task_id)
    if not status:
        raise HTTPException(status_code=404, detail="Task not found")
    return status


# ------------------------------------------------------------------ #

def _run_task(task_id: str, req: DeployRequest):
    TaskStore.save(DeployStatus(task_id=task_id, status="IN_PROGRESS"))
    try:
        # 修改：将 req.dict() 传递给 deploy_space
        url = deploy_space(**req.dict())
        TaskStore.save(DeployStatus(task_id=task_id, status="SUCCESS", detail={"space_url": url}))
    except SpaceDeployError as exc:
        TaskStore.save(DeployStatus(task_id=task_id, status="FAILED", detail={"error": str(exc)}))
