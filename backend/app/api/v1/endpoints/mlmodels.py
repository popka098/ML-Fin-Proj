from fastapi import APIRouter, Depends, HTTPException
from api.deps import get_current_user

from services.embeddingtransformer import EmbeddingTransformer
from services.sentiment_predict import sentiment_predict
from services.topic_predict import topic_predict

router = APIRouter(prefix="/mlmomdels")

@router.get("/sentiment")
def get_sentiment(text: str):
    res = sentiment_predict(text)
    return res

@router.get("/topic")
def get_topic(text: str):
    res = topic_predict(text)
    return res

@router.get("/all")
def get_all_preds(text: str):
    res_sentiment = sentiment_predict(text)
    res_topic = topic_predict(text)
    return {
        "sentiment_id": res_sentiment["pred_id"],
        "sentiment_label": res_sentiment["pred_label"],
        "topic_id": res_topic["pred_id"],
        "topic_label": res_topic["pred_label"],
    }

