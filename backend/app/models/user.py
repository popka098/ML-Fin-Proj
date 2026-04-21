from models.basemodel import BaseModel
from pydantic import EmailStr
from sqlmodel import Field, SQLModel

class User(BaseModel, table=True):
    username : str = Field(
        min_length=3,
        max_length=64,
        unique=True,
        index=True
    )
    email : EmailStr = Field(
        unique=True,
    )
    is_staff : bool = Field(
        default=False,
    )
    is_admin : bool = Field(
        default=False,
    )