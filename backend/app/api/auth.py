# api/auth.py
import datetime as dt

from fastapi import APIRouter, Depends, HTTPException, Request, Response
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
    response: Response,
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

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False, #!!! True в прод
        samesite="lax",
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

@router.post("/refresh")
async def refresh(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise HTTPException(401, "No refresh token")

    result = await db.execute(
        select(RefreshToken).where(RefreshToken.token == refresh_token)
    )
    token_entry = result.scalar_one_or_none()

    if not token_entry:
        raise HTTPException(401, "Invalid refresh token")

    if token_entry.expires_at.replace(tzinfo=dt.timezone.utc) < dt.datetime.now(dt.timezone.utc):
        raise HTTPException(401, "Refresh token expired")

    await db.delete(token_entry)

    new_refresh_token = create_refresh_token()
    db.add(RefreshToken(
        user_id=token_entry.user_id,
        token=new_refresh_token,
        expires_at=dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    ))

    await db.commit()

    response.set_cookie(
        key="refresh_token",
        value=new_refresh_token,
        httponly=True,
        secure=False, #!!! True в прод
        samesite="lax",
    )

    access_token = create_access_token({"sub": str(token_entry.user_id)})

    return {"access_token": access_token}

@router.post("/logout")
async def logout(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    refresh_token = request.cookies.get("refresh_token")
    if refresh_token:
        result = await db.execute(
            select(RefreshToken).where(RefreshToken.token == refresh_token)
        )
        token_entry = result.scalar_one_or_none()

        if token_entry:
            await db.delete(token_entry)
            await db.commit()
    response.delete_cookie("refresh_token")

    return {"msg": "Logged out"}