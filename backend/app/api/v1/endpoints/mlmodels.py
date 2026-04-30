from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from api.deps import get_current_user, get_db

from services.embeddingtransformer import EmbeddingTransformer
from services.sentiment_predict import sentiment_predict
from services.topic_predict import topic_predict

router = APIRouter(prefix="/mlmomdels", tags=["mlmodels"])
SENTIMENT_REQUEST_PRICE = 1
TOPIC_REQUEST_PRICE = 1

@router.get("/sentiment")
async def get_sentiment(
    text: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if user.crystals < SENTIMENT_REQUEST_PRICE:
        raise HTTPException(
            status_code=400,
            detail="Not enough crystals"
        )

    user.crystals -= SENTIMENT_REQUEST_PRICE
    await db.commit()
    await db.refresh(user)

    res = sentiment_predict(text)
    return res | {"crystals": user.crystals}

@router.get("/topic")
async def get_topic(
    text: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if user.crystals < TOPIC_REQUEST_PRICE:
        raise HTTPException(
            status_code=400,
            detail="Not enough crystals"
        )

    user.crystals -= TOPIC_REQUEST_PRICE
    await db.commit()
    await db.refresh(user)

    res = topic_predict(text)
    return res | {"crystals": user.crystals}

@router.get("/all")
async def get_all_preds(
    text: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    total_price = sum([
        SENTIMENT_REQUEST_PRICE,
        TOPIC_REQUEST_PRICE,
    ])
    if user.crystals < total_price:
        raise HTTPException(
            status_code=400,
            detail="Not enough crystals"
        )

    user.crystals -= total_price
    await db.commit()
    await db.refresh(user)

    res_sentiment = sentiment_predict(text)
    res_topic = topic_predict(text)
    return res_sentiment | res_topic | {"crystals": user.crystals}

