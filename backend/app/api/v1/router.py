# api/v1/router.py
from fastapi import APIRouter

from api.v1.endpoints import  users
from api.v1.endpoints import mlmodels

router = APIRouter(prefix="/v1")

router.include_router(users.router)
router.include_router(mlmodels.router)