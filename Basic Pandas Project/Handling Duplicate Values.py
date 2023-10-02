import pandas as pd
df = pd.read_csv("C:\\Users\\nagbi\\OneDrive\\Desktop\\DATA SCIENCE\\DIY_DATA_ SET\\diy_dataset_Day_13\\titanic.csv")
df2 = df.drop_duplicates(subset ="Ticket")
print(df)
print(df.isnull().sum())
print(df2)