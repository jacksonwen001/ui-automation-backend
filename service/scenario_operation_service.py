from sqlalchemy.orm import Session

from schemas.scenario_operation import CreateScenarioOperationRequest 

def query(db: Session, request: CreateScenarioOperationRequest): pass

def display(db: Session, request: CreateScenarioOperationRequest): pass

