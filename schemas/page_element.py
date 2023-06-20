
from typing import List
from pydantic import BaseModel


class QueryElementRequest:
    def __init__(self, page_id: str, current: int = 0, size: int = 10) -> None:
        self.page_id = page_id
        self.current = current
        self.size = size
    

class UpdateElementRequest(BaseModel): 
    name: str
    selector: str
    target: str

class CreateElementRequest(BaseModel): 
    name: str
    selector: str
    target: str

class QueryElementResponse(BaseModel):
    id: str
    name: str
    selector: str
    target: str

class QueryElementsResponse(BaseModel):
    total: int
    elements: List[QueryElementResponse]