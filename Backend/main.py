from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
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
    return {"prediction": 1 if prediction[0] == 1 else 0, "probability": prediction[1][0].tolist()}


# @app.get("/feature")
# def get_feature_importance():
#     # Extract feature importance
#     model = get_model()
#     booster = model.get_booster()
#     importance = booster.get_score(importance_type="weight")
    
#     # Convert to sorted list
#     sorted_importance = sorted(importance.items(), key=lambda x: x[1], reverse=True)

#     # Convert to JSON-friendly format
#     feature_data = [{"feature": feature, "importance": score} for feature, score in sorted_importance]
    
#     return {"feature": feature_data}

@app.get("/image")
async def get_image():
    image_path = "preprocessing/importance.png"  # Replace with the actual image path
    return FileResponse(image_path, media_type="image/jpeg")