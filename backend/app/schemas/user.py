from sqlmodel import Field
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)

class UserLogin(BaseModel):
    email: str
    password: str