import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Backend/datasets/diabetes.csv')
corr_matrix = df.corr()
print(corr_matrix)
df = df.drop(columns=['AnyHealthcare', 'NoDocbcCost', 'CholCheck', 'Sex', 'MentHlth', 'Smoker', 'HvyAlcoholConsump', 'Veggies', 'Fruits', 'Education', 'Income'])
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()