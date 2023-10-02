import pandas as pd
df1 = pd.DataFrame({'name': ['Shubham', 'Adin', 'Rahul'],'age': [23, 28, 30]})
df2 = pd.DataFrame({'name': ['Amrit', 'Shubham', 'Ali'],'age':[20, 23, 28]})
print(df1)
print(df2)
df3 = pd.concat([df1, df2]).drop_duplicates()
df3 = df3.reset_index(drop=True)
print(df3)