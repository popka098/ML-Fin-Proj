from fastapi import APIRouter, Depends, HTTPException
from auth.users import fastapi_users

router = APIRouter(prefix="/users")
current_user = fastapi_users.current_user()

@router.get("/me")
def get_me(user=Depends(current_user)):
    return user
