from sqlalchemy.orm import Session

from schemas.page_operation import CreatePageOperationRequest, QueryPageOperationRequest, UpdatePageOperationRequest


def query(db: Session, request: QueryPageOperationRequest): pass
def get(db: Session, page_operation_id: str): pass
def delete(db: Session, page_operation_id: str): pass
def update(db: Session, page_operation_id: str, reqeust: UpdatePageOperationRequest): pass
def create(db: Session, requst: CreatePageOperationRequest): pass