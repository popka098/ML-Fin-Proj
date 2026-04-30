import datetime as dt

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.deps import get_db
from models.user import User
from models.refresh_token import RefreshToken
from schemas.user import UserCreate, UserLogin
from core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    REFRESH_TOKEN_EXPIRE_DAYS
)

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(
    input_user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    email = input_user.email
    password = input_user.password

    result = await db.execute(
        select(User).where(User.email == email)
    )
    existing = result.scalar_one_or_none()

    if existing:
        raise HTTPException(400, "User already exists")

    user = User(
        email=email,
        hashed_password=hash_password(password)
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    email = form_data.username
    password = form_data.password

    result = await db.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(401, "Invalid credentials")

    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token()

    db.add(RefreshToken(
        user_id=user.id,
        token=refresh_token,
        expires_at=dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    ))
    await db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }

@router.get("/refresh")
async def refresh(
    refresh_token: str,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(RefreshToken).where(RefreshToken.token == refresh_token)
    )
    token_entry = result.scalar_one_or_none()

    if not token_entry:
        raise HTTPException(401, "Invalid refresh token")

    if token_entry.expires_at < dt.datetime.now(dt.timezone.utc):
        raise HTTPException(401, "Refresh token expired")

    access_token = create_access_token({"sub": str(token_entry.user_id)})

    return {"access_token": access_token}

@router.get("/logout")
async def logout(
    refresh_token: str,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(RefreshToken).where(RefreshToken.token == refresh_token)
    )
    token_entry = result.scalar_one_or_none()

    if token_entry:
        await db.delete(token_entry)
        await db.commit()
    
    return {"msg": "Logged out successfully"}