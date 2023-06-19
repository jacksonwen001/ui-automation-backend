
from pydantic import BaseModel


class QueryElementRequest:
    def __init__(self) -> None:
        pass
    

class UpdateElementRequest(BaseModel): pass
class CreateElementRequest(BaseModel): pass