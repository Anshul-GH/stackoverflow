import os
# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

import pandas as pd

df = pd.read_csv(os.path.join(__location__) + '/61737615_input.csv')

a_list = list(set(df.a))
# print(a_list)

df_meta = pd.DataFrame(columns=['key', 'c_mode'])
# df_meta.columns = ['key', 'c_mode']

meta = [] 

for val in a_list:
    columns = df_meta.columns
    data = [val, df.loc[df.a == val].c.mode()]
    zipped = dict(zip(columns, data))
    meta.append(zipped)

print(meta)

df_meta = df_meta.append(meta, ignore_index=True)
print(df_meta.columns)

