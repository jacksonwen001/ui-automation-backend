from fastapi import APIRouter


router = APIRouter(tags=['scenario_operations'], prefix='/scenario/operations')

@router.post('')
async def create(): pass

@router.get('')
async def query(): pass

@router.put('/{scenario_operation_id}')
async def update(scenario_operation_id: str): pass

@router.delete('/{scenario_operation_id}')
async def delete(scenario_operation_id: str): pass