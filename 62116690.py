import pandas as pd
import re

df = pd.read_csv('62116690.csv')

# df['Gender'] = df['Gender'].astype(str)

df['Gender'] = [val for val in df if ]
#df['Gender'].str.strip().replace(r'\W+', 'NA', regex=True)

print(df['Gender'].value_counts())
print(df.info())