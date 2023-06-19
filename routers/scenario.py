from fastapi import APIRouter

router = APIRouter(tags=['scenarios'], prefix='/scenarios')

@router.post('')
async def create(): pass

@router.get('')
async def query(): pass

@router.put('/{scenario_id}')
async def update(scenario_id: str): pass

@router.delete('/{scenario_id}')
async def delete(scenario_id: str): pass