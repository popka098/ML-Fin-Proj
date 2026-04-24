# api/v1/router.py
from fastapi import APIRouter

from api.v1.endpoints import auth

router = APIRouter(prefix="/v1")

router.include_router(auth.router)