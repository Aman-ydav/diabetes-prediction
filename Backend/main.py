from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("price_model.pkl")

# Define Request Model
class PredictionRequest(BaseModel):
    state: str
    crop: str
    month: int
    year: int

# Encode categorical values
state_mapping = {"Maharashtra": 0, "Uttar Pradesh": 1}
crop_mapping = {"potato": 0, "onion": 1, "rice": 2, "wheat": 3, "pulses": 4}

@app.post("/predict")
def predict_price(request: PredictionRequest):
    try:
        state_code = state_mapping.get(request.state, -1)
        crop_code = crop_mapping.get(request.crop, -1)

        if state_code == -1 or crop_code == -1:
            return {"error": "Invalid input"}

        input_data = np.array([[state_code, crop_code, request.month, request.year]])
        predicted_price = model.predict(input_data)[0]

        return {"predicted_price": round(predicted_price, 2)}
    except Exception as e:
        return {"error": str(e)}
