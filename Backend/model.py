from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv('Backend/datasets/potato_final.csv')

X = df[["yield", "rain_index"]]
y = df['price']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "simple_model.pkl")