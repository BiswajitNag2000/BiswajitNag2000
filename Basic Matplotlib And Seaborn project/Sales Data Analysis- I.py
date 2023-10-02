import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")
print(df.head())
print(df.isnull().sum())
print(df.info())
plt.figure(figsize=(16, 8))
plt.bar('Category', 'Sales', data=df)
plt.ylabel('Sales')
plt.xlabel('Categories')
plt.title('Total Sales for each Category of Products', fontsize=20)
plt.show()
df_state_dealings = df.groupby('State')['Sales'].count().sort_values(ascending = False).plot.bar(figsize = (15, 5))
plt.ylabel('Deals')
plt.xlabel('American States')
plt.title('Total Number of Deals in Each American State', fontsize = 20)
plt.show()
