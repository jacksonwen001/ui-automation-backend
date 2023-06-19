from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers import get_db
from schemas.page_element import CreateElementRequest, QueryElementRequest, UpdateElementRequest
from service import page_element_service


router = APIRouter(tags=['elements'], prefix='/page/elements')

@router.get('')
async def query(*, db:Session=Depends(get_db), request: Annotated[QueryElementRequest, Depends()]): 
    return page_element_service.query(db=db, request=request)

@router.put('/{element_id}')
async def update(*, db:Session=Depends(get_db), element_id: str, request: UpdateElementRequest): 
    page_element_service.update(db=db, element_id=element_id, reqeust=request)

@router.post('')
async def create(*, db:Session=Depends(get_db), request: CreateElementRequest): 
    page_element_service.create(db=db, requst=request)

@router.delete('/{element_id}')
async def delete(*, db:Session=Depends(get_db), element_id: str): 
    page_element_service.delete(db=db, element_id=element_id)