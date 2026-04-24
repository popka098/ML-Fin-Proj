from fastapi import APIRouter

from auth.users import fastapi_users
from auth.schemas import UserCreate, UserRead
from auth.backend import auth_backend

router = APIRouter(prefix="/auth", tags=["auth"])

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt"
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
