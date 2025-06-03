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
        env_vars_text: str = Form(""),
        deploy_path: str = Form("/"),
        bg: BackgroundTasks = BackgroundTasks()
):
    # Parse environment variables from textarea
    env_vars = {}
    if env_vars_text.strip():
        for line in env_vars_text.strip().split('\n'):
            if '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip()

    deploy_req = DeployRequest(
        hf_token=hf_token,
        git_repo_url=git_repo_url,
        space_name=space_name,
        description=description,
        space_port=space_port,
        private=private,
        env_vars=env_vars,
        deploy_path=deploy_path
    )

    task_id = str(uuid.uuid4())
    TaskStore.save(DeployStatus(task_id=task_id, status="PENDING"))
    bg.add_task(_run_task, task_id, deploy_req)

    # Redirect to status page instead of returning HTML
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
        url = deploy_space(**req.dict())
        TaskStore.save(DeployStatus(task_id=task_id, status="SUCCESS", detail={"space_url": url}))
    except SpaceDeployError as exc:
        TaskStore.save(DeployStatus(task_id=task_id, status="FAILED", detail={"error": str(exc)}))
