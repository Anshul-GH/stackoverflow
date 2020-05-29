# # # # # # # # # # # # def test() : # do not change this line!
# # # # # # # # # # # #   list = [4, 5, 1, 9, -2, 0, 3, -5] # do not change this line!
# # # # # # # # # # # #   list = sorted(list)
# # # # # # # # # # # #   min1 = list[0]
# # # # # # # # # # # #   min2 = list[1]
# # # # # # # # # # # #   #missing code here

# # # # # # # # # # # #   print(min1, min2)
# # # # # # # # # # # #   return (min1, min2) # do not change this line!
# # # # # # # # # # # # # do not write any code below here  

# # # # # # # # # # # # test() # do not change this line!
# # # # # # # # # # # # # do not remove this line!


# # # # # # # # # # # # and = 1

# # # # # # # # # # # # Did not worked:
# # # # # # # # # # # # and, or, not, print

# # # # # # # # # # # # Worked:
# # # # # # # # # # # # bytes




# # # # # # # # # # # # int = 1 # works

# # # # # # # # # # # # set = 1.0

# # # # # # # # # # # # print(set)


# # # # # # # # # # # # and = 1; print(and) no
# # # # # # # # # # # # or = 1; print(or) no
# # # # # # # # # # # # not = 1; print(not) no
# # # # # # # # # # # # int = 1; print(int) yes
# # # # # # # # # # # # float = 1; print(float) yes
# # # # # # # # # # # # complex = 1; print(complex) yes
# # # # # # # # # # # # list = 1; print(list) yes
# # # # # # # # # # # # tuple = 1; print(tuple) yes
# # # # # # # # # # # # range = 1; print(range) yes
# # # # # # # # # # # # str = 1; print(str) yes
# # # # # # # # # # # # bytes = 1; print(bytes) yes
# # # # # # # # # # # # bytearray = 1; print(bytearray) yes
# # # # # # # # # # # # memoryview = 1; print(memoryview) yes
# # # # # # # # # # # # print = 1; print(print) no
# # # # # # # # # # # # set = 1; print(set) yes
# # # # # # # # # # # # frozenset = 1; print(frozenset) yes
# # # # # # # # # # # # dict = 1; print(dict) yes

# # # # # # # # # # # import re
# # # # # # # # # # def checkCard():
# # # # # # # # # #     hand = ["KC", "9D", "10S", "jH","11H", "0S", "HC", "Q2S", "100D", "1C", "2D2"]
# # # # # # # # # #     true_vals = ["KC", "9D", "10S", "jH"]
# # # # # # # # # #     # bool_op = [True if val in true_vals else False for val in hand]
# # # # # # # # # #     bool_op = list(map(lambda val: True if val in true_vals else False, hand))
    
# # # # # # # # # #     print(bool_op)  
# # # # # # # # # # checkCard()

# # # # # # # # # # a = '1'
# # # # # # # # # # b = "11"
# # # # # # # # # # print(a + b)

# # # # # # # # # import pandas as pd
# # # # # # # # # df=pd.DataFrame(data=None)

# # # # # # # # # # def on_ticks(ws, ticks):
# # # # # # # # # #     global df
# # # # # # # # # # for sc in ticks:
# # # # # # # # # # token=sc['instrument_token']
# # # # # # # # # name='data'
# # # # # # # # # ltp=123.45
# # # # # # # # # df1 = pd.DataFrame([name,ltp]).T
# # # # # # # # # df1.columns = ['name', 'ltp']
# # # # # # # # # df=df.append(df1,ignore_index=True)

# # # # # # # # # # df = df.append([[name, ltp]], ignore_index=True, column=['name', 'ltp'])


# # # # # # # # # print(df)

# # # # # # # # import pandas as pd

# # # # # # # # test = pd.Series(['abcD0', 'defg', 'abcD1', 'ght', 'abcd_1', 'bbb0', 'bbb1', 'bbb_1'])

# # # # # # # # # print(test)

# # # # # # # # import re

# # # # # # # # test_new = [re.sub('\d+', '', val) if "_" not in val else val for val in test]

# # # # # # # # print(test_new)

# # # # # # # import pandas as pd

# # # # # # # indices_a = [0,1,3,6,10,15, 20, 40, 50,70, 100,400,700]
# # # # # # # indices_b = [0,1,3,6,10,15, 20, 40, 50,70, 100,400,700]

# # # # # # # a = pd.DataFrame({'time': pd.date_range(start='2016-03-10', end='2019-03-10'),
# # # # # # #                 'a': [1 if val in indices_a else 0 for val in range(1096)],
# # # # # # #                 'b': [1 if val in indices_b else 0 for val in range(1096)]})


# # # # # # # # a.loc[indices_a,'a'] = 1
# # # # # # # # a.loc[indices_b,'b'] = 1

# # # # # # # print(a.head(10))


