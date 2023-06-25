from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session

from models.page_element import PageElement
from models.page_step import PageStep
from schemas.page_element import CreateElementRequest, QueryElementRequest, QueryElementResponse, QueryElementsResponse, UpdateElementRequest

def query(db: Session, request: QueryElementRequest): 
    element_query = db.query(PageElement, count(PageStep)).outerjoin(PageStep, PageElement.id == PageStep.element_id).filter(PageElement.page_id == request.page_id)
    count = element_query.count()
    elements = element_query.limit(request.size).offset((request.current - 1) * request.size).order_by(desc(PageElement.created_at)).all()
    return QueryElementsResponse(total = count, elements=[QueryElementResponse(
        id = element.id, 
        name = element.name, 
        selecotr = element.selector, 
        target = element.target,
        usage = element.count
    ) for element in elements])

def get(db: Session, page_element_id: str): 
    element = db.query(PageElement).filter(PageElement.id == page_element_id).first()
    if not element: raise HTTPException(status_code=404, detail="page element not found. id={}".format(page_element_id))
    return QueryElementResponse(
        id = element.id, 
        name = element.name, 
        selecotr = element.selector, 
        target = element.target
    )

def delete(db: Session, page_element_id: str): 
    element = get(db, page_element_id=page_element_id)
    db.delete(element)
    db.commit()

def update(db: Session, page_element_id: str, request: UpdateElementRequest): 
    element = get(db = db, page_element_id = page_element_id)
    element.name = request.name
    element.selector = request.selector
    element.target = request.target
    db.add(element)
    db.commit()
    db.refresh()

def create(db: Session, requst: CreateElementRequest): 
    element = PageElement(name = requst.name, selector = requst.selector, target = requst.target)
    db.add(element)
    db.commit()

