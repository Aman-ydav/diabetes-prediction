import pandas as pd

def csv_generator(f1, f2):
    df1 = pd.read_csv(f1)
    df2 = pd.read_csv(f2)
    rain_series = pd.read_csv('Backend/datasets/rain_series.csv')

    merged = df1.merge(df2, on='month')
    merged = merged.merge(rain_series, on='month')
    merged.columns = ['month', 'price', 'yield', 'rain_index']
    return merged

file='wheat'
res = csv_generator(f'Backend/datasets/raw_data/{file}_price.csv', f'Backend/datasets/raw_data/{file}_yield.csv')
res.to_csv(f'Backend/datasets/{file}_final.csv', index=False)
