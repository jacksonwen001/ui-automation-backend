import datetime
from pydantic import BaseModel


class CreateScenarioRequest(BaseModel):
    name: str
  
class UpdateScenarioRequest(BaseModel):
    name: str

class QueryScenarioResponse(BaseModel): 
    id: str
    name: str
    created_at: datetime.datetime


class QueryScenarioRequest:
    def __init__(self, name: str|None = None, current: int = 1, size: int = 10) -> None:
        self.name = name
        self.current = current
        self.size = size

