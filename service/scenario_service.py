from sqlalchemy.orm import Session

from schemas.scenario import CreateScenarioRequest, QueryScenarioRequest, UpdateScenarioRequest


def query(db: Session, request: QueryScenarioRequest): pass
def get(db: Session, scenario_id: str): pass
def delete(db: Session, scenario_id: str): pass
def update(db: Session, scenario_id: str, reqeust: UpdateScenarioRequest): pass
def create(db: Session, requst: CreateScenarioRequest): pass