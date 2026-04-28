from pathlib import Path
import pandas as pd
import joblib

from services.embeddingtransformer import EmbeddingTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
MODELS_DIR = BASE_DIR / "models"

VER = 3
model = joblib.load(MODELS_DIR / f"topic_model{VER}.pkl")
label_encoder = joblib.load(MODELS_DIR / "label_encoder_topic.pkl")

def sentiment_predict(text:str):
    prediction = model.predict(pd.Series([text]))[0]
    label = label_encoder.inverse_transform([prediction])[0]
    return (prediction, label)