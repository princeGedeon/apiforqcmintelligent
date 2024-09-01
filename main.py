from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from ludwig.api import LudwigModel

from utils.inference import generate_qcm_with_model
from utils.parsers import parse_questions
# Définir le modèle de requête pour l'API
class LyricsRequest(BaseModel):
    lyrics: str
    default_format: bool = False



app = FastAPI()
# Charger le modèle Ludwig au démarrage de l'application
@app.on_event("startup")
def load_model():
    global ludwig_model
    ludwig_model = LudwigModel.load("./models/ghostprince")


# Définir le endpoint pour traiter les lyrics
@app.post("/generate-qcm")
def generate_qcm(request: LyricsRequest):
    try:
        qcm = generate_qcm_with_model(ludwig_model, request.lyrics, request.default_format)
        return {"qcm": qcm}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
