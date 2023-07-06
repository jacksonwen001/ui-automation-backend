import uuid
from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from models.page_operation import PageOperation

from schemas.page_operation import CreatePageOperationRequest, QueryPageOperationRequest, QueryPageOperationResponse, QueryPageOperationsResponse, UpdatePageOperationRequest

def query(db: Session, request: QueryPageOperationRequest) -> QueryPageOperationsResponse: 
    operation_query = db.query(PageOperation).filter(PageOperation.page_id == request.page_id)

    total = operation_query.count()
    operations = operation_query.order_by(desc(PageOperation.created_at)) \
        .limit(request.size).offset((request.current - 1 ) * request.size).all()
    
    response = QueryPageOperationsResponse(total=total, operations=[QueryPageOperationResponse(
        id = operation.id, 
        project_id= operation.project_id, 
        page_id = operation.page_id, 
        name = operation.name, 
        created_at = operation.created_at
    ) for operation in operations])

    return response

def get(db: Session, page_operation_id: str) -> QueryPageOperationResponse: 
    operation = db.query(PageOperation).filter(PageOperation.id == page_operation_id).first()
    if not operation: raise HTTPException(status_code=404, detail="operation not found.id={}".format(page_operation_id))

    return QueryPageOperationResponse(
        id = operation.id, 
        project_id= operation.project_id, 
        page_id = operation.page_id, 
        name = operation.name, 
    )

def delete(db: Session, page_operation_id: str): 
    operation = get(db, page_operation_id=page_operation_id)
    db.delete(operation)
    db.commit()

def update(db: Session, page_operation_id: str, reqeust: UpdatePageOperationRequest): 
    operation = get(db=db, page_operation_id=page_operation_id)
    operation.name = reqeust.name
    db.commit()
    db.refresh()

def create(db: Session, request: CreatePageOperationRequest): 
    operation = PageOperation(id=uuid.uuid4(), project_id = request.project_id, page_id = request.page_id, name = request.name)
    db.add(operation)
    db.commit()
    db.refresh(operation)