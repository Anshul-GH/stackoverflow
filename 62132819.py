# # # # # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # # # #    a
# # # # # # # # # # # # # # # # # # # # # # a  0
# # # # # # # # # # # # # # # # # # # # # # b  10
# # # # # # # # # # # # # # # # # # # # # # c  12
# # # # # # # # # # # # # # # # # # # # # # d  21
# # # # # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # # # # # # # dist = 15
# # # # # # # # # # # # # # # # # # # # # # val = list(df.loc[(df['a'] < dist) & (df.index != 'a')].index)
# # # # # # # # # # # # # # # # # # # # # # print(val)

# # # # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # # # PROD   TYPE  QUANTI CONFI avail  req
# # # # # # # # # # # # # # # # # # # # # wood   i     20     100   1000  800
# # # # # # # # # # # # # # # # # # # # # tv     u     30     100   500   600
# # # # # # # # # # # # # # # # # # # # # tabl   i     50     100   300   200
# # # # # # # # # # # # # # # # # # # # # rmt    z     40     100   50    100
# # # # # # # # # # # # # # # # # # # # # zet    y     60     100   200   400
# # # # # # # # # # # # # # # # # # # # # rm     t     60     100   300   500
# # # # # # # # # # # # # # # # # # # # # rt     f     80     100   500   200
# # # # # # # # # # # # # # # # # # # # # dud    i     40     100   900   800
# # # # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # # # # # # for row in df.iterrows():
# # # # # # # # # # # # # # # # # # # # #     print(type(row))

# # # # # # # # # # # # # # # # # # # # # # df['CONFI'] = [100 for row in df.iterrows() if (row[-2] - row[-1]) > 80]
# # # # # # # # # # # # # # # # # # # # # # # #df.loc[df['TYPE'] == 'i']

# # # # # # # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # # Fridge:200:1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
# # # # # # # # # # # # # # # # # # # # Washer:500:0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0
# # # # # # # # # # # # # # # # # # # # Oven:2150:0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0
# # # # # # # # # # # # # # # # # # # # Microwave:1000:0,0,0,0,0,0,0,0,0.5,0,0,0,0,0,0,0,0,0.5,0,0,0.5,0,0,0
# # # # # # # # # # # # # # # # # # # # Aircon:2000:0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0
# # # # # # # # # # # # # # # # # # # # TV:60:1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
# # # # # # # # # # # # # # # # # # # # TV:60:1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
# # # # # # # # # # # # # # # # # # # # TV:60:1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
# # # # # # # # # # # # # # # # # # # # Console:140:1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
# # # # # # # # # # # # # # # # # # # # Console:140:1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
# # # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # for your case, if you are reading the data from csv, 
# # # # # # # # # # # # # # # # # # # # # use the separator as ":" just like below
# # # # # # # # # # # # # # # # # # # # df = pd.read_clipboard(sep=":", header=None)

# # # # # # # # # # # # # # # # # # # # # df[2] = df[2].str.replace(",","+")

# # # # # # # # # # # # # # # # # # # # df[3]=df[2].str.split(',',expand=True).astype(float).sum(axis=1)

# # # # # # # # # # # # # # # # # # # # # df[3] = [map(int, val) for val in df[2].str.split(',')]
# # # # # # # # # # # # # # # # # # # # # sum(map(int, df[2].str.split(',')))) # sum(df[2].str.split(','))

# # # # # # # # # # # # # # # # # # # # # df[3] = [eval(val) for val in df[2]]

# # # # # # # # # # # # # # # # # # # # # df[2] = df[2].str.replace("+",",")

