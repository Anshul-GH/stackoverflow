# # # # # # # # # # import pandas as pd

# # # # # # # # # # df = pd.read_json("sample.json").T

# # # # # # # # # # print(df)
# # # # # # # # # '''
# # # # # # # # #     Day Description
# # # # # # # # # Date    
# # # # # # # # # 2011-01-26  Wednesday   Republic Day
# # # # # # # # # 2011-03-02  Wednesday   Mahashivratri
# # # # # # # # # 2011-04-12  Tuesday Ram Navmi
# # # # # # # # # 2011-04-14  Thursday    Dr. Babasaheb Ambedkar Jayanti
# # # # # # # # # 2011-04-22  Friday  Good Friday
# # # # # # # # # '''

# # # # # # # # # import pandas as pd

# # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # print(df)

# # # # # # # # '''
# # # # # # # # col_a col_b isactive
# # # # # # # # a b True
# # # # # # # # c d False
# # # # # # # # '''

# # # # # # # # import pandas as pd

# # # # # # # # df = pd.read_clipboard()

# # # # # # # # df1 = df[~df['isactive']]
# # # # # # # # print(df1)

# # # # # # # # df2 = df[df['isactive']]
# # # # # # # # print(df2)

# # # # # # # # # print(df)

# # # # # # # import pandas as pd
# # # # # # # import numpy as np

# # # # # # # df= pd.DataFrame( {'%': {('Origin', 'Germany'): 88.88888888888889, ('Form', 'Any'): 77.77777777777777, ('Kind', 'Fresh'): 55.55555555555556}} )

# # # # # # # df["desc"] = df.index.get_level_values(0) + ": " + df.index.get_level_values(1) + " (" + df["%"].apply(np.round).astype(str) + "%)"


# # # # # # # print('\n'.join(list(df['desc'])))
# # # # # # # print(df["desc"].str.cat(sep='\n'))

# # # # # # # # print(str(df['desc']))

# # # # # # Employee_data = { 
# # # # # #     101:['Shiva', 24, 'Content Strategist'],
# # # # # #     102:['Udit',25,'Content Strategist'], 
# # # # # #     103:['Sonam', 28,'Sr Manager'], 
# # # # # #     104:['Ansari',29,'Product Lead'],
# # # # # #     105:['Huzefa',32,'Project Manager' ]
# # # # # # }

# # # # # # # for key, val in enumerate(Employee_data):
# # # # # # #     print(val, Employee_data[val])


# # # # # # print(Employee_data[104][2])

# # # # # import pandas as pd

# # # # # df = pd.DataFrame({'VisitID':[1,1,1,1,2,2,2,3,3,4,4], 'Item':['A','B','C','D','A','D','B','B','C','D','C']})

# # # # # print(df)

# # # # # filter = df.loc[df['Item'] == 'D']['VisitID']
# # # # # print(filter)


# # # # import pandas as pd
# # # # dict = {'val':[3.2, 2.4, -2.3, -4.9, 3.2, 2.4, -2.3, -4.9, 2.4, -2.3, -4.9], 
# # # #         'label': [0, 2, 1, -1, 1, 2, -1, -1,1, 1, -1]} 

# # # # df = pd.DataFrame(dict) 

# # # # print(df)

# # # # filter = df.loc[df['label'] == -1].index

# # # # req_idx = []
# # # # for idx in filter:
# # # #     if idx == 0:
# # # #         continue
# # # #     elif idx == 1:
# # # #         req_idx.append(idx-1)
# # # #     else:
# # # #         req_idx.append(idx-2)
# # # #         req_idx.append(idx-1)

# # # # req_idx = list(set(req_idx))


# # # # df2 = df.loc[df.index.isin(req_idx)]

# # # # print(df2)



# # # my_list = ['20/20',  '30/30',  '20/80',  '120/120',  '120/140',  '165/165', '30/170',  '165/175']

# # # new_list = '/'.join(my_list)

# # # print(new_list)
# # # new_list = new_list.split('/')

# # # print(new_list)
# # # dup_list = []
# # # app_list = []

# # # for idx,val in enumerate(new_list):
# # #     # if not new_list :
        
# # #     # elif val in new_list:
# # #     # print(idx, val)
# # #     if not dup_list:
# # #         dup_list.append(val)
# # #     elif val:


# # '''
# # statutInit
# # Majoration : 0,06‰ Capital 
# # '''

# # import pandas as pd
# # import re

# # # using some random dummy seperator to get the entire 
# # df = pd.read_clipboard(sep="!")

# # df['statute'] = [re.split(r'[^a-zA-Z]+', val.strip()) for val in df['statutInit']]
# # df['statute'] = [' '.join(val) for val in df['statute']]

# # df['taux'] = [re.split(r'[a-zA-Z:\s]+', val.strip()) for val in df['statutInit']]
# # df['taux'] = [''.join(val) for val in df['taux']]


# # print(df)

# # # for val in df['per']:
# # #     print(val)
# # # print(df['per'])






# import numpy as np
# import pandas as pd
# import math

# df = pd.read_csv('/home/anshul/youtube/stackoverflow/dataset2.csv')

# print(df.info())

# x = []
# y = []

# # Populate x and y values from csv :

# for z in df['x'][0:]:
#     x.append(float(z))

# # print(x)

# for z in df['y'][0:]:
#     y.append(float(z))

# y = np.nan_to_num(y)

# # print(y)
# # y_invalid = np.nan in y
# # print(y_invalid)

# x_mean = float(np.array(x).mean())
# y_mean = float(np.array(y).mean())

# print(x_mean)
# print(y_mean)

# num = 0.0
# den = 0.0

# print("type of num",type(num))

# for z in range(len(y)):
#     num += float(y[z]) - float(y_mean)    
# for z in range(len(x)):
#     den += float(x[z]) - float(x_mean)

# print("type of num",type(num))

# print("Numerator is",num)
# print("Denominator is",den)

import pandas as pd

df=pd.DataFrame({'A':['a','b','c',1,2,3],'B':['pp','qq','rr',3,4,5]})

print(df)

print(df.apply(lambda x:x.str.contains('\w+').sum()))

# # convert all the cells of the df into a single list
# ls = df.values.tolist()
# ls = [item for sublist in ls for item in sublist]

# count = 0

# for val in ls:
#     if isinstance(val, str):
#         count += 1

# print(count)
