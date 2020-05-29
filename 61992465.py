# # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # df = pd.read_json("sample.json").T

# # # # # # # # # # # # # # # # # # print(df)
# # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # #     Day Description
# # # # # # # # # # # # # # # # # Date    
# # # # # # # # # # # # # # # # # 2011-01-26  Wednesday   Republic Day
# # # # # # # # # # # # # # # # # 2011-03-02  Wednesday   Mahashivratri
# # # # # # # # # # # # # # # # # 2011-04-12  Tuesday Ram Navmi
# # # # # # # # # # # # # # # # # 2011-04-14  Thursday    Dr. Babasaheb Ambedkar Jayanti
# # # # # # # # # # # # # # # # # 2011-04-22  Friday  Good Friday
# # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # col_a col_b isactive
# # # # # # # # # # # # # # # # a b True
# # # # # # # # # # # # # # # # c d False
# # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # df1 = df[~df['isactive']]
# # # # # # # # # # # # # # # # print(df1)

# # # # # # # # # # # # # # # # df2 = df[df['isactive']]
# # # # # # # # # # # # # # # # print(df2)

# # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # # import numpy as np

# # # # # # # # # # # # # # # df= pd.DataFrame( {'%': {('Origin', 'Germany'): 88.88888888888889, ('Form', 'Any'): 77.77777777777777, ('Kind', 'Fresh'): 55.55555555555556}} )

# # # # # # # # # # # # # # # df["desc"] = df.index.get_level_values(0) + ": " + df.index.get_level_values(1) + " (" + df["%"].apply(np.round).astype(str) + "%)"


# # # # # # # # # # # # # # # print('\n'.join(list(df['desc'])))
# # # # # # # # # # # # # # # print(df["desc"].str.cat(sep='\n'))

# # # # # # # # # # # # # # # # print(str(df['desc']))

# # # # # # # # # # # # # # Employee_data = { 
# # # # # # # # # # # # # #     101:['Shiva', 24, 'Content Strategist'],
# # # # # # # # # # # # # #     102:['Udit',25,'Content Strategist'], 
# # # # # # # # # # # # # #     103:['Sonam', 28,'Sr Manager'], 
# # # # # # # # # # # # # #     104:['Ansari',29,'Product Lead'],
# # # # # # # # # # # # # #     105:['Huzefa',32,'Project Manager' ]
# # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # for key, val in enumerate(Employee_data):
# # # # # # # # # # # # # # #     print(val, Employee_data[val])


# # # # # # # # # # # # # # print(Employee_data[104][2])

# # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # df = pd.DataFrame({'VisitID':[1,1,1,1,2,2,2,3,3,4,4], 'Item':['A','B','C','D','A','D','B','B','C','D','C']})

# # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # filter = df.loc[df['Item'] == 'D']['VisitID']
# # # # # # # # # # # # # print(filter)


# # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # dict = {'val':[3.2, 2.4, -2.3, -4.9, 3.2, 2.4, -2.3, -4.9, 2.4, -2.3, -4.9], 
# # # # # # # # # # # #         'label': [0, 2, 1, -1, 1, 2, -1, -1,1, 1, -1]} 

# # # # # # # # # # # # df = pd.DataFrame(dict) 

# # # # # # # # # # # # print(df)

# # # # # # # # # # # # filter = df.loc[df['label'] == -1].index

# # # # # # # # # # # # req_idx = []
# # # # # # # # # # # # for idx in filter:
# # # # # # # # # # # #     if idx == 0:
# # # # # # # # # # # #         continue
# # # # # # # # # # # #     elif idx == 1:
# # # # # # # # # # # #         req_idx.append(idx-1)
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         req_idx.append(idx-2)
# # # # # # # # # # # #         req_idx.append(idx-1)

# # # # # # # # # # # # req_idx = list(set(req_idx))


# # # # # # # # # # # # df2 = df.loc[df.index.isin(req_idx)]

# # # # # # # # # # # # print(df2)



# # # # # # # # # # # my_list = ['20/20',  '30/30',  '20/80',  '120/120',  '120/140',  '165/165', '30/170',  '165/175']

# # # # # # # # # # # new_list = '/'.join(my_list)

# # # # # # # # # # # print(new_list)
# # # # # # # # # # # new_list = new_list.split('/')

# # # # # # # # # # # print(new_list)
# # # # # # # # # # # dup_list = []
# # # # # # # # # # # app_list = []

# # # # # # # # # # # for idx,val in enumerate(new_list):
# # # # # # # # # # #     # if not new_list :
        
# # # # # # # # # # #     # elif val in new_list:
# # # # # # # # # # #     # print(idx, val)
# # # # # # # # # # #     if not dup_list:
# # # # # # # # # # #         dup_list.append(val)
# # # # # # # # # # #     elif val:


