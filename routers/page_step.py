from fastapi import APIRouter


router = APIRouter(tags=['steps'], prefix='/page/steps')

@router.get('')
async def query(): pass

@router.put('/{step_id}')
async def update(step_id: str): pass

@router.post('')
async def create(): pass

@router.delete('/{step_id}')
async def delete(step_id: str): pass