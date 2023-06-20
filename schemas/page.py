import datetime
from typing import List
from pydantic import BaseModel


class CreatePageRequest(BaseModel):
    project_id: str
    name: str
  
class UpdatePageRequest(BaseModel):
    name: str

class QueryPageResponse(BaseModel): 
    id: str
    project_id: str
    name: str
    created_at: datetime.datetime

class QueryPagesResponse(BaseModel): 
    total: int
    pages: List[QueryPageResponse]

class QueryPageRequest:
    def __init__(self, project_id: str, name: str|None = None, current: int = 1, size: int = 10) -> None:
        self.name = name
        self.project_id = project_id
        self.current = current
        self.size = size

