import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\nagbi\\OneDrive\\Desktop\\diy_dataset_Day_12\\player.csv") 
print (df)

df.drop(df[df['100s'] == 0].index, inplace = True)

df["name"] = df["name"].replace(to_replace = "V Kohli",value ="Virat Kohli")

df["not batting "] = df["matches"] - df["innings"]

df["not batting "] = df["matches"] - df["innings"]
print(df)