from fastapi import Depends
from fastapi_users import FastAPIUsers
from auth.models import User
from auth.schemas import UserRead, UserCreate
from auth.manager import UserManager
from auth.backend import auth_backend
from auth.db import get_user_db

def get_user_manager(user_db=Depends(get_user_db)):
    yield

fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
)