# # # # # # dict1 = {
# # # # # # 'Alice': {'AGATC': '2', 'AATG': '8', 'TATC': '3'},
# # # # # # 'Bob': {'AGATC': '4', 'AATG': '1', 'TATC': '5'},
# # # # # # 'Charlie': {'AGATC': '3', 'AATG': '2', 'TATC': '5'}
# # # # # # }

# # # # # # dict2 = {'AGATC': '4', 'AATG': '1', 'GATA': '2', 'TATC': '5', 'GAAA': '3'}

# # # # # # print(dict2 in dict1.values())

# # # # # import json
# # # # # import pandas as pd

# # # # # data = pd.read_json("62061012.json")

# # # # # notifications = data["notifications"]
# # # # # for notification in notifications:
# # # # #     if notification["updates"].get("inDiscards" or "outDiscards"):
# # # # #         outDiscards = notification["updates"]["outDiscards"]["value"]["avg"]["float"]
# # # # #         inDiscards = notification["updates"]["inDiscards"]["value"]["avg"]["float"]
# # # # #         name = notification["path_elements"][1]
# # # # #         interface = notification["path_elements"][5]
# # # # #         print(name, interface, outDiscards, inDiscards, sep=',')


# # # # zdict = { 'a':1,'b':2,'c':3}
# # # # print(list(zdict.values()) + list(zdict.keys()))

# # # # lst = []

# # # # for key, val in zdict.iteritems():
# # # #     lst.append(key)
# # # #     lst.append(value)

# # # # print(lst)

# # # candidates = [' '.join(word for word, pos, chunk in group).lower()
# # #               for key, group in itertools.groupby(all_chunks, lambda (word,pos,chunk): chunk != 'O') if key]


# # '''
# # value	name	type	plain_data
# # 1000	A	UE	[{'sub_name':'a','itm':{'b_amt':100,'t_amt':150,'val':200}},{'sub_name':'a2','itm':{'b_amt':150,'t_amt':100,'val':300}]
# # 2000	B	RN	[{'sub_name':'b','itm':{'b_amt':300,'t_amt':200,'val':400}},{'sub_name':'b2','itm':{'b_amt':300,'t_amt':600,'val':200}]
# # '''

# # import pandas as pd
# # import re

# # df = pd.read_clipboard()

# # df['sum'] = [sum(list(map(int, re.findall(r':(\d+)', val)))) for val in df['plain_data']]
# # df.drop(columns='plain_data', inplace=True)
# # df['matches_value'] = df['value'] == df['sum']

# # # df['matches_value'] = ['True' if val_sum == val else 'False' for val in df[['value', 'sum']]]

# # print(df)


