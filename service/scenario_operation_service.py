from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.page_operation import PageOperation
from models.scenario_operation import ScenarioOperation

from schemas.scenario_operation import CreateScenarioOperationRequest, QueryScenarioOperationRequest, QueryScenarioOperationsResponse, ScenarioOperationResponse, UpdateOperationOrderRequest 

def query(db: Session, request: QueryScenarioOperationRequest): 
    return db.query(ScenarioOperation.id, ScenarioOperation.scenario_page_id, ScenarioOperation.operation_id, ScenarioOperation.order_no, PageOperation.name)\
      .outerjoin(PageOperation, ScenarioOperation.operation_id == PageOperation.id)\
      .filter(ScenarioOperation.scenario_page_id == request.scenario_page_id).all()

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
    db.bulk_update_mappings(mapper = ScenarioOperation, mappings = request.operations)

def create(db: Session, request: CreateScenarioOperationRequest):
    operation = ScenarioOperation(
        project_id = request.project_id,
        scenario_page_id = request.scenario_page_id, 
        operation_id = request.operation_id, 
        order_no = request.order_no
    )
    db.add(operation)
    db.commit()

def get(db:Session, operation_id: str):
    scenario_page = db.query(ScenarioOperation).filter(ScenarioOperation.operation_id == operation_id).first()
    if not scenario_page:
        raise HTTPException(status_code=404, detail="scenario operation not found. id={}".format(operation_id))
    return scenario_page
    
def delete(db:Session, operation_id: str):
    with db.begin():
      scenario_operation: ScenarioOperation|None = get(db, operation_id)
      db.delete(scenario_operation)
      operations = db.query(ScenarioOperation)\
          .filter(ScenarioOperation.scenario_page_id == scenario_operation.scenario_page_id and ScenarioOperation.id != scenario_operation.id)\
          .all()
      for i in range(0, len(operations)):
          operations[i].order_no = i
      mapping_operations = {operation.id: operation.order_no for operation in operations}
      db.bulk_update_mappings(mapper=ScenarioOperation, mappings=mapping_operations)
    