# # # # # # # # # # '''
# # # # # # # # # # statutInit
# # # # # # # # # # Majoration : 0,06‰ Capital 
# # # # # # # # # # '''

# # # # # # # # # # import pandas as pd
# # # # # # # # # # import re

# # # # # # # # # # # using some random dummy seperator to get the entire 
# # # # # # # # # # df = pd.read_clipboard(sep="!")

# # # # # # # # # # df['statute'] = [re.split(r'[^a-zA-Z]+', val.strip()) for val in df['statutInit']]
# # # # # # # # # # df['statute'] = [' '.join(val) for val in df['statute']]

# # # # # # # # # # df['taux'] = [re.split(r'[a-zA-Z:\s]+', val.strip()) for val in df['statutInit']]
# # # # # # # # # # df['taux'] = [''.join(val) for val in df['taux']]


# # # # # # # # # # print(df)

# # # # # # # # # # # for val in df['per']:
# # # # # # # # # # #     print(val)
# # # # # # # # # # # print(df['per'])






# # # # # # # # # import numpy as np
# # # # # # # # # import pandas as pd
# # # # # # # # # import math

# # # # # # # # # df = pd.read_csv('/home/anshul/youtube/stackoverflow/dataset2.csv')

# # # # # # # # # print(df.info())

# # # # # # # # # x = []
# # # # # # # # # y = []

# # # # # # # # # # Populate x and y values from csv :

# # # # # # # # # for z in df['x'][0:]:
# # # # # # # # #     x.append(float(z))

# # # # # # # # # # print(x)

# # # # # # # # # for z in df['y'][0:]:
# # # # # # # # #     y.append(float(z))

# # # # # # # # # y = np.nan_to_num(y)

# # # # # # # # # # print(y)
# # # # # # # # # # y_invalid = np.nan in y
# # # # # # # # # # print(y_invalid)

# # # # # # # # # x_mean = float(np.array(x).mean())
# # # # # # # # # y_mean = float(np.array(y).mean())

# # # # # # # # # print(x_mean)
# # # # # # # # # print(y_mean)

# # # # # # # # # num = 0.0
# # # # # # # # # den = 0.0

# # # # # # # # # print("type of num",type(num))

# # # # # # # # # for z in range(len(y)):
# # # # # # # # #     num += float(y[z]) - float(y_mean)    
# # # # # # # # # for z in range(len(x)):
# # # # # # # # #     den += float(x[z]) - float(x_mean)

# # # # # # # # # print("type of num",type(num))

# # # # # # # # # print("Numerator is",num)
# # # # # # # # # print("Denominator is",den)

# # # # # # # # import pandas as pd

# # # # # # # # df=pd.DataFrame({'A':['a','b','c',1,2,3],'B':['pp','qq','rr',3,4,5]})

# # # # # # # # print(df)

# # # # # # # # print(df.apply(lambda x:x.str.contains('\w+').sum()))

# # # # # # # # # # convert all the cells of the df into a single list
# # # # # # # # # ls = df.values.tolist()
# # # # # # # # # ls = [item for sublist in ls for item in sublist]

# # # # # # # # # count = 0

# # # # # # # # # for val in ls:
# # # # # # # # #     if isinstance(val, str):
# # # # # # # # #         count += 1

# # # # # # # # # print(count)


# # # # # # # '''
# # # # # # # col1
# # # # # # # Q2 '20
# # # # # # # Q1 '21
# # # # # # # May '20
# # # # # # # June '20
# # # # # # # 25/05/2020
# # # # # # # Q4 '20+Q1 '21
# # # # # # # Q2 '21+Q3 '21
# # # # # # # Q2 '21+Q3 '21
# # # # # # # '''

# # # # # # # import pandas as pd

# # # # # # # df = pd.read_clipboard(sep="!")

# # # # # # # print(df)

# # # # # # # # ref_dict = {
# # # # # # # #     "Q4 '20+Q1 '21": 'Winter 20',
# # # # # # # #     "Q2 '21+Q3 '21": 'Summer 21',
# # # # # # # #     "Q4 '21+Q1 '22": 'Winter 21'
# # # # # # # # }

# # # # # # # # import re 

# # # # # # # # def regex_filter(val):
# # # # # # # #     regex = re.compile(r"([Q][1-4])+ '(\d+)\+([Q][1-4])+ '(\d+)")
# # # # # # # #     result = regex.split(val)
# # # # # # # #     result = [val for val in result if val]
# # # # # # # #     if 'Q3' in result:
# # # # # # # #         result = 'Summer '+result[-1]
# # # # # # # #     elif 'Q1' in result:
# # # # # # # #         result = 'Winter '+result[1]
# # # # # # # #     else:
# # # # # # # #         result = ''.join(result)

# # # # # # # #     return result

# # # # # # # # df['col1'] = df['col1'].apply(regex_filter)

