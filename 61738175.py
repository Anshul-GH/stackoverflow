import pandas as pd

s = pd.Series(['User Location', 'Sentiment'])

df = pd.get_dummies(s, )
print(df)