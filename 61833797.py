# # # # # import pandas as pd
# # # # # # import os
# # # # # # import glob

# # # # # # source=r'/home/anshul/youtube'

# # # # # # dest=r'/home/anshul/youtube'

# # # # # # os.chdir(source)

# # # # # # for file in glob.glob("*.xls"):
# # # # # #     df = pd.read_excel(file)
# # # # # #     df.to_csv(dest+file+'.csv', index=False)
# # # # # #     os.remove(file)

# # # # # # import numpy as np


# # # # # table = pd.DataFrame({'id_1': [1, 2, 2, 2, 3, 3],
# # # # #                   'id_2': [3, 4, 5, 3, 2, 1],})

# # # # # # Result_table=pd.DataFrame({'id_1': [1, 2, 2, 2, 3, 3],
# # # # # #           'id_2': [3, 4, 5, 3, 2, 1],
# # # # # #           'Result':[0, 0, 0, 0, 1, 1]})

# # # # # print(table.columns)

# # # # # for row in table:
# # # # #     print(row) #['id_1'], row['id_2'])

# # # # # # table['concat'] = [[row['id_1'], row['id_2']].sort() for row in table]
# # # # # # # int(table['id_1']), int(table['id_2'])

# # # # # # print(table)

# # # # json_inp = '''{
# # # #         "ID": "PRED",
# # # #         "fields": [
# # # #             "id",
# # # #             "name",
# # # #             "parent"
# # # #         ],
# # # #         "items": [
# # # #             {
# # # #                 "ref": "#55:130",
# # # #                 "id": "122",
# # # #                 "values": [
# # # #                     "1904",
# # # #                     "DD",
# # # #                     "PP-PADK"
# # # #                 ],
# # # #                 "relationships": [
# # # #                     {
# # # #                         "screen1": "menu",
# # # #                         "relationships": [
# # # #                             {
# # # #                                 "id": "157"
# # # #                             },
# # # #                             {
# # # #                                 "id": "158"
# # # #                             }
# # # #                         ]
# # # #                     },
# # # #                     {
# # # #                         "screen2": "home",
# # # #                         "relationships": [
# # # #                             {
# # # #                                 "id": "4",
# # # #                                 "relTypeId": 2,
# # # #                                 "relTypeName": "Is required"
# # # #                             },
# # # #                             {
# # # #                                 "id": "7",
# # # #                                 "relTypeId": 2,
# # # #                                 "relTypeName": "Is required"
# # # #                             }
# # # #                         ]
# # # #                     }
# # # #                 ]
# # # #             }
# # # #         ]
# # # #     }'''

# # # # import pandas as pd
# # # # import json

# # # # # df = json.loads(json_inp) #pd.DataFrame()
# # # # # print(df['fields'])
# # # # # print(df['items'][0]['relationships'][0]['relationships'][0]['id'])

# # # # # print(type(df))


# # # # # dataset for read_clipboard()
# # # # # '''
# # # # # COL1 COL2
# # # # # SP1  SEQA
# # # # # SP1  SEQB
# # # # # SP1  SEQC
# # # # # SP2  SEQC
# # # # # SP2  SEQD
# # # # # SP3  SEQA
# # # # # SP4  SEQB
# # # # # SP4  SEQD
# # # # # SP5  SEQL
# # # # # SP6  SEQL
# # # # # '''

# # # # # df = pd.read_clipboard()
# # # # # unique_vals = df.drop_duplicates(['COL1'], keep=False)['COL2'].unique()
# # # # # print(unique_vals)



# # # # # '''
# # # # # Date    ABC
# # # # # 2019-10-18  1.00
# # # # # 2019-11-20  1.01
# # # # # 2019-11-22  1.02
# # # # # 2019-12-20  1.03
# # # # # 2019-12-23  1.04
# # # # # '''

# # # # # df = pd.read_clipboard()
# # # # # df['Date'] = pd.to_datetime(df['Date'])

