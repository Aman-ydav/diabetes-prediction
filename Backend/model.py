import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Sample dataset with historical data
data = {
    "state": ["State1", "State1", "State2", "State2"],
    "crop": ["potato", "onion", "potato", "onion"],
    "month": [1, 2, 1, 2],
    "year": [2023, 2023, 2023, 2023],
    "prev_yield": [20, 25, 22, 24],  # Yield in tons
    "prev_price": [30, 40, 35, 38],  # Price in currency units
    "weather_factor": [0.9, 0.8, 1.0, 0.85],  # Weather impact
    "price": [32, 42, 36, 39]  # Actual future price
}

df = pd.DataFrame(data)

# Selecting features and target variable
X = df[["prev_yield", "prev_price", "weather_factor"]]
y = df["price"]

# Training Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Save trained model
joblib.dump(model, "price_model.pkl")

print("Model trained and saved successfully!")