# # # # # # # seasons = {
# # # # # # # r"Q4 '(\d*)\+Q1 .*": r'Winter \1',
# # # # # # # r"Q1 '(\d*)\+Q2 .*": r'Spring \1',
# # # # # # # r"Q2 '(\d*)\+Q3 .*": r'Summer \1',
# # # # # # # r"Q3 '(\d*)\+Q4 .*": r'Autumn \1'
# # # # # # # }

# # # # # # # df['col1'] = df.col1.replace(seasons, regex=True)

# # # # # # # # [ if val in ref_dict.keys() else val for val in df['col1']]
# # # # # # # # df['col2'] = df['col1'].match("([Q][1-4])+ '(\d+)\+([Q][1-4])+ '(\d+)")
# # # # # # # print(df)



# # # # # # # # regex_filter("Q2 '21+Q3 '21")




# # # # # # #     # if val:
# # # # # # #     #     mo = re.search(regex,val)
# # # # # # #     #     if mo:
# # # # # # #     #         return True
# # # # # # #     #     else:
# # # # # # #     #         return False
# # # # # # #     # else:
# # # # # # #     #     return False




# # # # # # dict_values = {'name':['John','Peter'], 'attach':['0001-test.jpg,0002-test.jpg','0003-test.jpg']}


# # # # # # import pandas as pd

# # # # # # df = pd.DataFrame(dict_values)

# # # # # # print(df)

# # # # # # df['attach'] = [val.replace(r'\D+', '') for val in df['attach']]

# # # # # # print(df)


# # # # # lst = ['a_balance', 'b_balance', 'a_agg_balance', 'b_agg_balance']

# # # # # lst_agg_bal = [col for col in lst if col.endswith('_agg_balance')]

# # # # # print(lst_agg_bal)

# # # # # lst_bal = [value for value in lst if value not in lst_agg_bal]

# # # # # print(lst_agg_bal)
# # # # # print(lst_bal)


# # # # import pandas as pd
# # # # import numpy as np
# # # # mysubset = np.array([1,2,3,4])
# # # # d = {'col1': [1, 2, 3, 4, 5, 6], 'col2': [3, 4, 1, 3, 5, 5]}
# # # # df = pd.DataFrame(data=d)
# # # # df1 = df[df['col1'].isin(mysubset)]

# # # # print(df1)

# # # # ls = [18692, 18694, 18696, 18706, 18711, 18714, 18716, 18722, 19332,
# # # #        19333, 26526, 26527, 26530, 26532, 26533, 26534, 26535, 26536,
# # # #        26538, 26541, 14107, 14110, 14120, 14149, 14165, 17984, 18004,
# # # #        18005, 18006, 18007, 18008, 18134, 18136, 18139, 18141, 18142,
# # # #        19081, 19084, 19086, 20789, 20794, 20796, 20800, 20802, 26784,
# # # #        26785, 26786, 26787]


# # # # df['print_value'] = ['temp' if val == 'In progress' else 'not' for val in df['Data status']]


# # # import pandas as pd

# # # table = pd.read_html('https://www.finra.org/investors/learn-to-invest/advanced-investing/margin-statistics')

# # # #set the index to date column
# # # df = table[0].set_index('Month/Year')

# # # df.index = df.index.str.replace("-", " ")

# # # df.index = pd.to_datetime(df.index, format="%b %y")

# # # print(df.index)


# # import pandas as pd
# # from io import StringIO

# # s = '  "Random Text"  1234.00  5678.00  9876.00 1   Z5     2   0   1   1.500   35.3   1.00  389 0.096000  10.00  15000.0  0.102  0.199  0.040  1    0       0    2900             N/A     N/A          N/A\n'
# # # print(s)

# # # df = pd.read_csv(StringIO(s), sep=None,  
# # # header=None, quoting=0, skipinitialspace=True, na_filter=False) # engine='python',
# # # # display(df)

# # # print(df)

# # # # df = pd.read_csv(StringIO(s), header=None, sep=r'\s+', quotechar='"')
# # # # print(df)

# # df = pd.read_csv(StringIO(s), sep=None, 
# # header=None, quoting=0, skipinitialspace=True) #, na_filter=False , engine='python',

# # print(df)


# '''
# productNum,ProductOMS,productPrice,Unnamed: 3
# 2463448,1002623072,419.95,
# 2463413,1002622872,289.95,
# 2463430,1002622974,309.95,
# 2463419,1002622908,329.95,
# 2463434,search?searchTerm=2463434,,
# 2463423,1002622932,469.95,
# '''


# import pandas as pd

# df = pd.read_clipboard(sep=',')

# # print(df)



# df1 = df.loc[df['ProductOMS'].str.isdigit()]

# print(df1)

# # df1 = pd.to_numeric(df['ProductOMS'], errors='coerce').notnull().all()

# print(df1)
