from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI()

# Load trained model
model = joblib.load("price_model.pkl")

# Define request format
class PredictionRequest(BaseModel):
    state: str
    crop: str
    month: int
    year: int
    prev_yield: float
    prev_price: float
    weather_factor: float

# API Endpoint for Prediction
@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = model.predict([[request.prev_yield, request.prev_price, request.weather_factor]])
    return {"predicted_price": round(prediction[0], 2)}

# Run with: uvicorn main:app --reload
