import pandas as pd

file = 'wheat'
df = pd.read_csv(f'Backend/datasets/{file}_final.csv')
corr = df[['yield', 'price', 'rain_index']].corr()

print(corr)