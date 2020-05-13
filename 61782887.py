# '''
# Code	Names	Country
# 1	a	France
# 2	b	France
# 3	c	USA
# 4	d	Canada
# 5	e	TOTO
# 6	f	TITI
# 7	g	Corona
# '''
# import pandas as pd
# df = pd.read_clipboard(sep='\s\s+')
# # print(df)

# df2 = df.loc[~df['Names'].isin(['f','b','c'])].copy()

# print(df2)

import numpy as np
import pandas as pd

x = np.array([[1,2,3,1,2,3], 
              [4,5,np.nan,3,5,np.nan], 
              [7,8,9,4,5,6],])

df = pd.DataFrame([x[0][1], x[0][2], x[0][3]])
df = pd.DataFrame(x)
print(df)
print(df.dropna(axis=1))