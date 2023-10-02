import numpy as np
import pandas as pd
from IPython.display import display
df = pd.read_csv("big_bang_theory_episodes.csv").fillna(np.nan)
result = df.groupby('directed_by')
display(df)
display(result.first())
display(result.get_group("Mark Cendrowski"))
