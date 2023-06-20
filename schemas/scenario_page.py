import datetime
from typing import Dict, List
from pydantic import BaseModel


class CreateScenarioPageRequest(BaseModel): 
    project_id: str
    scenario_id: str
    page_id: str
    order_no: str

class UpdateScenarioPageOrderRequest(BaseModel): 
    pages: Dict[str, int]

class ScenarioPageResponse(BaseModel):
    id: str
    order_no: int 
    name: str

class QueryScenarioPageResponse(BaseModel):
    pages: List[ScenarioPageResponse]