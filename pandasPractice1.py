import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

file_path = 'D:\downloads\python-data-analysis-master\python-data-analysis-master\data\drinks.csv'
drinks = pd.read_csv(file_path)

drinksDataDescribe = pd.DataFrame(drinks.describe())

# corr = drinks[['beer_servings', 'wine_servings']].corr(method = 'pearson')
# print(corr)

corr = drinks.corr(method='pearson')
print(corr)
cols_view = ['beer', 'spirit', 'wine', 'alcohol']
hm = sbn.heatmap(corr.values,
                 cbar=True,
                 yticklabels=cols_view,
                 xticklabels=cols_view)

plt.tight_layout()
plt.show()

sbn.set(style='whitegrid', context='notebook')
sbn.pairplot(drinks, height=2.5)
plt.show()