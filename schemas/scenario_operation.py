from typing import Dict, List
from pydantic import BaseModel

class CreateScenarioOperationRequest(BaseModel): 
    project_id: str
    scenario_page_id: str 
    operation_id: str 
    order_no: str

class ScenarioOperationResponse(BaseModel): 
    id:str
    project_id: str
    scenario_page_id: str 
    operation_id: str 
    order_no: str
  
class UpdateOperationOrderRequest(BaseModel):
    operations: Dict[str, int]


class QueryScenarioOperationsResponse(BaseModel):
    operations: List[ScenarioOperationResponse]

class QueryScenarioOperationRequest:
    def __init__(self, scenario_page_id: str) -> None:
        self.scenario_page_id = scenario_page_id 
    