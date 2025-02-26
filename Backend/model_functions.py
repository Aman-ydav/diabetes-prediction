import joblib
import numpy as np
import pandas as pd

model = joblib.load('xgb_model.pkl')

def model_predict(data: np.array):
    df = pd.DataFrame(data, columns=['HighBP', 'HighChol', 'BMI' ,'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'GenHlth', 'PhysHlth' ,'DiffWalk', 'Age'])
    print(df)
    return model.predict(df)