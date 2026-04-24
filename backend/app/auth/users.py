from fastapi import Depends
from fastapi_users import FastAPIUsers
from app.auth.models import User
from app.auth.schemas import UserRead, UserCreate
from app.auth.manager import UserManager
from app.auth.backend import auth_backend
from app.auth.db import get_user_db

def get_user_manager(user_db=Depends(get_user_db)):
    yield

fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
)