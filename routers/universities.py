from fastapi import APIRouter
from starlette.responses import JSONResponse
from config.celery_utils import get_task_info

from celery_tasks.tasks import get_all_universities_task
from schemas.schemas import Country


router = APIRouter(
    prefix="/universities", 
    tags=['university'], 
    responses={
        404: {"description": "Not found"}
    }
)

@router.post('/async')
async def get_universiites_async(country: Country): 
    task = get_all_universities_task.apply_async(args=[country.countries])
    return JSONResponse({'task_id': task.id})

@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)