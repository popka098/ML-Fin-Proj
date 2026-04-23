from fastapi import APIRouter, Depends, HTTPException

from sqlmodel import Session, select
from db.base import get_session

from models.user import User
from schemas.user import UserCreate, UserRead, UserUpdate

from typing import Annotated

router = APIRouter(prefix="/users")
SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/", response_model=UserCreate)
def create_user(user: UserCreate, session: SessionDep) -> UserRead:
    new_user = User.model_validate(user)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.get("/", response_model=list[UserRead])
def read_all_users(session: SessionDep) -> list[UserRead]:
    users = session.exec(select(User)).all()
    return users

@router.get("/{id}", response_model=UserRead)
def read_all_users(id: int, session: SessionDep) -> UserRead:
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user