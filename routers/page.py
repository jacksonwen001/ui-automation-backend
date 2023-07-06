from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.page import CreatePageRequest, QueryPageRequest, PageResponse, QueryPageUsagesResponse, QueryPagesResponse, UpdatePageRequest
from service import page_service
from routers import get_db


router = APIRouter(tags=['pages'], prefix='/pages')

@router.get('')
async def query(*, request: Annotated[QueryPageRequest, Depends()], db: Session = Depends(get_db)) -> QueryPagesResponse: 
    return page_service.query(db, request)

@router.put('/{page_id}')
async def update(*, page_id: str, request: UpdatePageRequest, db: Session = Depends(get_db)): 
    page_service.update(db, page_id=page_id, request=request)

@router.post('')
async def create(*, request: CreatePageRequest, db: Session = Depends(get_db)): 
    page_service.create(db=db, request=request)

@router.delete('/{page_id}')
async def delete(page_id: str, db: Session = Depends(get_db)): 
    page_service.delete(db=db, page_id=page_id)

@router.get('/{page_id}/usages')
async def get(page_id: str, db: Session = Depends(get_db)) -> QueryPageUsagesResponse:
    return page_service.query_page_usages(db, page_id)