# # # # # # # # # # # # # # # # # # # # print(df)
# # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # time	Discharge	Resistance	Greater_than_50
# # # # # # # # # # # # # # # # # # # 0	0.000	NaN	NaN
# # # # # # # # # # # # # # # # # # # 1	0.005	76.373	True
# # # # # # # # # # # # # # # # # # # 2	0.010	-48.174	False
# # # # # # # # # # # # # # # # # # # 3	0.016	-37.012	False
# # # # # # # # # # # # # # # # # # # 4	0.021	-27.808	False
# # # # # # # # # # # # # # # # # # # 5	0.026	-24.674	False
# # # # # # # # # # # # # # # # # # # 6	0.031	-20.464	False
# # # # # # # # # # # # # # # # # # # 7	0.037	100.114	True
# # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # # # # # df['Greater_than_50'] = [val.strip() for val in df['Greater_than_50'].astype(str)]

# # # # # # # # # # # # # # # # # # # # columns to keep
# # # # # # # # # # # # # # # # # # # col_mask = ['Discharge', 'Resistance']

# # # # # # # # # # # # # # # # # # # df_new = df.loc[df['Greater_than_50'] == 'True'][col_mask].reset_index(drop=True)

# # # # # # # # # # # # # # # # # # # # # columns to keep
# # # # # # # # # # # # # # # # # # # # col_mask = ['Discharge', 'Resistance']

# # # # # # # # # # # # # # # # # # # # df_new = df_new[col_mask]

# # # # # # # # # # # # # # # # # # # print(df_new)

# # # # # # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # # # # # import numpy as np

# # # # # # # # # # # # # # # # # # df1 = pd.DataFrame(np.array([['A', '2015-12-21'],['A', '2015-12-22'], ['A', '2015-12-25'], ['B', '2018-01-28'],['B', '2018-02-28'],['B', '2018-03-28']]),
# # # # # # # # # # # # # # # # # #                    columns=['name', 'date'])

# # # # # # # # # # # # # # # # # # df2 = pd.DataFrame(np.array([['A', '2015-12-23'], ['B', '2018-03-01']]),
# # # # # # # # # # # # # # # # # #                    columns=['name', 'startdate'])

# # # # # # # # # # # # # # # # # # # df1['date'] = pd.to_datetime(df1['date'], format='%y-%m-%d')
# # # # # # # # # # # # # # # # # # # df2['startdate'] = pd.to_datetime(df2['startdate'], format='%y-%m-%d')

# # # # # # # # # # # # # # # # # # df1['date'] = pd.to_datetime(df1['date'], format='%y-%m-%d')
# # # # # # # # # # # # # # # # # # df2['startdate'] = pd.to_datetime(df2['startdate'], format='%y-%m-%d')

# # # # # # # # # # # # # # # # # # print(df1)
# # # # # # # # # # # # # # # # # # print(df2)


# # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # datetimeindex	Value
# # # # # # # # # # # # # # # # # 09:00:00	34
# # # # # # # # # # # # # # # # # 09:01:00	45
# # # # # # # # # # # # # # # # # 09:02:00	48
# # # # # # # # # # # # # # # # # 09:03:00	50
# # # # # # # # # # # # # # # # # 18:58:00	55
# # # # # # # # # # # # # # # # # 18:59:00	65
# # # # # # # # # # # # # # # # # 19:00:00	68
# # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # df1 = pd.read_clipboard()

# # # # # # # # # # # # # # # # # df1['datetimeindex'] = pd.to_datetime(df1['datetimeindex'], infer_datetime_format=True)

# # # # # # # # # # # # # # # # # df1.index = df1['datetimeindex']
# # # # # # # # # # # # # # # # # df1.drop(['datetimeindex'], axis=1, inplace=True)

# # # # # # # # # # # # # # # # # print(df1)

# # # # # # # # # # # # # # # # # data = {
# # # # # # # # # # # # # # # # #     "Time_1": ["09:00:00","18:55:00","11:55:00","17:05:00"],
# # # # # # # # # # # # # # # # #     "Time_2": ["09:05:00","19:00:00","12:15:00","17:15:00"]
# # # # # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # # # df2 = pd.DataFrame(data, dtype='datetime64[ns]')

# # # # # # # # # # # # # # # # # print(df2)

# # # # # # # # # # # # # # # # # mask = df1.index.astype('datetime64[ns]') >= df2['Time_1'].astype('datetime64[ns]') & df1.index.astype('datetime64[ns]') <= df2['Time_2'].astype('datetime64[ns]')

