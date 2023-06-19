from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    password: str
  
class UpdateUserEmailRequest(BaseModel):
    email: str
    new_email: str
    password: str

