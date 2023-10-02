import pandas as pd

ap = pd.read_csv("big_bang_theory_episodes.csv")
result = ap.groupby(['directed_by', 'written_by'])['us_viewers'].mean()
print(ap)
print(result)