# # # # # df_new = df.groupby(df['Date'].dt.strftime('%B'))['ABC'].pct_change()
# # # # # print(df_new)

# # # # # print(df.columns)
# # # # # print(df.index)
# # # # # df = df.set_index('Date') #, drop=False
# # # # # print(df)
# # # # # print(df.groupby(month('Date')).pct_change()) #freq='M'

# # # # # df = pd.DataFrame({"id":[1, 1, 1, 2, 2, 2, 2, 3, 3], "val":["A12", "B23", "C34", "A12", "C34", "E45", "F56", "G67", "B23"]})
# # # # # print(df)

# # # # # # df = df.set_index('val') 

# # # # # # print(df)

# # # # # # df_pivot = df.pivot_table(['id'])

# # # # # # print(df_pivot)

# # # # # df_new = pd.crosstab(df.id, df.val).reset_index()

# # # # # print(df_new)

# # # # '''
# # # # Id	A	B	C
# # # # 1	45	78	67
# # # # 2	67	89	76
# # # # 3	67	94	56
# # # # 4	26	78	56
# # # # 5	38 	67	75
# # # # '''


# # # # # import os
# # # # # from multiprocessing import Pool
# # # # # import pandas as pd
# # # # # import time
# # # # # import statistics
    
# # # # # def average(listed_marks):
# # # # #     avg=[]
# # # # #     i=[]
# # # # #     for i in listed_marks:
# # # # #         avg.append(statistics.mean(i))

# # # # #     return avg



# # # # # if __name__ == '__main__':

# # # # #     list_of_marks=[]  

# # # # #     # df = pd.read_csv(r"C:\Users\Radhika\Desktop\RADZ Projects\Xoriant\data.csv")
# # # # #     df = pd.read_clipboard()
# # # # #     # n = df['STUDENT ID'].count() #no of rows
# # # # #     n = df['Id'].count() #no of rows

# # # # #     for i in range(n):  #to obtain the list of lists
# # # # #         a=list(df.iloc[i , 3:6])
# # # # #         a = list(map(int, a)) #converting the lists into int to perform mean
# # # # #         list_of_marks.append(list(a))

# # # # # # ---------------------MP---------------------------------------------------

# # # # #     s1= time.time()    

# # # # #     p = Pool()
# # # # #     avg_mp = p.map(average, list_of_marks) #passed the average function and iterator is a list of list
# # # # #     df['Average'] = avg_mp
# # # # #     p.close()
# # # # #     p.join()

# # # # #     print(f"Processing took {time.time() - s1} using Multi-Processing")


# # # # # import numpy as np 
# # # # # import pandas as pd
# # # # # # pd.set_option('display.max_columns', 500)
# # # # # seed=int(input())
# # # # # n=int(input())
# # # # # p=float(input())
# # # # # i = 1
# # # # # a = np.random.binomial(n, p)
# # # # # s = np.empty(n)
# # # # # while i < n:
# # # # #     a = np.random.binomial(n, p)
# # # # #     np.append(s, a)
# # # # #     i += 1
# # # # # print(s)
# # # # # print(type(s))

# # # # # '''
# # # # #      regiment company deaths battles size
# # # # # 0  Nighthawks     1st    kkk       5    l
# # # # # 1  Nighthawks     1st     52      42   ll
# # # # # 2  Nighthawks     2nd     25       2    l
# # # # # 3  Nighthawks     2nd    616       2    m
# # # # # '''

# # # # # df = pd.read_clipboard()

# # # # # df = df.apply(lambda x: x.astype(str).str.lower())

# # # # # print(df)
# # # # # print(df.columns)


# # # # # arr = [6, 7, 5, 4, 3, 1, 2, 3, 5, 6, 7, 9, 0, 0, 1, 2, 4, 1, 2, 3, 5, 1, 2]
# # # # # idx = [val for val in range(0,len(arr))]

# # # # # df = pd.DataFrame([idx, arr]).T
# # # # # df.columns = ['idx','arr']

# # # # # print(df)

