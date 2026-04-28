from pathlib import Path
import re
import sys
import pandas as pd
import joblib

from services.embeddingtransformer import EmbeddingTransformer

sys.modules['__main__'].EmbeddingTransformer = EmbeddingTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
MODELS_DIR = BASE_DIR / "models"

VER = 3
model = joblib.load(MODELS_DIR / f"topic_model{VER}.pkl")
label_encoder = joblib.load(MODELS_DIR / "label_encoder_topic.pkl")

def clean_text(x):
    x = str(x)
    x = re.sub(r"-{3,}", " ", x)
    x = re.sub(r"\S+@\S+", " ", x)
    x = re.sub(r"\bDoD\s*#?\d+\b", " ", x)
    x = re.sub(r"\".*?\"", " ", x)
    x = re.sub(r"[^\w\s.,!?'/]", " ", x)
    x = re.sub(r"\s+", " ", x)

    return x.strip().lower()

def topic_predict(text:str):
    text = clean_text(text)
    prediction = model.predict(pd.Series([text]))
    label = label_encoder.inverse_transform([int(prediction[0])])[0]
    return {
        "pred_id": int(prediction[0]),
        "pred_label": label,
    }

print(type(model))
print(model)