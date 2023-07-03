
import datetime
from typing import List
from pydantic import BaseModel

class CreateProjectRequest(BaseModel):
    name: str

class UpdateProjectrequest(BaseModel):
    name: str

class QueryProjectRequest:
    def __init__(self, name: str|None = None, current: int = 1, size: int = 10) -> None:
        self.name = name
        self.current = current
        self.size = size

class ProjectResponse(BaseModel):
    id: str
    name: str
    created_at: datetime.datetime

class QueryProjectsResponse(BaseModel):
    total: int
    projects: List[ProjectResponse] 

