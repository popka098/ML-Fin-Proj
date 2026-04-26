from auth.users import fastapi_users
from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import AsyncSessionLocal
from auth.db import get_user_db
from auth.manager import UserManager

current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(superuser=True)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session