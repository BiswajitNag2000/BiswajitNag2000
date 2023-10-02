import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\nagbi\\OneDrive\\Desktop\\diy_dataset_Day_12\\player.csv") 
print (df)
filtered_values = df[(df['innings']>150) & (df['100s']>2) & (df['50s']>35)]
print (filtered_values)