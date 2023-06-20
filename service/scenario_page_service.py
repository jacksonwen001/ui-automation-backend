from fastapi import HTTPException
from sqlalchemy import asc
from sqlalchemy.orm import Session

from models.page import Page
from models.scenario_page import ScenarioPage
from schemas.scenario_page import CreateScenarioPageRequest, QueryScenarioPageResponse, QueryScenarioPagesResponse, UpdateScenarioPageOrderRequest

def query(db: Session, scenario_id: str): 
    scenario_pages = db \
        .query(ScenarioPage.id, ScenarioPage.order_no,ScenarioPage.page_id, Page.name)\
        .outerjoin(Page, ScenarioPage.page_id == Page.id) \
        .filter(ScenarioPage.scenario_id == scenario_id).order_by(asc(ScenarioPage.order_no)).all()
    return scenario_pages

def display(db: Session, scenario_id: str) -> QueryScenarioPagesResponse:
    scenario_pages = query(db, scenario_id)
    return QueryScenarioPagesResponse(
        pages = [QueryScenarioPageResponse(
          id = scenario_page.id, 
          page_id = scenario_page.page_id, 
          order_no = scenario_page.order_no, 
          name = scenario_page.name
        ) for scenario_page in scenario_pages]
    )
    
def get(db: Session, scenario_page_id: str) -> ScenarioPage: 
    page = db.query(ScenarioPage).filter(ScenarioPage.id == scenario_page_id).first()
    if not page: raise HTTPException(status_code=404, detail="scenario page not found. id={}".format(scenario_page_id))
    return page 

def delete(db: Session, scenario_page_id: str):
    page = get(db, scenario_page_id)
    db.delete(page)
    pages = db.query(ScenarioPage) \
        .filter(ScenarioPage.scenario_id == page.scenario_id and ScenarioPage.id != scenario_page_id) \
        .order_by(asc(ScenarioPage.order_no)).all()
    
    for i in range(pages):
        pages[i].order_no = i 
    mappings = {p.id: p.order_no for p in pages}
    db.bulk_update_mappings(mapper = ScenarioPage, mappings = mappings)
    db.commit() 

def updateOrder(db: Session, request: UpdateScenarioPageOrderRequest):
    db.bulk_update_mappings(ScenarioPage, request.pages)
    db.commit()
    
def create(db: Session, request: CreateScenarioPageRequest): 
    page = ScenarioPage(
        project_id = request.project_id, 
        scenario_id = request.scenario_id, 
        page_id = request.page_id, 
        order_no = request.order_no
    )
    db.add(page)
    db.commit()
    db.refresh(page)