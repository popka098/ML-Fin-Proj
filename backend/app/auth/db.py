from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import AsyncSessionLocal
from fastapi_users.db import SQLAlchemyUserDatabase
from auth.models import User
# from api.deps import get_db

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)