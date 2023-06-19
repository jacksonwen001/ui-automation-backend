from fastapi import HTTPException
from models.page import Page
from sqlalchemy.orm import Session

from schemas.page import CreatePageRequest, UpdatePageRequest


def query(db: Session, name: str = None, current: int = 1, size: int = 10) -> Page:
    if (name):
        return db.query(Page).filter(Page.name.contains(name)).order_by(Page.created_at).limit(size).offset((current - 1) * size)
    
    return db.query(Page).order_by(Page.created_at).limit(size).offset((current - 1) * size)

def create(db: Session, request: CreatePageRequest):
    page = Page(name = request.name) 
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

