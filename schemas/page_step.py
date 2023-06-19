from typing import List, Optional
from pydantic import BaseModel


class QueryPageStepRequest: 
    def __init__(self) -> None:
        pass


class CreatePageStepRequest(BaseModel): 
    project_id: str
    page_id: str
    operation_id: str
    command: str 
    element_id: Optional[str]
    value: Optional[str]

class QueryPageStepResponse(BaseModel): 
    id: str
    command: str
    target: str
    value: str 

class QueryPageStepsResponse(BaseModel): 
    total: int
    steps: List[QueryPageStepResponse]

class UpdatePageStepRequest(BaseModel): pass
class UpdatePageStepOrderRequest(BaseModel): pass