import pandas as pd

'''
Id	A	B	C
1	45	78	67
2	67	89	76
3	67	94	56
4	26	78	56
5	38 	67	75
'''

df = pd.read_clipboard()

print(df)
print(df.columns)