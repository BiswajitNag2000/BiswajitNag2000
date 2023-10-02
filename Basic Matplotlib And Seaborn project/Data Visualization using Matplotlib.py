import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\nagbi\\OneDrive\\Desktop\\netflix_titles.csv")
print (df.head())
df.info()

plt.figure(figsize=(14, 7))
labels=['TV Show', 'Movie']
plt.pie(df['type'].value_counts().sort_values(),labels=labels,explode=[0.1,0.1],
        autopct='%1.2f%%',colors=['blue','red'], startangle=90)
plt.title('Type of Netflix Content')
plt.axis('equal')
plt.show()

country_df = df['country'].value_counts().reset_index()
country_df = country_df[country_df['country'] /  country_df['country'].sum() > 0.01]
print(country_df)
plt.show()