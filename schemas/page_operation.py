import datetime
from typing import List
from pydantic import BaseModel


class QueryPageOperationRequest: 
    def __init__(self, page_id: str, current: int = 1, size: int = 10) -> None:
        self.page_id = page_id
        self.current = current
        self.size = size

class QueryPageOperationResponse(BaseModel): 
    id: str
    project_id: str
    page_id: str
    name: str
    created_at: datetime.datetime

class QueryPageOperationsResponse(BaseModel):
    total: int 
    operations: List[QueryPageOperationResponse]

class CreatePageOperationRequest(BaseModel): 
    project_id: str
    page_id: str
    name: str

class UpdatePageOperationRequest(BaseModel): 
    name: str