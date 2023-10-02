from sys import displayhook
import pandas as pd
 
df1 = pd.read_csv("Iris.csv")
print("Original DataFrame is:")
displayhook(df1)

df2 = df1.loc[df1['SepalLengthCm'] >= 6]
print("Flowers with morethan 6 cm sepal length are:")
displayhook(df2)
df2.to_csv('iris2.csv')