# # # # # # # # # # # # # # # # # df3 = df1.loc[mask]

# # # # # # # # # # # # # # # # # print(df3)

# # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # df = pd.DataFrame([['indiejesse.d@gmail.com; pamelasilvera69@gmail.com; kristinestringer69@gmail.com', 'conference meeting ...']], columns=['CC', 'Body'])

# # # # # # # # # # # # # # # # df['CC_count'] = df['CC'].str.count(';').add(1)

# # # # # # # # # # # # # # # # print(df)



# # # # # # # # # # # # # # # import numpy as np
# # # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # # import matplotlib.pyplot as plt
# # # # # # # # # # # # # # # import seaborn as sns

# # # # # # # # # # # # # # # index = np.arange(1, 49, 1)
# # # # # # # # # # # # # # # value = np.append(np.arange(1,25,1), np.arange(25,1,-1))
# # # # # # # # # # # # # # # color_choice = np.random.choice(['YES', 'NO'], 48, p=[0.3, 0.7])

# # # # # # # # # # # # # # # dt = pd.DataFrame(zip(index, value, color_choice), columns=['index', 'value', 'color_choice'])

# # # # # # # # # # # # # # # plt.figure(figsize = (16, 5))
# # # # # # # # # # # # # # # color_dict = dict({'NO':'green', 'YES':'red'})
# # # # # # # # # # # # # # # sns.pointplot(x="index", y="value", data=dt, hue="color_choice", palette=color_dict)

# # # # # # # # # # # # # # import os
# # # # # # # # # # # # # # import shutil

# # # # # # # # # # # # # # archive = "archive"
# # # # # # # # # # # # # # if not os.path.exists(archive):
# # # # # # # # # # # # # #     os.mkdir(archive)
# # # # # # # # # # # # # # gzfile = "lalala.gz"
# # # # # # # # # # # # # # dest = '\\'.join([archive, gzfile])
# # # # # # # # # # # # # # shutil.move(gzfile, dest)


# # # # # # # # # # # # # '''
# # # # # # # # # # # # # yyyy-mm	ID	Amt
# # # # # # # # # # # # # 2019-08	0	0
# # # # # # # # # # # # # 2019-09	0	0
# # # # # # # # # # # # # 2019-10	0	0
# # # # # # # # # # # # # 2019-11	0	0
# # # # # # # # # # # # # 2019-12	0	0
# # # # # # # # # # # # # 2020-01	0	0
# # # # # # # # # # # # # 2020-02	0	0
# # # # # # # # # # # # # 2020-03	0	100
# # # # # # # # # # # # # 2020-04	0	0
# # # # # # # # # # # # # 2020-05	0	0
# # # # # # # # # # # # # 2020-06	0	0
# # # # # # # # # # # # # 2020-07	0	0
# # # # # # # # # # # # # 2020-08	0	150
# # # # # # # # # # # # # 2020-09	0	0
# # # # # # # # # # # # # 2020-10	0	0
# # # # # # # # # # # # # 2020-11	0	0
# # # # # # # # # # # # # 2020-12	0	1000
# # # # # # # # # # # # # 2021-01	0	10000
# # # # # # # # # # # # # 2021-02	0	0
# # # # # # # # # # # # # 2021-03	0	0
# # # # # # # # # # # # # 2021-04	0	0
# # # # # # # # # # # # # 2021-05	0	0
# # # # # # # # # # # # # 2021-06	0	0
# # # # # # # # # # # # # 2021-07	0	0
# # # # # # # # # # # # # 2019-01	1	0
# # # # # # # # # # # # # 2019-02	1	0
# # # # # # # # # # # # # 2019-03	1	0
# # # # # # # # # # # # # 2019-04	1	0
# # # # # # # # # # # # # 2019-05	1	0
# # # # # # # # # # # # # 2019-06	1	0
# # # # # # # # # # # # # '''

# # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # df['Expected'] = df.groupby('ID')['Amt'].cumsum()

# # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # [[[1,10],[2,20],[3,30]],[[4,40],[5,50],[6,60]]]

# # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # df1 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4,5,6]})

# # # # # # # # # # # # df2 = pd.DataFrame({'col1': [10, 20, 30], 'col2': [40,50,60]})

# # # # # # # # # # # # print(df1)
# # # # # # # # # # # # print(df2)


# # # # # # # # # # # '''
# # # # # # # # # # # Country	Energy Supply	Energy Supply per Capita
# # # # # # # # # # # Afghanistan	3.210000e+08	10.0
# # # # # # # # # # # Albania	1.020000e+08	35.0
# # # # # # # # # # # Algeria	1.959000e+09	51.0
# # # # # # # # # # # American Samoa	NaN	NaN
# # # # # # # # # # # Bolivia	3.360000e+08	32.0
# # # # # # # # # # # Republic of Korea	1.100700e+10	221.0 
# # # # # # # # # # # Switzerland	1.113000e+09	136.0 
# # # # # # # # # # # Syrian Arab Republic	5.420000e+08	28.0
# # # # # # # # # # # Tajikistan	1.060000e+08	13.0
# # # # # # # # # # # Thailand	5.336000e+09	79.0
# # # # # # # # # # # Ukraine	4.844000e+09	107.0
# # # # # # # # # # # United Kingdom of Great Britain and Northern	7.920000e+09	124.0 
# # # # # # # # # # # United Republic of Tanzania	9.940000e+08	20.0
# # # # # # # # # # # United States of America	9.083800e+10	286.0
# # # # # # # # # # # '''

# # # # # # # # # # # import pandas as pd

# # # # # # # # # # # df = pd.read_clipboard("\t")

# # # # # # # # # # # print(df.info())

# # # # # # # # # # # df.replace({"United States of America":"United States",
# # # # # # # # # # # "United Kingdom of Great Britain and Northern":"United Kingdom"},inplace=True)

# # # # # # # # # # # print(df)

# # # # # # # # # # import pandas as pd

# # # # # # # # # # index = pd.MultiIndex.from_product([['A','B'],range(3)],names=['Letters','Numbers'])
# # # # # # # # # # s = pd.Series([0,2,1,2,0,2], index=index)

# # # # # # # # # # print(s)

# # # # # # # # # # df = s.groupby('Letters').nlargest(-1)

# # # # # # # # # # print(df)

# # # # # # # # # import pandas as pd

# # # # # # # # # df = pd.DataFrame({'CaseNo':[1,1,2,2,2,2],
# # # # # # # # #                     'Test1':['180','189','328','328','266','256'],
# # # # # # # # #                     'Test2':['20','21','33','30','28','15'],
# # # # # # # # #                     'Test3':['55','55','58','64','68','58'],
# # # # # # # # #                     'Age':['65','65','45','45','45','45']})

# # # # # # # # # print(df)

# # # # # # # # # df1 = df.groupby(['Age', 'CaseNo']).tail(1)

# # # # # # # # # print(df1)

# # # # # # # # import subprocess

# # # # # # # # print(str(subprocess.check_call(['git', 'clone', 'https://github.com/hello/automan.git'])))



# # # # # # # # define the default output as 'Weird' 
# # # # # # # output = "Weird"

# # # # # # # n = int(input())

# # # # # # # # only check the conditions that will need 
# # # # # # # # the output to be updated to 'Not Weird'
# # # # # # # if (n in list(range(2, 6, 2))) | (n > 20 & n % 2 == 0):
# # # # # # #     output = "Not Weird"

# # # # # # # print(output)

# # # # # # # # if n%2==1:
# # # # # # # #   print('weird')
# # # # # # # # else:
# # # # # # # #   if n%2==0 and 2<=n<=5:
# # # # # # # #     print('not weird')
# # # # # # # #   elif n%2==0 and 6<=n<=20:
# # # # # # # #     print ("Weird")
# # # # # # # #   elif n%2==0 and n>20:
# # # # # # # #     print('not weird')`



