import sqlalchemy
from pydantic import EmailStr
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    crystals: int = Field(
        default=50, 
        sa_column_kwargs={"server_default": sqlalchemy.text("50")}
    )