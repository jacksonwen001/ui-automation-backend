from fastapi import APIRouter

router = APIRouter(tags=['users'], prefix='/users')

@router.post('')
async def create(): pass

@router.get('')
async def query(): pass

@router.put('/{user_id}')
async def update(user_id: str): pass

@router.delete('/{user_id}')
async def delete(user_id: str): pass