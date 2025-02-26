import joblib
import numpy as np
import pandas as pd

model = joblib.load('Backend/xgb_model.pkl')

def model_predict(data: np.array):
    df = pd.DataFrame(data, columns=['HighBP', 'HighChol', 'BMI' ,'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'GenHlth', 'PhysHlth' ,'DiffWalk', 'Age'])
    print(df)
    return model.predict(df)

print(model_predict(np.array([[1,0, 20, 0, 0, 5, 5, 1, 0, 20]])))