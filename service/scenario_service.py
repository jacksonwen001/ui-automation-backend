from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from models.scenario import Scenario

from schemas.scenario import CreateScenarioRequest, QueryScenarioRequest, QueryScenarioResponse, QueryScenariosResponse, UpdateScenarioRequest


def query(db: Session, request: QueryScenarioRequest): 
    scenario_query = db.query(Scenario).filter(Scenario.project_id == request.project_id); 
    if request.name: 
        scenario_query = scenario_query.filter(Scenario.name.like("%{}%".format(request.name)))
    
    total = scenario_query.count()
    scenarios = scenario_query.order_by(desc(Scenario.created_at)).limit(request.size).offset((request.current - 1) * request.size).all()
    
    return QueryScenariosResponse(total = total, scenarios = [QueryScenarioResponse(
        id = scenario.id, 
        project_id = scenario.project_id, 
        name = scenario.name, 
        description = scenario.description, 
        created_at = scenario.created_at
    ) for scenario in scenarios])    


def get(db: Session, scenario_id: str): 
    scenario = db.query(Scenario).filter(Scenario.id == scenario_id).first()
    if not scenario: raise HTTPException(status_code=404, detail="scenario not found. id={}".format(scenario_id))
    return QueryScenarioResponse(
        id = scenario.id, 
        project_id = scenario.project_id, 
        name = scenario.name, 
        created_at = scenario.created_at
    ) 

def delete(db: Session, scenario_id: str): 
    scenario = get(db, scenario_id=scenario_id)
    db.delete(scenario)
    db.commit()

def update(db: Session, scenario_id: str, request: UpdateScenarioRequest): 
    scenario = get(db=db, scenario_id=scenario_id)
    scenario.name = request.name
    scenario.description = request.description 
    db.add(scenario)
    db.commit()
    db.refresh()

def create(db: Session, request: CreateScenarioRequest): 
    scenario = Scenario(
        project_id = request.project_id,
        name = request.name,
        description = request.description
    )
    db.add(scenario)
    db.commit()