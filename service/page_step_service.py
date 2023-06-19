from sqlalchemy.orm import Session

from schemas.page_step import CreatePageStepRequest, QueryPageStepRequest, QueryPageStepsResponse, UpdatePageStepOrderRequest, UpdatePageStepRequest


def query(db: Session, request: QueryPageStepRequest) -> QueryPageStepsResponse: 
    db.query()
def get(db: Session, page_step_id: str): pass
def delete(db: Session, page_step_id: str): pass
def update(db: Session, page_step_id: str, reqeust: UpdatePageStepRequest): pass
def updateOrder(db: Session, reqeust: UpdatePageStepOrderRequest): pass
def create(db: Session, requst: CreatePageStepRequest): pass