from fastapi import APIRouter, Depends, HTTPException
from api.deps import get_current_user

router = APIRouter(prefix="/users")

@router.get("/me")
def get_me(user = Depends(get_current_user)):
    return user
