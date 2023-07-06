import datetime
from typing import List
from pydantic import BaseModel


class CreatePageRequest(BaseModel):
    project_id: str
    name: str
  
class UpdatePageRequest(BaseModel):
    name: str

class PageResponse(BaseModel): 
    id: str
    project_id: str
    name: str
    created_at: datetime.datetime

class QueryPagesResponse(BaseModel): 
    total: int
    pages: List[PageResponse]

class PageUsageResponse(BaseModel):
    scenario_id: str
    scenario_page_id: str
    name: str

class QueryPageUsagesResponse(BaseModel):
    used: bool
    scenarios: List[PageUsageResponse]

class QueryPageRequest:
    def __init__(self, project_id: str, name: str|None = None, current: int = 1, size: int = 10) -> None:
        self.name = name
        self.project_id = project_id
        self.current = current
        self.size = size

