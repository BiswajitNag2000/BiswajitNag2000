import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\nagbi\\OneDrive\\Desktop\\starbucks_drinkMenu_expanded.csv")
print(df.head())
df.isnull().sum()
df.dropna()
plt.figure(figsize=(10,8))
bar_cal = sns.barplot(x="Calories", y="Beverage_category", data=df).set(title="Which of the starbucks drinks have highest calories? ")
plt.show()
