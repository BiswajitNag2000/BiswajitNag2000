import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("SampleSuperstore.csv")
print(df.head())
attributes = ['Sales','Quantity','Discount','Profit']
corr_mat = df.corr()
print(corr_mat)
plt.subplots(figsize=(12,9))
sns.heatmap(corr_mat,annot=True)
plt.title('Correlation between Postal code, Quantity, Sales, Discount, and Profit ', fontsize = 20)
plt.show()
