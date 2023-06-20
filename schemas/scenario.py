import datetime
from typing import List, Optional
from pydantic import BaseModel


class CreateScenarioRequest(BaseModel):
    project_id: str
    name: str
    description: Optional[str]
  
class UpdateScenarioRequest(BaseModel):
    name: str
    description: str

class QueryScenarioResponse(BaseModel): 
    id: str
    name: str
    description: Optional[str]
    created_at: datetime.datetime

class QueryScenariosResponse(BaseModel):
    total: int
    scenarios: List[QueryScenarioResponse]

class QueryScenarioRequest:
    def __init__(self, project_id: str, name: Optional[str]= None, current: int = 1, size: int = 10) -> None:
        self.project_id = project_id
        self.name = name
        self.current = current
        self.size = size

