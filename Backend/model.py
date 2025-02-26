import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("datasets/prediction.csv")

# Select features and target variable
X = df[["highBP", "highChol", "bmi", "stroke", "heartDisease", "physActivity", "genHlth", "physHlth", "diffWalk", "age"]]
y = df["diabetes_risk"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Calculate accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Model Accuracy: {accuracy:.4f}")  # Print accuracy with 4 decimal places
print(classification_report(y_test,y_pred))
# Save the trained model
joblib.dump(model, "lifestyle_model.pkl")

print("Model training complete. Model saved as 'lifestyle_model.pkl'.")
