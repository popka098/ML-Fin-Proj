from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import AsyncSessionLocal
from auth.db import get_user_db
from auth.manager import UserManager

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session