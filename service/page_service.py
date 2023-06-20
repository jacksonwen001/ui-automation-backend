from fastapi import HTTPException
from sqlalchemy import desc
from models.page import Page
from sqlalchemy.orm import Session

from schemas.page import CreatePageRequest, QueryPageRequest, QueryPageResponse, QueryPagesResponse, UpdatePageRequest

def query(db: Session, request: QueryPageRequest) -> QueryPagesResponse:
    page_query = db.query(Page).filter(Page.project_id == request.project_id)
    if request.name: 
        page_query = page_query.filter(Page.name.like('%{}%'.format(request.name)))
    total = page_query.count() 
    pages = page_query.order_by(desc(Page.created_at)).limit(request.size).offset((request.current - 1) * request.size).all()
    
    return QueryPagesResponse(total = total, pages=[QueryPageResponse(
        id = page.id, 
        project_id = page.project_id, 
        name = page.name, 
        created_at = page.created_at
    ) for page in pages])

def create(db: Session, request: CreatePageRequest):
    page = Page(project_id = request.project_id, name = request.name) 
    db.add(page)
    db.commit()
    db.refresh(page)

def get(db: Session, page_id: str):
    page = db.query(Page).filter(Page.id == page_id).first()
    if not page: raise HTTPException(status_code=404, detail="page not found! id={}".format(page_id))
    return page

def update(db: Session, page_id: str, request: UpdatePageRequest):
    page = get(db, page_id=page_id)
    page.name = request.name
    db.add(page)
    db.commit()
    db.refresh(page)

def delete(db: Session, page_id: str):
    page = get(db, page_id)
    db.delete(page)
    db.commit()

