import matplotlib.pyplot as plt
import pandas as pd


potato = pd.read_csv('Backend/datasets/potato_final.csv')

plt.scatter(potato['yield'], potato['price'])
plt.xlabel('Yield (tons)')
plt.ylabel('Price (currency units)')
plt.title('Potato Price vs Yield')
plt.show()