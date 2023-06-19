from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from routers import get_db
from schemas.scenario_page import CreateScenarioPageRequest
from service import scenario_page_service

router = APIRouter(tags=['scenario_pages'], prefix='/scenario/pages')

@router.post('')
async def create(*, db:Session=Depends(get_db), request: CreateScenarioPageRequest): 
    scenario_page_service.create(db=db, request=request)

@router.get('')
async def query(*, db:Session=Depends(get_db), scenario_id: str): 
    return scenario_page_service.query(db=db, scenario_id=scenario_id)

@router.delete('/{scenario_page_id}')
async def delete(*, db:Session=Depends(get_db), scenario_page_id: str): 
    scenario_page_service.delete(db, scenario_page_id=scenario_page_id)