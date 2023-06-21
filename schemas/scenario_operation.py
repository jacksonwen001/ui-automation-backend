from ast import Dict, List
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
    def __init__(self, page_id: str) -> None:
        self.page_id = page_id 
    