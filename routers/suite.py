from fastapi import APIRouter

router = APIRouter(tags=['suites'], prefix='/suites')

@router.post('')
async def create(): pass

@router.get('')
async def query(): pass

@router.put('/{suite_id}')
async def update(suite_id: str): pass

@router.delete('/{suite_id}')
async def delete(suite_id: str): pass