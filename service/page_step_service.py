from sqlalchemy.orm import Session

from schemas.page_step import CreatePageStepRequest, QueryPageStepRequest, UpdatePageStepRequest


def query(db: Session, request: QueryPageStepRequest): pass
def get(db: Session, page_step_id: str): pass
def delete(db: Session, page_step_id: str): pass
def update(db: Session, page_step_id: str, reqeust: UpdatePageStepRequest): pass
def create(db: Session, requst: CreatePageStepRequest): pass