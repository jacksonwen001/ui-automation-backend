from pydantic import BaseModel


class QueryPageOperationRequest: 
    def __init__(self) -> None:
        pass


class CreatePageOperationRequest(BaseModel): pass
class UpdatePageOperationRequest(BaseModel): pass