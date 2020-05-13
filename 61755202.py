
# # # listOflist = [[123, "A", "B", "C"], [456, "D", "E", "F"], [123, "G", "H", "I"]]

# # # test = {}

# # # temp=[{'key1':'value1','key2':'value2'},{'key1':'value3','key2':'value4'}]
# # # test['k1']['k2']['k3']=temp

# # # print(test)


# # # 61755415

# # # inp_date = '200605015'

# # # year = inp_date[:4]
# # # print(year)

# # # month = inp_date[4:6]
# # # print(month)

# # # from datetime import datetime

# # # datetime.strptime(inp_date[:6], '')

# # # import pandas as pd

# # # df = pd.DataFrame([{'Items': 'Product A + Product B + Product C'}, {'Items': 'Product A + Product B + Product B1 + Product C1'}])

# # # My_Items = ['Product B1', 'Product C']

# # # df['Item_list'] = df.Items.str.findall('|'.join(My_Items))
# # # df['Item_list'] = [','.join(val) for val in df['Item_list']]

# # # print(df)


# # import pandas as pd

# # '''
# # First_Name  Last_Name   Source
# # Matt    Jones   XX
# # James   Smith   YY
# # Smith   Weston  AA
# # Weston  Supermare   CC
# # Matt    Jones   YY
# # Weston  Supermare   FF
# # '''

# # # data = pd.read_clipboard(sep='\s\s+')
# # # print(data)
# # # print(data.columns)

# # # data = data.groupby(['First_Name', 'Last_Name'])
# # # print(data)


# # def calculatepct(gems,pct):
    
# # if pct < 0:        

# #     pct = 0

# #     not_in_dictionary = True        

# #     for child in acap1051.itertuples():

# #         if child.gems == gems:

# #             not_in_dictionary = False

# #             if child.parent_gems_ in all_children['gems'].values:

# #                 mask1 = all_children[all_children["gems"] == child.parent_gems_]

# #                 if all_children.loc[mask1.index.item()]['calculated'] == -1:

# #                     calculatepct(child.parent_gems_,all_children.loc[mask1.index.item()]['calculated'])


# '''
# Company Id      DateTime               col1  col2       col3    col4   col5     col6
# 0   25502921    2018-08-16 10:23:36     0   175.000     0.0     0.0     0.0     0
# 1   25502921    2018-08-16 10:33:55     0   155.557     0.0     0.0     0.0     0
# 2   25502921    2018-08-16 10:43:55     0   153.615     0.0     0.0     0.0     0
# '''

# import pandas as pd
# import datetime as dt

# df = pd.read_clipboard(sep='\s\s+')

# # print(df)
# # print(df.columns)
# df1 = df.loc[df['DateTime'].dt.normalize() == '2018-08-16']

# print(df1)


import pandas as pd

'''
flag
1
1
1
0
1
1
1
1
1
0
0
1
1
1
1
'''

df = pd.read_clipboard(sep='\s\s+')

lst_flag = list(df['flag'])
lst_safe = [-1]*len(lst_flag)
param = 2

print(lst_flag)
print(lst_safe)

for i in range(len(lst_flag)- param - 1):
    if 0 in lst_flag[i:(i+param+1)]:
        for j in range(param+1):
            lst_safe[i+j] = 0
    else:
        if lst_safe[i] == -1:
            lst_safe[i] = lst_flag[i]

print(lst_safe)
