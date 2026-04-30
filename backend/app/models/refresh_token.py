from sqlmodel import SQLModel, Field
import datetime as dt

class RefreshToken(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    token: str
    expires_at: dt.datetime