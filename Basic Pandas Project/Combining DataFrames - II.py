import pandas as pd
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue','John', 'Daisy'],'department': ['Accounting', 'Engineering', 'Engineering', 'HR','Engineering', 'Engineering']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue', 'John', 'Daisy'],'joining_date': [2004, 2008, 2012, 2022, 2021, 2020]})
df3 = pd.merge(df1, df2)
print(df3)
df4= df3.loc[df3['department'] == 'Engineering']
from IPython.core.display_functions import display
display(df4)