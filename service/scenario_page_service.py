from sqlalchemy.orm import Session

from schemas.scenario_page import CreateScenarioPageRequest

def query(db: Session, scenario_id: str): pass
def delete(db: Session, scenario_page_id: str): pass
def create(db: Session, requst: CreateScenarioPageRequest): pass