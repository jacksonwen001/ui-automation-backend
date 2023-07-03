from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers import get_db
from schemas.scenario_operation import CreateScenarioOperationRequest, QueryScenarioOperationRequest, QueryScenarioOperationsResponse
from service import scenario_operation_service

router = APIRouter(tags=['scenario_operations'], prefix='/scenario/page/operations')

@router.get('', description="query all operations")
async def query(*, db: Session = Depends(get_db), req: Annotated[QueryScenarioOperationRequest, Depends()]) -> QueryScenarioOperationsResponse: 
    return scenario_operation_service.display(db=db, request=req)

@router.post('', status_code=201, description="add operation into scenario page")
async def create(*, db:Session=Depends(get_db), request:CreateScenarioOperationRequest): 
    scenario_operation_service.create()

@router.delete('/{scenario_operation_id}')
async def delete(*, db:Session=Depends(get_db), scenario_operation_id: str): 
    scenario_operation_service.delete(db=db, scenario_operation_id=scenario_operation_id)