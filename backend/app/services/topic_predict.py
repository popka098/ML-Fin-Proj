from pathlib import Path
import re
import sys
import pandas as pd
import joblib

from services.embeddingtransformer import EmbeddingTransformer

sys.modules['__main__'].EmbeddingTransformer = EmbeddingTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# MODELS_DIR = BASE_DIR / "models"
MODELS_DIR = Path("/app/models")

VER = ""
model = joblib.load(MODELS_DIR / f"topic_model{VER}.pkl")

IDX2WORD = {
    1: "Society & Culture",
    2: "Science & Mathematics",
    3: "Health",
    4: "Education & Reference",
    5: "Computers & Internet",
    6: "Sports",
    7: "Business & Finance",
    8: "Entertainment & Music",
    9: "Family & Relationships",
    10: "Politics & Government",
}

def clean_text(x):
    if x is None:
        x = ""

    x = str(x)
    x = re.sub(r"\s+", " ", x)

    return x.strip()

def topic_predict(text:str):
    text = clean_text(text)
    prediction = model.predict(pd.Series([text]))
    return {
        "topic_pred_id": int(prediction[0]),
        "topic_pred_label": IDX2WORD[int(prediction[0])],
    }