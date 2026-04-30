from pathlib import Path
import sys
import pandas as pd
import joblib

from services.embeddingtransformer import EmbeddingTransformer

sys.modules['__main__'].EmbeddingTransformer = EmbeddingTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
MODELS_DIR = BASE_DIR / "models"
IDX2WORD = {
    1: "Positive",
    2: "Neutral",
    3: "Negative",
}

model = joblib.load(MODELS_DIR / "sentiment_model.pkl")

def sentiment_predict(text:str):
    prediction = model.predict(pd.Series([text]))
    return {
        "sentiment_pred_id": int(prediction[0]),
        "sentiment_pred_label": IDX2WORD[int(prediction[0])],
    }