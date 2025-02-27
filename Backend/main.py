from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from model_functions import model_predict


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictRequest(BaseModel):
    highBP: int
    highChol: int
    bmi: float
    stroke: int
    heartDisease: int
    physActivity: int
    genHlth: int
    physHlth: int
    diffWalk: int
    age: int


@app.post("/predict")
async def predict(data: PredictRequest):
    features = np.array([[data.highBP, data.highChol, data.bmi, data.stroke, 
                          data.heartDisease, data.physActivity, data.genHlth, 
                          data.physHlth, data.diffWalk, data.age]])
    
    prediction = model_predict(features)
    print(prediction)
    return {"prediction": 1 if prediction[0] == 1 else 0}
