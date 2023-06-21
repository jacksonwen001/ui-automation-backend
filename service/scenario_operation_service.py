from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.page_operation import PageOperation
from models.scenario_operation import ScenarioPageOperation

from schemas.scenario_operation import CreateScenarioOperationRequest, QueryScenarioOperationRequest, QueryScenarioOperationsResponse, ScenarioOperationResponse, UpdateOperationOrderRequest 

def query(db: Session, request: QueryScenarioOperationRequest): 
    return db.query(ScenarioPageOperation.id, ScenarioPageOperation.scenario_page_id, ScenarioPageOperation.operation_id, ScenarioPageOperation.order_no, PageOperation.name)\
      .outerjoin(PageOperation, ScenarioPageOperation.operation_id == PageOperation.id)\
      .filter(ScenarioPageOperation.scenario_page_id == request.page_id).all()

def display(db: Session, request: CreateScenarioOperationRequest): 
    operations = query(db, request)
    return QueryScenarioOperationsResponse(operations = [ScenarioOperationResponse(
        id = operation.id, 
        project_id = operation.project_id,
        scenario_page_id = operation.scenario_page_id, 
        operation_id= operation.operation_id, 
        order_no = operation.order_no
    ) for operation in operations])

def updateOrder(db:Session, request: UpdateOperationOrderRequest):
    db.bulk_update_mappings(mapper = ScenarioPageOperation, mappings = request.operations)

def create(db: Session, request: CreateScenarioOperationRequest):
    operation = ScenarioPageOperation(
        project_id = request.project_id,
        scenario_page_id = request.scenario_page_id, 
        operation_id = request.operation_id, 
        order_no = request.order_no
    )
    db.add(operation)
    db.commit()

def get(db:Session, operation_id: str):
    scenario_page = db.query(ScenarioPageOperation).filter(ScenarioPageOperation.operation_id == operation_id).first()
    if not scenario_page:
        raise HTTPException(status_code=404, detail="scenario operation not found. id={}".format(operation_id))
    return scenario_page
    
def delete(db:Session, operation_id: str):
    with db.begin():
      scenario_operation: ScenarioPageOperation|None = get(db, operation_id)
      db.delete(scenario_operation)
      operations = db.query(ScenarioPageOperation)\
          .filter(ScenarioPageOperation.scenario_page_id == scenario_operation.scenario_page_id and ScenarioPageOperation.id != scenario_operation.id)\
          .all()
      for i in range(0, len(operations)):
          operations[i].order_no = i
      mapping_operations = {operation.id: operation.order_no for operation in operations}
      db.bulk_update_mappings(mapper=ScenarioPageOperation, mappings=mapping_operations)
    