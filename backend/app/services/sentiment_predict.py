from pathlib import Path
import pandas as pd
import joblib

from services.embeddingtransformer import EmbeddingTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
MODELS_DIR = BASE_DIR / "models"
IDX2WORD = {
    1: "Positive",
    2: "Neutral",
    3: "Negative",
}

model = joblib.load(MODELS_DIR / "sentiment_model.pkl")

def sentiment_predict(text:str) -> tuple[int, str]:
    prediction = model.predict(pd.Series([text]))[0]
    return (prediction, IDX2WORD[prediction])