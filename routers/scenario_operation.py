from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers import get_db
from schemas.scenario_operation import CreateScenarioOperationRequest


router = APIRouter(tags=['scenario_operations'], prefix='/scenario/page/operations')

@router.post('')
async def create(*, db:Session=Depends(get_db), request:CreateScenarioOperationRequest): pass

@router.get('')
async def query(*, db:Session=Depends(get_db)): pass

@router.delete('/{scenario_operation_id}')
async def delete(*, db:Session=Depends(get_db), scenario_operation_id: str): pass