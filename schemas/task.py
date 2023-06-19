from pydantic import BaseModel


class ExecuteRequest(BaseModel):
    suite_id: str
    browser: str
    browser_version: str