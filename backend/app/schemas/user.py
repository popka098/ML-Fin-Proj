from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class UserCreate(SQLModel):
    username : str = Field(
        min_length=3,
        max_length=64,
        unique=True,
    )
    email : EmailStr = Field(
        unique=True
    )

class UserUpdate(UserCreate):
    ...

class UserRead(UserCreate):
    id : int
    is_staff : bool
    is_admin : bool