# master_list = [[7.3,10.3,7.3,3.4,1.2,0.3,0.1,8.8,12.4,8.8,4.1,1.5,0.4,0.1,5.3,7.5,5.3,2.5,0.9,0.2,0.1,2.1,3.0,2.1,1.0,0.4,0.1,0.0,0.6,0.9,0.6,0.3,0.1,0.0,0.0,0.2,0.2,0.2,0.1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
# [4.6,6.6,4.7,2.3,0.8,0.2,0.1,7.6,10.9,7.8,3.7,1.3,0.4,0.1,6.3,8.9,6.4,3.0,1.1,0.3,0.1,3.4,4.9,3.5,1.7,0.6,0.2,0.0,1.4,2.0,1.4,0.7,0.2,0.1,0.0,0.5,0.7,0.5,0.2,0.1,0.0,0.0,0.1,0.2,0.1,0.1,0.0,0.0,0.0],
# [6.4,9.1,6.4,3.0,1.1,0.3,0.1,8.5,12.1,8.6,4.0,1.4,0.4,0.1,5.7,8.1,5.7,2.7,1.0,0.3,0.1,2.5,3.6,2.5,1.2,0.4,0.1,0.0,0.8,1.2,0.8,0.4,0.1,0.0,0.0,0.2,0.3,0.2,0.1,0.0,0.0,0.0,0.0,0.1,0.1,0.0,0.0,0.0,0.0],
# [3.9,5.8,4.4,2.2,0.8,0.2,0.1,6.8,10.2,7.6,3.8,1.4,0.4,0.1,5.9,8.9,6.7,3.3,1.3,0.4,0.1,3.5,5.2,3.9,1.9,0.7,0.2,0.1,1.5,2.3,1.7,0.9,0.3,0.1,0.0,0.5,0.8,0.6,0.3,0.1,0.0,0.0,0.2,0.2,0.2,0.1,0.0,0.0,0.0],
# [7.2,10.0,6.8,3.1,1.1,0.3,0.1,9.1,12.5,8.6,3.9,1.3,0.4,0.1,5.7,7.8,5.3,2.5,0.8,0.2,0.1,2.4,3.2,2.2,1.0,0.4,0.1,0.0,0.7,1.0,0.7,0.3,0.1,0.0,0.0,0.2,0.3,0.2,0.1,0.0,0.0,0.0,0.0,0.1,0.0,0.0,0.0,0.0,0.0],
# [3.0,4.9,4.0,2.2,0.9,0.3,0.1,5.7,9.2,7.5,4.0,1.6,0.5,0.1,5.3,8.6,7.0,3.8,1.5,0.5,0.1,3.3,5.4,4.4,2.4,1.0,0.3,0.1,1.6,2.5,2.1,1.1,0.5,0.1,0.0,0.6,0.9,0.8,0.4,0.2,0.1,0.0,0.2,0.3,0.2,0.1,0.1,0.0,0.0],
# [6.9,8.1,4.7,1.8,0.5,0.1,0.0,10.4,12.2,7.1,2.8,0.8,0.2,0.0,7.8,9.1,5.3,2.1,0.6,0.1,0.0,3.9,4.6,2.7,1.0,0.3,0.1,0.0,1.5,1.7,1.0,0.4,0.1,0.0,0.0,0.4,0.5,0.3,0.1,0.0,0.0,0.0,0.1,0.1,0.1,0.0,0.0,0.0,0.0],
# [3.0,4.5,3.4,1.7,0.6,0.2,0.0,6.0,9.1,6.8,3.4,1.3,0.4,0.1,6.0,9.1,6.8,3.4,1.3,0.4,0.1,4.0,6.0,4.5,2.3,0.8,0.3,0.1,2.0,3.0,2.3,1.1,0.4,0.1,0.0,0.8,1.2,0.9,0.5,0.2,0.1,0.0,0.3,0.4,0.3,0.2,0.1,0.0,0.0],
# [6.4,9.6,7.2,3.6,1.3,0.4,0.1,8.0,12.0,9.0,4.5,1.7,0.5,0.1,5.0,7.5,5.6,2.8,1.1,0.3,0.1,2.1,3.1,2.3,1.2,0.4,0.1,0.0,0.7,1.0,0.7,0.4,0.1,0.0,0.0,0.2,0.2,0.2,0.1,0.0,0.0,0.0,0.0,0.1,0.0,0.0,0.0,0.0,0.0],
# [1.1,1.9,1.7,1.0,0.4,0.2,0.0,3.1,5.3,4.7,2.7,1.2,0.4,0.1,4.2,7.4,6.4,3.8,1.6,0.6,0.2,3.9,6.7,5.9,3.4,1.5,0.5,0.2,2.6,4.6,4.1,2.4,1.0,0.4,0.1,1.5,2.5,2.2,1.3,0.6,0.2,0.1,0.7,1.2,1.0,0.6,0.3,0.1,0.0]]

# import pandas as pd

# df = pd.DataFrame()
# i = 0

# # for lst in master_list:
# #     df['col_'+str(i)] = lst

# lst = list(map(list, zip(*master_list)))

# df = pd.DataFrame(lst)

# print(df)

# for read_clipboard()
'''
salary_day
monday
tuesday
wednesday
thursday
friday
saturday
sunday
'''

import pandas as pd
df = pd.read_clipboard()
# print(df)


import calendar

d=dict(enumerate(calendar.day_name))

c = calendar.Calendar(firstweekday=calendar.SUNDAY)

year = 2020; month = 5

monthcal = c.monthdatescalendar(year,month)
# fridays = [(str(day)[-2:]) for week in monthcal for day in week if \
#                 day.weekday() == calendar.FRIDAY and \
#                 day.month == month]
# thursdays = [(str(day)[-2:]) for week in monthcal for day in week if \
#                 day.weekday() == calendar.THURSDAY and \
#                 day.month == month]

day_date = [{d[day.weekday()]: (str(day)[-2:])} for week in monthcal for day in week if \
                # day.weekday() == calendar.FRIDAY and \
                day.month == month]

# print(day_date)

# df1 = pd.DataFrame(day_date)
# print(df1)

# df['req_dates'] = ''

# # for the months with 5 fridays
# if int(thursdays[0]) < int(fridays[0]):
#     fridays = fridays[1:]

# df.loc[df['salary_day'] == 'thursday', 'req_dates'] = ','.join(thursdays[::2])
# df.loc[df['salary_day'] == 'friday', 'req_dates'] = ','.join(fridays[::2])

# print(df)

# print(fridays[::2])
# print(thursdays[::2])

# if fridays[0] != 1:
#     df.loc[df['salary_day'] == 'thursday']['req_dates'] = thursdays[::2]
#     df.loc[df['salary_day'] == 'friday']['req_dates'] = fridays[::2]
# else:
#     df.loc[df['salary_day'] == 'thursday']['req_dates'] = thursdays[1::2]
#     df.loc[df['salary_day'] == 'friday']['req_dates'] = fridays[::2]

# print(df)
