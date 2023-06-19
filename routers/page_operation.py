from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from routers import get_db
from schemas.page_operation import CreatePageOperationRequest, QueryPageOperationRequest, UpdatePageOperationRequest
from service import page_operation_service


router = APIRouter(tags=['page_operations'], prefix='/page/operations')

@router.get('')
async def query(*, db:Session=Depends(get_db), request: Annotated[QueryPageOperationRequest, Depends()]): 
    return page_operation_service.query(db=db, request=request)

@router.put('/{operation_id}')
async def update(*, db:Session=Depends(get_db), operation_id: str, request: UpdatePageOperationRequest): 
    page_operation_service.update(db=db, page_operation_id=operation_id, reqeust=request)

@router.post('')
async def create(*, db:Session=Depends(get_db), request: CreatePageOperationRequest): 
    page_operation_service.create(db=db, requst=request)

@router.delete('/{operation_id}')
async def delete(*, db:Session=Depends(get_db), operation_id: str): 
    page_operation_service.delete(db=db, page_operation_id=operation_id)