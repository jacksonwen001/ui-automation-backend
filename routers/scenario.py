from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from routers import get_db
from schemas.scenario import CreateScenarioRequest, QueryScenarioRequest, QueryScenariosResponse, UpdateScenarioRequest
from service import scenario_service

router = APIRouter(tags=['scenarios'], prefix='/scenarios')

@router.post('', status_code=201, description="create scenario")
async def create(*, db:Session=Depends(get_db), request: CreateScenarioRequest): 
    scenario_service.create(db=db, request=request)

@router.get('', status_code=200, description="query and paginate scenarios")
async def query(*, db:Session=Depends(get_db), request: Annotated[QueryScenarioRequest, Depends()]) -> QueryScenariosResponse: 
    return scenario_service.query(db=db, request=request)

@router.put('/{scenario_id}', status_code=200)
async def update(*, db:Session=Depends(get_db), scenario_id: str, request: UpdateScenarioRequest): 
    scenario_service.update(db=db, scenario_id=scenario_id, reqeust=request)

@router.delete('/{scenario_id}', status_code=200)
async def delete(*, db:Session=Depends(get_db), scenario_id: str): 
    scenario_service.delete(db, scenario_id=scenario_id)