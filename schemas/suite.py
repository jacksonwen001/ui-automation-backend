import datetime
from typing import List
from pydantic import BaseModel


class CreateSuiteRequest(BaseModel):
    name: str
  
class UpdateSuiteRequest(BaseModel):
    name: str

class QuerySuiteResponse(BaseModel): 
    id: str
    name: str
    created_at: datetime.datetime

class QuerySuitesResponse(BaseModel): 
    total: int 
    suites: List[QuerySuiteResponse]


class QuerySuiteRequest:
    def __init__(self, name: str|None = None, current: int = 1, size: int = 10) -> None:
        self.name = name
        self.current = current
        self.size = size

