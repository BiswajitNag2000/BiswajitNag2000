import pandas as pd
df = pd.read_csv("C:\\Users\\nagbi\\OneDrive\\Desktop\\DATA SCIENCE\\DIY_DATA_ SET\\diy_dataset_Day_13\\titanic.csv")
df2= df.dropna()
df2.head(10)
print(df.head())
print(df.isnull().sum())
print(df2.isnull())