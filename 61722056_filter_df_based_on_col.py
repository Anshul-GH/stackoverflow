import pandas as pd
import os

# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


df = pd.read_csv(os.path.join(__location__,'61722056_input.csv'))
# print(df)

df_upper = df.loc[df.PERCENTCHANGE <= 30]
df_lower = df.loc[df.PERCENTCHANGE > 30]


df_required = pd.concat([df_upper.tail(1), df_lower])
