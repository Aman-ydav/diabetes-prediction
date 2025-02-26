import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE
import joblib
from xgboost import XGBClassifier


df = pd.read_csv('Backend/datasets/diabetes.csv')
df = df.drop(columns=['AnyHealthcare', 'NoDocbcCost', 'CholCheck', 'Sex', 'MentHlth', 'Smoker', 'HvyAlcoholConsump', 'Veggies', 'Fruits', 'Education', 'Income'])
X = df.drop('Diabetes_binary', axis=1)
y = df['Diabetes_binary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

smote = SMOTE(random_state=42, sampling_strategy=0.7)
X_train, y_train = smote.fit_resample(X_train, y_train)

model: XGBClassifier = XGBClassifier(
    scale_pos_weight=2.8,
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    colsample_bytree=0.8,
    subsample=0.8,
    random_state=42
)
# model = LogisticRegression(max_iter=1000, )

model.fit(X_train, y_train)

y_probs = model.predict_proba(X_test)[:,1] 

threshold = 0.69 
y_pred_new = (y_probs >= threshold).astype(int)
y_pred = model.predict(X_test)

joblib.dump(model, 'Backend/xgb_model.pkl')