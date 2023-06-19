from fastapi import APIRouter


router = APIRouter(tags=['page_operations'], prefix='/page/operations')

@router.get('')
async def query(): pass

@router.put('/{operation_id}')
async def update(operation_id: str): pass

@router.post('')
async def create(): pass

@router.delete('/{operation_id}')
async def delete(operation_id: str): pass