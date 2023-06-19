from sqlalchemy.orm import Session

from schemas.page_element import CreateElementRequest, QueryElementRequest, UpdateElementRequest

def query(db: Session, request: QueryElementRequest): pass
def get(db: Session, page_element_id: str): pass
def delete(db: Session, page_element_id: str): pass
def update(db: Session, page_element_id: str, reqeust: UpdateElementRequest): pass
def create(db: Session, requst: CreateElementRequest): pass