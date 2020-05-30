'''
Loan_ID
loan_status
Principal
terms
effective_date
due_date
paid_off_time
past_due_days
age
education
Gender
'''

import pandas as pd
import string

df = pd.read_clipboard()

df['Loan_ID'] = df['Loan_ID'].apply(lambda x: string.capwords(x, sep='_'))

print(df)


import pandas as pd

df = pd.read_clipboard()

df.insert(1,'prev_year',(df['year']-1))

print(df)