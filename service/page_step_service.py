import uuid
from fastapi import HTTPException
from sqlalchemy import asc
from sqlalchemy.orm import Session
from models.page_element import PageElement
from models.page_step import PageStep

from schemas.page_step import CreatePageStepRequest, QueryPageStepRequest, QueryPageStepResponse, QueryPageStepsResponse, UpdatePageStepOrderRequest, UpdatePageStepRequest


def query(db: Session, request: QueryPageStepRequest): 
    steps = db\
            .query(PageStep.id, PageStep.operation_id, PageStep.command, PageStep.element_id, PageStep.value, PageStep.order_no, PageElement.name) \
            .outerjoin(PageElement, PageStep.element_id == PageElement.id) \
            .filter(PageStep.operation_id == request.operation_id).order_by(asc(PageStep.order_no)) \
            .all(); 
    
    return steps

def display(db:Session, request: QueryPageStepRequest) -> QueryPageStepsResponse:
    steps = query(db=db, request=request)
    print("steps:{}".format(steps))
    print("total: {}".format(len(steps)))
    return QueryPageStepsResponse(total = len(steps), steps = [QueryPageStepResponse(
        id = step.id, 
        operation_id = step.operation_id, 
        command = step.command, 
        element_id = step.element_id,
        element_name = step.name,
        value = step.value, 
        order_no = step.order_no  
    ) for step in steps])
        
def get(db: Session, page_step_id: str) -> PageStep: 
    step = db.query(PageStep).filter(PageStep.id == page_step_id).first()
    if not step: raise HTTPException(status_code = 404, detail="page step not found. id={}".format(page_step_id))
    return step

def delete(db: Session, page_step_id: str): 
    page = get(db = db, page_step_id = page_step_id)
    db.delete(page)
    db.commit()
    
def update(db: Session, page_step_id: str, request: UpdatePageStepRequest): 
    step = get(db=db, page_step_id=page_step_id)
    step.command = request.command
    step.element_id = request.element_id
    step.value = request.value
    db.add(step)
    db.commit()
    db.refresh(step)

def updateOrder(db: Session, reqeust: UpdatePageStepOrderRequest): 
    db.bulk_update_mappings(PageStep, reqeust.steps)
    db.commit()


def create(db: Session, request: CreatePageStepRequest): 
    step = PageStep(
        id = uuid.uuid4(), 
        project_id = request.project_id, 
        page_id = request.page_id, 
        operation_id = request.operation_id, 
        command = request.command, 
        element_id = request.element_id,
        value = request.value, 
        order_no = request.order_no
    )
    db.add(step)
    db.commit()