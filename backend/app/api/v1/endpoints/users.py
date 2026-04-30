from fastapi import APIRouter, Depends, HTTPException
from schemas.user import UserRead
from api.deps import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def get_me(user = Depends(get_current_user)) -> UserRead:
    return user
