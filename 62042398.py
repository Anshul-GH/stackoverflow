# '''
# address
# 3, my_street, Mumbai, Maharashtra
# Bangalore Karnataka 45th Avenue
# TelanganaHyderabad some_street, some apartment
# '''

# data = {
# "state": ["Maharashtra","Maharashtra","Bihar","Karnataka","Telangana"],
# "city": ["Mumbai","Ahmednagar","Ahmednagar","Bangalore","Hyderabad"]
# }

# import pandas as pd

# df1 = pd.read_clipboard('\t')
# df2 = pd.DataFrame(data)

# print(df1)
# print(df2)


import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('train.csv', sep='\t')


from math import sin, cos, sqrt, atan2, radians
def calculate_distance(**kwargs):
    R = 6373.0

    lat1 = radians(kwargs['plat'])
    lon1 = radians(kwargs['plon'])
    lat2 = radians(kwargs['dlat'])
    lon2 = radians(kwargs['dlon'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

df['distance'] = [calculate_distance(**df[['plat', 'plon', 'dlat', 'dlon']].iloc[i].to_dict()) for i in range(df.shape[0])]

print(df)