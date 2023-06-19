import datetime
from pydantic import BaseModel


class CreatePageRequest(BaseModel):
    name: str
  
class UpdatePageRequest(BaseModel):
    name: str

class QueryPageResponse(BaseModel): 
    id: str
    name: str
    created_at: datetime.datetime


class QueryPageRequest:
    def __init__(self, name: str|None = None, current: int = 1, size: int = 10) -> None:
        self.name = name
        self.current = current
        self.size = size