# # # # # # input_data = [
# # # # # #     {
# # # # # #         "name": "system1",
# # # # # #         "other_param": "%param1%",
# # # # # #         "secret_text": "%secret%",
# # # # # #         "options": {
# # # # # #             "conditions": "[\"f--updated_at,geq,\\\"%max_date%\\\"\",\"f--status,eq,\\\"Void\\\"\"]"
# # # # # #         }
# # # # # #     }
# # # # # # ]

# # # # # # variables = {
# # # # # #     '%secret%': "abc",
# # # # # #     '%param1%': "text_param",
# # # # # #     '%max_date%': '2018-01-01'
# # # # # # }

# # # # # # # variables = dict(variables)

# # # # # # # convert input data to string

# # # # # # data = str(input_data)

# # # # # # for k, v in variables.items():
# # # # # #     data = data.replace(k, v)

# # # # # # import ast
# # # # # # data = ast.literal_eval(data)
# # # # # # print(type(data))
# # # # # # print(data)

# # # # # '''
# # # # # 	x	y	z
# # # # # toto	2020-12-13 00:00:00	2020-12-13 00:00:00	2020-12-13 00:00:00
# # # # # titi	1	2	3
# # # # # tata	4	5	6
# # # # # '''

# # # # # import pandas as pd

# # # # # data = {
# # # # # "x":["2020-12-13 00:00:00",1,4],
# # # # # "y":["2020-12-13 00:00:00",2,5],
# # # # # "z":["2020-12-13 00:00:00",3,6]
# # # # # }

# # # # # idx = ['toto', 'titi', 'tata']

# # # # # df = pd.DataFrame(data, index = idx)

# # # # # print(df)

# # # # # df1 = df.T

# # # # # df1['toto'] = pd.to_datetime(df1['toto'], infer_datetime_format=True)
# # # # # df1['toto'] = df1['toto'].dt.strftime('%d/%m/%y')

# # # # # df_final = df1.T

# # # # # print(df_final)

# # # # import pandas as pd

# # # # df = pd.DataFrame({"A":[1,2,3,4], "B":[3,4,5,6], "C":[2,3,4,5]})

# # # # print(df)

# # # # # print(len(df.columns))

# # # # for count in range(len(df.columns)):
# # # #     df.insert(count*2+1, str('col'+str(count+1)), 'NaN')

# # # # print(df)

# # # '''
# # # A	B	C_10	C_20
# # # 0.1	0.2	5	8
# # # 0.3	0.5	2	9
# # # '''



# # data=[{'content': '2018', 'time': 1528186319, 'title': '2018-06-05 16:11:59', 'info': '', 'id': 1}, {'content': '2019', 'time': 1559722345, 'title': '2019-06-05 16:12:25', 'info': '', 'id': 2}, {'content': '017', 'time': 1496650502, 'title': '2017-06-05 16:15:02', 'info': '', 'id': 4}, {'content': '160', 'time': 1465114543, 'title': '2016-06-05 16:15:43', 'info': '', 'id': 5}]


# # import pandas as pd

# # df = pd.DataFrame(data)

# # print(df)


# import pandas as pd    
# df = pd.DataFrame({
#          'A':[177,887,945,412,231,314],
#          'B':[5,3,6,9,2,4],
# })

# print(df)

# import math
# print(df.query('floor(A/100) > 2'))


'''
min max names
1   5   ['a','b']
0   5   ['d']
6   8   ['a','c']
3   4   ['e','a']
'''

import pandas as pd

# df = pd.read_clipboard()

# print(df)

df = pd.DataFrame({"min": [1, 0, 6, 3],
   "max": [5, 5, 8, 4],
   "names": [['a','b'], ['d'], ['a','c'], ['e','a']]})

print(df)

# change these range values as required
min_max = [0, 5]

mask1 = df['min'] >= min_max[0]
mask2 = df['max'] <= min_max[1]

name_set = df[mask1 & mask2]['names'].sum()

print(name_set)