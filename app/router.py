from fastapi import BackgroundTasks, FastAPI, HTTPException, Depends
import uuid

from app.models import DeployRequest, DeployStatus
from app.store import TaskStore
from app.deploy import deploy_space, SpaceDeployError
from app.auth import require_api_key

app = FastAPI(title="HF Space Deployer", version="1.0.0")

@app.post("/deploy", response_model=DeployStatus, status_code=202, dependencies=[Depends(require_api_key)])
async def deploy(req: DeployRequest, bg: BackgroundTasks):
    task_id = str(uuid.uuid4())
    TaskStore.save(DeployStatus(task_id=task_id, status="PENDING"))
    bg.add_task(_run_task, task_id, req)
    return TaskStore.load(task_id)

@app.get("/deploy/status/{task_id}", response_model=DeployStatus, dependencies=[Depends(require_api_key)])
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
