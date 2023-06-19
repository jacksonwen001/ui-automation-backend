from fastapi import APIRouter


router = APIRouter(tags=['elements'], prefix='/page/elements')

@router.get('')
async def query(): pass

@router.put('/{element_id}')
async def update(element_id: str): pass

@router.post('')
async def create(): pass

@router.delete('/{element_id}')
async def delete(element_id: str): pass