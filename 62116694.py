'''
			Test
1995-07-10	1
1995-07-02	0
1995-07-03	0
1995-07-04	1
1995-07-05	0
1995-07-06	0
1995-07-07	0
1995-07-08	0
1995-07-09	0
1995-07-10	0
1995-07-11	1
'''

'''
			Test
1995-07-10	1
1995-07-02	2
1995-07-03	3
1995-07-04	4
1995-07-05	5
1995-07-06	6
1995-07-07	7
1995-07-08	8
1995-07-09	9
1995-07-10	10
1995-07-11	11
'''

import pandas as pd

df = pd.read_clipboard()

df['rolling_sum'] = df['Test'].shift(-1).rolling(6).sum()

print(df)