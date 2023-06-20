from typing import Dict, List, Optional
from pydantic import BaseModel


class QueryPageStepRequest: 
    def __init__(self, operation_id: str) -> None:
        self.operation_id = operation_id


class CreatePageStepRequest(BaseModel): 
    project_id: str
    page_id: str
    operation_id: str
    command: str 
    element_id: Optional[str]
    value: Optional[str]
    order_no: int

class QueryPageStepResponse(BaseModel): 
    id: str
    operation_id: str
    command: str
    element_id: Optional[str]
    element_name: Optional[str]
    value: str 
    order_no: str

class QueryPageStepsResponse(BaseModel): 
    total: int
    steps: List[QueryPageStepResponse]

class UpdatePageStepRequest(BaseModel): pass
class UpdatePageStepOrderRequest(BaseModel): 
    steps: Dict[str, int]