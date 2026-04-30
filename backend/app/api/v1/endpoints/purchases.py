from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from api.deps import get_current_user, get_db

router = APIRouter(prefix="/purchases")

@router.post("/add-crystals")
async def add_crystals(
    amount: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if amount < 1:
        raise HTTPException(400, detail="Bad credentials")

    user.crystals += amount
    await db.commit()
    await db.refresh(user)

    return {"msg": "Success", "crystals": user.crystals}