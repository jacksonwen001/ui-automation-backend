from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from routers import get_db
from schemas.scenario import CreateScenarioRequest, QueryScenarioRequest, UpdateScenarioRequest
from service import scenario_service

router = APIRouter(tags=['scenarios'], prefix='/scenarios')

@router.post('')
async def create(*, db:Session=Depends(get_db), request: CreateScenarioRequest): 
    scenario_service.create(db=db, request=request)

@router.get('')
async def query(*, db:Session=Depends(get_db), request: Annotated[QueryScenarioRequest, Depends()]): 
    return scenario_service.query(db=db, request=request)

@router.put('/{scenario_id}')
async def update(*, db:Session=Depends(get_db), scenario_id: str, request: UpdateScenarioRequest): 
    scenario_service.update(db=db, scenario_id=scenario_id, reqeust=request)

@router.delete('/{scenario_id}')
async def delete(*, db:Session=Depends(get_db), scenario_id: str): 
    scenario_service.delete(db, scenario_id=scenario_id)