from pathlib import Path
import re
import sys
import pandas as pd
import joblib

from services.embeddingtransformer import EmbeddingTransformer

sys.modules['__main__'].EmbeddingTransformer = EmbeddingTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
MODELS_DIR = BASE_DIR / "models"

VER = ""
model = joblib.load(MODELS_DIR / f"topic_model{VER}.pkl")

IDX2WORD = {
    0: 'alt.atheism',
    1: 'comp.graphics',
    2: 'comp.os.ms-windows.misc',
    3: 'comp.sys.ibm.pc.hardware',
    4: 'comp.sys.mac.hardware',
    5: 'comp.windows.x',
    6: 'misc.forsale',
    7: 'rec.autos',
    8: 'rec.motorcycles',
    9: 'rec.sport.baseball',
    10: 'rec.sport.hockey',
    11: 'sci.crypt',
    13: 'sci.med',
    12: 'sci.electronics',
    14: 'sci.space',
    15: 'soc.religion.christian',
    16: 'talk.politics.guns',
    17: 'talk.politics.mideast',
    18: 'talk.politics.misc',
    19: 'talk.religion.misc',
}

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
    return {
        "pred_id": int(prediction[0]),
        "pred_label": IDX2WORD[int(prediction[0])],
    }