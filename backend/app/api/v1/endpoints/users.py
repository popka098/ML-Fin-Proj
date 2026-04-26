from fastapi import APIRouter, Depends, HTTPException
from auth.models import User
from api.deps import current_user

router = APIRouter(prefix="/users")

@router.get("/me")
def get_me(user: User = Depends(current_user)):
    return user
