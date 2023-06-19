from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers import get_db
from schemas.page import QueryPageRequest
from schemas.page_step import CreatePageStepRequest, UpdatePageStepOrderRequest, UpdatePageStepRequest
from service import page_step_service

router = APIRouter(tags=['steps'], prefix='/page/steps')

@router.get('')
async def query(*, db: Session=Depends(get_db), reqeust: Annotated[QueryPageRequest, Depends()]): 
    return page_step_service.query(db, reqeust)

@router.put('/{step_id}')
async def update(*, db:Session=Depends(get_db), step_id: str, request: UpdatePageStepRequest): 
    page_step_service.update(db=db, reqeust=request)

@router.put('/orders')
async def update(*, db:Session=Depends(get_db), request: UpdatePageStepOrderRequest): 
    page_step_service.updateOrder(db=db, reqeust=request)

@router.post('')
async def create(*, db: Session=Depends(get_db), request: CreatePageStepRequest): 
    page_step_service.create(db=db, requst=request)

@router.delete('/{step_id}')
async def delete(*, db:Session=Depends(get_db), step_id: str): 
    page_step_service.delete(db=db, step_id=step_id)