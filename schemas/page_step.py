from pydantic import BaseModel


class QueryPageStepRequest: 
    def __init__(self) -> None:
        pass


class CreatePageStepRequest(BaseModel): pass
class UpdatePageStepRequest(BaseModel): pass