# # # # # total = 13

# # # # # # srt_arr = arr.sort()
# # # # # arr.sort()
# # # # # # print(srt_arr)
# # # # # print(arr)

# # # # # print(sum(arr))

# # # # # for i in range(len(arr)):
# # # # #     if sum(arr[:i]) < total:

# # # # '''
# # # # Date       Open        Close  
# # # # 2016-06-01  17670.85    17423.45
# # # # 2016-06-02  17405.15    17567.80
# # # # 2016-06-03  17657.20    17680.80
# # # # 2016-06-06  17710.45    17671.40
# # # # 2016-06-07  17796.55    17948.15
# # # # 2020-05-11  19610.45    18950.50
# # # # 2020-05-12  18751.40    18862.85
# # # # 2020-05-13  20017.75    19634.95
# # # # 2020-05-14  19197.70    19068.50
# # # # 2020-05-15  19098.80    18833.95
# # # # '''

# # # # # df = pd.read_clipboard()

# # # # # print(df)
# # # # # print(df.columns)

# # # # # # df['change'] = ((df['Close'] - df['Open'])/df['Open'])*100
# # # # # df["prevClose"] = df.Close.shift(1)
# # # # # df['change'] = df[['Open','prevClose']].pct_change(axis=1)['prevClose']

# # # # # # df['change'] = ((df["prevClose"]- df['Open'])/df['Open'])*100

# # # # # print(df)

# # # # '''
# # # # content_duration
# # # # 1.5 
# # # # 39 mins 
# # # # 2.5 
# # # # 3 
# # # # '''

# # # # df = pd.read_clipboard('\t')

# # # # df['content_duration'] = df['content_duration'].apply(lambda x: int(x.replace('mins', '').strip()) * 1/100 if 'mins' in x else x)


# # # # print(df)

# # # import pandas as pd

# # # #Creating dataframe
# # # d = {'col1': [1,2,3,4,5,6,7,8,9,10], 'col2': ['a','b','b','b','c','d','c','a','z','c']}
# # # df = pd.DataFrame(data=d)



# # # filter_set = df['col2'].unique()



# # # for val in filter_set:
# # #     df.loc[df['col2'].str.contains(val)].to_excel("{}.xlsx".format(val))

# # # # #Finding the lines that contain a certain letter
# # # # a = df[df['col2'].str.contains("a")]
# # # # b = df[df['col2'].str.contains("b")]
# # # # c = df[df['col2'].str.contains("c")]

# # # # #importing to excel

# # # # a.to_excel("a.xlsx")
# # # # b.to_excel("b.xlsx")
# # # # c.to_excel("c.xlsx")



# # import pandas as pd
# # import matplotlib.pyplot as plt

# # df2 = pd.read_csv("https://raw.githubusercontent.com/peoplecure/pandoras-box/master/doge.csv")
# # # plt.plot(df2['begins_at'], df2['open_price'])
# # # plt.show()

# # from pandas import DataFrame

# # df = DataFrame(df2)
# # plt.plot(df['begins_at'], df['open_price'])
# # plt.show()


# import pandas as pd

# #Creating dataframe
# d = {'col1': [1,2,3,4,5,6,7,8,9,10], 'col2': ['azs','bdq','bzm','bqm','csm','dqs','cm','a','z','c']}
# df = pd.DataFrame(data=d)

# # assuming you want to search these substrings/characters in col2
# search_str = ['a', 'b', 'c']

# for val in search_str:
#     df.loc[df['col2'].str.contains(val)].to_excel("{}.xlsx".format(val))


'''
SubNo Trails Height Weight Nutrition 
19      1      100    30      Yes      
19      2      400    30      Yes      
19      3      810    10      No       
7       1      911    20      Yes      
7       2      811.   20      Yes      
7       3      811    14      No       
20      1      222    40      Yes      
20      2      222    50      Yes      
20      3      789    30      No 

'''

import pandas as pd

df = pd.read_clipboard()

print(df)