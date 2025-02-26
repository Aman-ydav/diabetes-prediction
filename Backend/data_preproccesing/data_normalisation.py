import pandas as pd
from sklearn.preprocessing import StandardScaler

file = 'potato'
df = pd.read_csv(f'Backend/datasets/{file}_final.csv')

num_cols = ['price', 'yield', 'rain_index']

def standardize(df, cols):
    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df

df = standardize(df, num_cols)
df.to_csv(f'Backend/datasets/{file}_final.csv', index=False)
print(df.head())