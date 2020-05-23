# # # # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # # # Values	Count_Range
# # # # # # # # # # # # # # # # # # # # # 455	1
# # # # # # # # # # # # # # # # # # # # # 475	2
# # # # # # # # # # # # # # # # # # # # # 479	3
# # # # # # # # # # # # # # # # # # # # # 471	4
# # # # # # # # # # # # # # # # # # # # # 255	1
# # # # # # # # # # # # # # # # # # # # # 220	2
# # # # # # # # # # # # # # # # # # # # # 470	5
# # # # # # # # # # # # # # # # # # # # # 473	6
# # # # # # # # # # # # # # # # # # # # # 151	1
# # # # # # # # # # # # # # # # # # # # # 101	2
# # # # # # # # # # # # # # # # # # # # # 293	3
# # # # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # df = pd.read_clipboard('\t')

# # # # # # # # # # # # # # # # # # # # # df['bins'] = df['Values'] // 100

# # # # # # # # # # # # # # # # # # # # # df['prob'] = df.iloc[:,1].rolling(window=3).mean()

# # # # # # # # # # # # # # # # # # # # # print(df)


# # # # # # # # # # # # # # # # # # # # # from urllib.request import Request, urlopen
# # # # # # # # # # # # # # # # # # # # # from bs4 import BeautifulSoup
# # # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # url = "https://www.countries-ofthe-world.com/world-currencies.html"

# # # # # # # # # # # # # # # # # # # # # req = Request(url, headers={"User-Agent":"Mozilla/5.0"})

# # # # # # # # # # # # # # # # # # # # # webpage=urlopen(req).read()

# # # # # # # # # # # # # # # # # # # # # soup = BeautifulSoup(webpage, "html.parser")

# # # # # # # # # # # # # # # # # # # # # table = soup.find("table", {"class":"codes"})

# # # # # # # # # # # # # # # # # # # # # rows = table.find_all('tr')


# # # # # # # # # # # # # # # # # # # # # columns = [v.text for v in rows[0].find_all('th')] 

# # # # # # # # # # # # # # # # # # # # # print(columns) # ['Country or territory', 'Currency', 'ISO-4217']
# # # # # # # # # # # # # # # # # # # # # print


# # # # # # # # # # # # # # # # # # # # # from networkx import convert_matrix as nx

# # # # # # # # # # # # # # # # # # # # # df = nx.to_pandas_edgelist

# # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # df = pd.DataFrame({'STREAM':['EAGLE','HAWK','NORTH','HAWK','EAGLE','HAWK','NORTH'],'MAT':['A','D','F','D','C','C','E'],'KIS':['B','D','E','D','A','C','D']})

# # # # # # # # # # # # # # # # # # # # # columns = ["A","B","C","D","E", "F"]

# # # # # # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # # # # # # # a = (pd.crosstab(df.STREAM,[df.MAT, df.KIS], margins=True, margins_name='TOTAL').iloc[:,:-1].reindex(columns, axis=1, fill_value=0).rename_axis(None))
# # # # # # # # # # # # # # # # # # # # # # saved = a.to_csv(index=False)
# # # # # # # # # # # # # # # # # # # # # a['TOT'] = a.sum(axis=1)
# # # # # # # # # # # # # # # # # # # # # a['MEAN'] = a.mean(axis=1).round(2)
# # # # # # # # # # # # # # # # # # # # # def x(i):
# # # # # # # # # # # # # # # # # # # # #     if i >5:
# # # # # # # # # # # # # # # # # # # # #         grade='A'
# # # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # # #         grade='E'
# # # # # # # # # # # # # # # # # # # # #     return grade
# # # # # # # # # # # # # # # # # # # # # a['GRD'] = a.MEAN.apply(x)
# # # # # # # # # # # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # created sample data - same example row inserted 5 times. Not ideal but just was trying to test
# # # # # # # # # # # # # # # # # # # # # df = pd.DataFrame({"text": [b"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management", 
# # # # # # # # # # # # # # # # # # # # # b"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management", 
# # # # # # # # # # # # # # # # # # # # # b"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management", 
# # # # # # # # # # # # # # # # # # # # # b"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management", 
# # # # # # # # # # # # # # # # # # # # # b"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management"]})

# # # # # # # # # # # # # # # # # # # # # df = pd.DataFrame({"text": [r"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management", 
# # # # # # # # # # # # # # # # # # # # # r"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management", 
# # # # # # # # # # # # # # # # # # # # # r"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management", 
# # # # # # # # # # # # # # # # # # # # # r"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management", 
# # # # # # # # # # # # # # # # # # # # # r"COMPETENCIES\nBenefits Administration \xe2\x80\x93 Customer Service \xe2\x80\x93 Cost Control \xe2\x80\x93 Recruiting \xe2\x80\x93 Acquisition Management"]})

# # # # # # # # # # # # # # # # # # # # # path=r'/home/anshul/youtube/stackoverflow/resume_dataset.csv'
# # # # # # # # # # # # # # # # # # # # # path2=r'/home/anshul/youtube/stackoverflow/resume_dataset_cleaned.csv'

# # # # # # # # # # # # # # # # # # # # # # path stores the location of the data file downloaded from kaggle
# # # # # # # # # # # # # # # # # # # # # df = pd.read_csv(path)

# # # # # # # # # # # # # # # # # # # # # # remove the binary 'b' prefix reinstated even though the data is 
# # # # # # # # # # # # # # # # # # # # # # read as string during df creation
# # # # # # # # # # # # # # # # # # # # # df['Resume'] = [val[1:].encode('utf-8') for val in df['Resume']]

# # # # # # # # # # # # # # # # # # # # # # create a separate column with multiple decode and encode steps to 
# # # # # # # # # # # # # # # # # # # # # # retrieve the final clean version
# # # # # # # # # # # # # # # # # # # # # df['text_clean'] = df['Resume'].apply(lambda x: x.decode('unicode_escape').\
# # # # # # # # # # # # # # # # # # # # #     encode('ascii', 'ignore').decode('utf-8').strip())

# # # # # # # # # # # # # # # # # # # # # df['text_clean'].to_csv(path2)

# # # # # # # # # # # # # # # # # # # # # print(df['text_clean'])



# # # # # # # # # # # # # # # # # # # # # .encode('utf-8').decode('unicode_escape').encode('ascii', 'ignore').strip()

# # # # # # # # # # # # # # # # # # # # # print(df)
# # # # # # # # # # # # # # # # # # # # # print(df.info())


# # # # # # # # # # # # # # # # # # # # # df['text_clean'] = df['Resume'].apply(lambda x: x.decode('unicode_escape').\
# # # # # # # # # # # # # # # # # # # # #                                           encode('ascii', 'ignore').\
# # # # # # # # # # # # # # # # # # # # #                                           strip())
# # # # # # # # # # # # # # # # # # # # # df['text_clean'] = [val.decode('utf-8') for val in df['text_clean']]

# # # # # # # # # # # # # # # # # # # # # with pd.option_context('display.max_rows', 5, 'display.max_columns', 1):  # more options can be specified also
# # # # # # # # # # # # # # # # # # # # # print(df['text_clean'])
# # # # # # # # # # # # # # # # # # # # # print(df['text_clean'])

# # # # # # # # # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # # # # # # # # import numpy as np

# # # # # # # # # # # # # # # # # # # # # df = pd.DataFrame(np.arange(12).reshape((4, 3)),
# # # # # # # # # # # # # # # # # # # # #                  index=["a", "b", "c", "d"],
# # # # # # # # # # # # # # # # # # # # #                  columns=["a", "b", "c"])


# # # # # # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # # # # # # # df.mask(df.apply(lambda x: x.name == x.index), inplace=True)

# # # # # # # # # # # # # # # # # # # # # print(df)


# # # # # # # # # # # # # # # # # # # # # sentence = input("Give your sentence: ") 
# # # # # # # # # # # # # # # # # # # # # words = sentence.split() 
# # # # # # # # # # # # # # # # # # # # # print(words) 
# # # # # # # # # # # # # # # # # # # # # characters = 0 
# # # # # # # # # # # # # # # # # # # # # for word in words: 
# # # # # # # # # # # # # # # # # # # # #     characters += len(word) 
# # # # # # # # # # # # # # # # # # # # #     average_word_lengt = characters/len(words)

# # # # # # # # # # # # # # # # # # # # # print(characters)
# # # # # # # # # # # # # # # # # # # # # print(average_word_lengt)

# # # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # # Category     Value 
# # # # # # # # # # # # # # # # # # # # A            1     
# # # # # # # # # # # # # # # # # # # # C            5
# # # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # # Category     Value 
# # # # # # # # # # # # # # # # # # # # A            1     
# # # # # # # # # # # # # # # # # # # # B            10
# # # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # df1 = pd.DataFrame({"Category": ['A', 'C'], "Value": [1, 5]})
# # # # # # # # # # # # # # # # # # # # # df2 = pd.DataFrame({"Category": ['A', 'B'], "Value": [1, 10]})

# # # # # # # # # # # # # # # # # # # # # print(df1)
# # # # # # # # # # # # # # # # # # # # # print(df2)

# # # # # # # # # # # # # # # # # # # # # df3 = df1.merge(df2, how='outer', on=['Category'], suffixes=('_l', '_r'))
# # # # # # # # # # # # # # # # # # # # # df3['Value'] = df3['Value_l'].fillna(0) + df3['Value_r'].fillna(0)
# # # # # # # # # # # # # # # # # # # # # df3 = df3[['Category', 'Value']]


# # # # # # # # # # # # # # # # # # # # # print(df3)


# # # # # # # # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # # # # # # # import numpy as np

# # # # # # # # # # # # # # # # # # # # conversion = [["a",5],["b",1],["c",10]]
# # # # # # # # # # # # # # # # # # # # conversion_table = pd.DataFrame(conversion,columns=['Variable','Cost'])

# # # # # # # # # # # # # # # # # # # # data1 = [[1,"3a+b"],[2,"c"],[3,"2c"]]
# # # # # # # # # # # # # # # # # # # # to_solve = pd.DataFrame(data1,columns=['Day','Q1'])

# # # # # # # # # # # # # # # # # # # # desired = [[1,16],[2,10],[3,20]]
# # # # # # # # # # # # # # # # # # # # desired_table=pd.DataFrame(desired,columns=['Day','Q1 solved'])

# # # # # # # # # # # # # # # # # # # # print(conversion_table)
# # # # # # # # # # # # # # # # # # # # print(to_solve)
# # # # # # # # # # # # # # # # # # # # print(desired_table)

# # # # # # # # # # # # # # # # # # # # equn = to_solve['Q1']

# # # # # # # # # # # # # # # # # # # # val=0

# # # # # # # # # # # # # # # # # # # # for eq in equn:
# # # # # # # # # # # # # # # # # # # #     for i in range(len(eq)):
# # # # # # # # # # # # # # # # # # # #         if(eq[i].isdigit()):
# # # # # # # # # # # # # # # # # # # #             val += int(eq[i])
# # # # # # # # # # # # # # # # # # # #         elif(eq[i].isalpha() & i>0 & eq[i-1].isdigit()):
# # # # # # # # # # # # # # # # # # # #             val *= eq[i]
# # # # # # # # # # # # # # # # # # # #         elif(eq[i].isalpha() & i>0):
# # # # # # # # # # # # # # # # # # # #             if
# # # # # # # # # # # # # # # # # # # #     print()

# # # # # # # # # # # # # # # # # # # # # print(equn)

# # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # month_year  Date_of_basket_entry
# # # # # # # # # # # # # # # # # # # 03/2017 01.04.2005
# # # # # # # # # # # # # # # # # # # 02/2019 01.01.1995
# # # # # # # # # # # # # # # # # # # 07/2017 None
# # # # # # # # # # # # # # # # # # # 02/2017 None
# # # # # # # # # # # # # # # # # # # 04/2017 01.01.2020
# # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # df = pd.read_clipboard()
# # # # # # # # # # # # # # # # # # # print(df.columns)

# # # # # # # # # # # # # # # # # # # # df['month_year'] = pd.to_datetime(df['month_year'], format="%m/%Y")


# # # # # # # # # # # # # # # # # # # # df.loc[df['Date_of_basket_entry'] == 'None']['Date_of_basket_entry'] = 
# # # # # # # # # # # # # # # # # # # # # df['Date_of_basket_entry'] = pd.to_datetime(df[df['Date_of_basket_entry'] == 'None'], format="%m.%d.%Y")

# # # # # # # # # # # # # # # # # # # # print(df)
# # # # # # # # # # # # # # # # # # # import numpy as np
# # # # # # # # # # # # # # # # # # # from datetime import datetime
# # # # # # # # # # # # # # # # # # # # df.loc[:,'Date_of_basket_boolean'] = np.where((df.Date_of_basket_entry.isna()) | (df.Date_of_basket_entry < df.month_year) , 0, 1)

# # # # # # # # # # # # # # # # # # # df['month_year'] = pd.to_datetime(df['month_year'], format="%m/%Y")
# # # # # # # # # # # # # # # # # # # print(df.loc[df['Date_of_basket_entry'] == 'None']['Date_of_basket_entry'])
# # # # # # # # # # # # # # # # # # # df.loc[df['Date_of_basket_entry'] == 'None']['Date_of_basket_entry'] = datetime.today().strftime(format="%m.%d.%Y")
# # # # # # # # # # # # # # # # # # # df['Date_of_basket_entry'] = pd.to_datetime(df['Date_of_basket_entry'], format="%m.%d.%Y")
# # # # # # # # # # # # # # # # # # # # df.loc[:,'Date_of_basket_boolean'] = np.where((df.Date_of_basket_entry.notna()) | (df.Date_of_basket_entry < df.month_year) , 0, 1)

# # # # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # lst = ['UserA', 'UserB', 'UserC', 'UserD','UserB', 'UserC']
# # # # # # # # # # # # # # # # # # lst2 = ['X', 'Y', 'Z', 'Y','X','Z'] 

# # # # # # # # # # # # # # # # # # dm = pd.DataFrame(list(zip(lst, lst2)), columns =['Name', 'val']) 
# # # # # # # # # # # # # # # # # # dm['count']= 1
# # # # # # # # # # # # # # # # # # dm.groupby(['Name','val']).count()

# # # # # # # # # # # # # # # # # # # df_piv = pd.crosstab(df['Name'], df['val'])
# # # # # # # # # # # # # # # # # # df_piv = dm.groupby(['Name','val']).count()['count'].unstack('val', fill_value='')

# # # # # # # # # # # # # # # # # # print(dm)
# # # # # # # # # # # # # # # # # # print(df_piv)

# # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # 0        4.0
# # # # # # # # # # # # # # # # # 1        5.0
# # # # # # # # # # # # # # # # # 2        5.0
# # # # # # # # # # # # # # # # # 3        4.0
# # # # # # # # # # # # # # # # # 4        4.0
# # # # # # # # # # # # # # # # # 82624    3.0
# # # # # # # # # # # # # # # # # 82625    4.5
# # # # # # # # # # # # # # # # # 82626    4.0
# # # # # # # # # # # # # # # # # 82627    5.0
# # # # # # # # # # # # # # # # # 82628    4.5
# # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # df = pd.read_clipboard()
# # # # # # # # # # # # # # # # # df.columns = ['no', 'rating']

# # # # # # # # # # # # # # # # # df['rating'] = df['rating'].astype('int')

# # # # # # # # # # # # # # # # # print(df)


# # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # ID    ID2       DATE       Status
# # # # # # # # # # # # # # # # 23    10     2019-06-11     Sent
# # # # # # # # # # # # # # # # 23    20     2019-06-21     Sent
# # # # # # # # # # # # # # # # 23    30     2019-06-26     Sent
# # # # # # # # # # # # # # # # 23    40     2019-06-27     Sent
# # # # # # # # # # # # # # # # 23    50     2019-12-02     Sent
# # # # # # # # # # # # # # # # '''


# # # # # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # # # import datetime as dt
# # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # df['FMT_DATE'] = pd.to_datetime(df['DATE'], format="%Y-%m-%d")
# # # # # # # # # # # # # # # # df['YEAR']

# # # # # # # # # # # # # # # # print(df)
# # # # # # # # # # # # # # # # print(df.columns)



# # # # # # # # # # # # # # # # # id = df.groupby(['ID'], as_index = False)
# # # # # # # # # # # # # # # # # id_dict = {}

# # # # # # # # # # # # # # # # # all_df = id.get_group(ID)

# # # # # # # # # # # # # # # # # letter_count = 0
# # # # # # # # # # # # # # # # # for index, row in all_df.iterrows():
# # # # # # # # # # # # # # # # #         if ((row['Status'] == 'Sent')):
# # # # # # # # # # # # # # # # #             letter_count = letter_count + 1

# # # # # # # # # # # # # # # # # id_dict.update({ID:letter_count})
# # # # # # # # # # # # # # # # # df['letter_count'] = df['ID'].map(id_dict)




# # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # def filter(df, foo="df['foo']"):
# # # # # # # # # # # # # # #     newdf = df[df['foo']==eval(foo)]
# # # # # # # # # # # # # # #     print(newdf)

# # # # # # # # # # # # # # # data = {
# # # # # # # # # # # # # # #     'foo': ['First value', 'Second value'],
# # # # # # # # # # # # # # #     'bar': ['First value', 'Second value']
# # # # # # # # # # # # # # #     }

# # # # # # # # # # # # # # # df = pd.DataFrame(data, columns = ['foo', 'bar'])

# # # # # # # # # # # # # # # filter(df, "'First value'") # 

# # # # # # # # # # # # # # data = {
# # # # # # # # # # # # # #   "process": "1",
# # # # # # # # # # # # # #   "description": "some more details"
# # # # # # # # # # # # # # }

# # # # # # # # # # # # # # print(data['description'])

# # # # # # # # # # # # # # li = []
# # # # # # # # # # # # # # li2 = ['A', 'B', 'C', 'D']

# # # # # # # # # # # # # # # strg=''

# # # # # # # # # # # # # # # li = [map(lambda x,y:x+y, val,strg) for val in li2]
# # # # # # # # # # # # # # # # [lambda x: x+val for val in li2]
# # # # # # # # # # # # # # # print(li)

# # # # # # # # # # # # # # from itertools import accumulate

# # # # # # # # # # # # # # li = list(accumulate(li2, lambda x,y: x+y))
# # # # # # # # # # # # # # # ['A', 'AB', 'ABC', 'ABCD']

# # # # # # # # # # # # # # print(li)


# # # # # # # # # # # # # zeros = [0, 0, 0, 0]
# # # # # # # # # # # # # outp=[]

# # # # # # # # # # # # # for key, val in enumerate(zeros):
# # # # # # # # # # # # #     temp = zeros.copy()
# # # # # # # # # # # # #     temp[key] = 1
# # # # # # # # # # # # #     outp.append(tuple(temp))
    
# # # # # # # # # # # # # print(outp)

# # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # '''
# # # # # # # # # # # #     id  colA colB
# # # # # # # # # # # # 0   1   4    1
# # # # # # # # # # # # 1   2   5    2
# # # # # # # # # # # # 2   3   2    4
# # # # # # # # # # # # 3   4   4    2
# # # # # # # # # # # # 4   5   2    4
# # # # # # # # # # # # '''

# # # # # # # # # # # # '''
# # # # # # # # # # # #     id  colA colB colC
# # # # # # # # # # # # 0   1   4    1    0
# # # # # # # # # # # # 1   2   5    2    0
# # # # # # # # # # # # 2   5   2    4    0
# # # # # # # # # # # # '''

# # # # # # # # # # # # df1 = pd.read_clipboard()

# # # # # # # # # # # # df2 = df1.loc[df1['id'].isin(['1','2','5'])]
# # # # # # # # # # # # df2['colC'] = 0


# # # # # # # # # # # # df3 = df1.loc[~df1['id'].isin(list(df2['id']))]

# # # # # # # # # # # # print(df3)
# # # # # # # # # # # # # print(df2)

# # # # # # # # # # # import pandas as pd

# # # # # # # # # # # alphabet_list = ['a','b','c','d','e','f']

# # # # # # # # # # # master_df = pd.DataFrame()

# # # # # # # # # # # for letter in alphabet_list:

# # # # # # # # # # #     player_df = pd.read_html('https://www.nfl.com/players/active/{}'.format(letter))

# # # # # # # # # # #     master_df = master_df.append(player_df)

# # # # # # # # # # # print(master_df)

# # # # # # # # # # import pandas as pd

# # # # # # # # # # '''
# # # # # # # # # #    id   year    month      target1  
# # # # # # # # # # 0  324  2019.0  1.0        100.0
# # # # # # # # # # 1  325  2019.0  3.0        100.0
# # # # # # # # # # 2  326  2019.0  10.0       100.0
# # # # # # # # # # 3  327  2019.0  11.0       100.0
# # # # # # # # # # 5  328  2020.0  4.0       100.0
# # # # # # # # # # 6  329  2020.0  12.0       100.0
# # # # # # # # # # 7  330  2020.0  2.0       100.0
# # # # # # # # # # '''

# # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # df1 = df.loc[df['year'] <= 2019].join(df.loc[df['month'] <= 10], how='', lsuffix='_l', rsuffix='_r')  #.loc[df['month'] <= 10]

# # # # # # # # # # print(df1)

# # # # # # # # # # # print(df)


# # # # # # # # # import pyap
# # # # # # # # # test_address = """
# # # # # # # # #    4998 Stairstep Lane Toronto ON   
# # # # # # # # #     """
# # # # # # # # # addresses = pyap.parse(test_address, country='CA')
# # # # # # # # # for address in addresses:
# # # # # # # # #         # shows found address
# # # # # # # # #         print(address)
# # # # # # # # #         # shows address parts
# # # # # # # # #         print(address.as_dict())

# # # # # # # # # addresses.apply(lambda x: pyap.parse(x['address'], country='CA'),axis=1)

# # # # # # # # '''
# # # # # # # # productNum  productOMS  productPrice
# # # # # # # # 2463448  1002623073  419.95
# # # # # # # # 2463448  sample_text#@$#%#_test  239.95
# # # # # # # # 2463448  1002623073  4239.95
# # # # # # # # 2463448  sample_text#@$#%#_test  4124.95
# # # # # # # # 2463448  1002623073  249.95
# # # # # # # # 2463448  1002623073  454549.95
# # # # # # # # '''

# # # # # # # # import pandas as pd

# # # # # # # # df = pd.read_clipboard()

# # # # # # # # print(df)

# # # # # # # # df1 = df.loc[df['productOMS'].str.contains('[0-9]+')]

# # # # # # # # print(df1)

# # # # # # # import pandas as pd 
# # # # # # # pincodes=[800678,800456]
# # # # # # # numbers=[2567890,256757]
# # # # # # # labels=['R','M']
# # # # # # # first=pd.DataFrame({'Number':numbers, 'Pincode':pincodes},index=labels)
# # # # # # # print(first)




# # # # # # import os
# # # # # # import glob
# # # # # # import pandas as pd

# # # # # # # replace "/dir" with the location that contains the files
# # # # # # os.chdir("/home/anshul/youtube/stackoverflow/csv_files/")

# # # # # # extn = 'csv'
# # # # # # filenames = [i for i in glob.glob('*.{}'.format(extn))]

# # # # # # combined_csv = pd.concat([pd.read_csv(f) for f in filenames ])
# # # # # # combined_csv.to_csv( "/home/anshul/youtube/stackoverflow/csv_files/combined_csv.csv", index=False)


# # # # # # # , encoding='utf-8-sig'

# # # # # '''
# # # # # a,b,4
# # # # # b,c,5
# # # # # a,c,3
# # # # # a,a,0
# # # # # b,b,0
# # # # # c,c,0
# # # # # b,a,4
# # # # # c,b,5
# # # # # c,a,3
# # # # # '''

# # # # # import pandas as pd

# # # # # df = pd.read_clipboard()

# # # # # print(df)

# # # # # df1 = df.as_matrix()

# # # # # print(df1)

# # # # '''
# # # # A  B  C
# # # # 1  2  4
# # # # 2  4  6
# # # # 8  10 12
# # # # 1  3  5 
# # # # '''

# # # # import pandas as pd

# # # # df = pd.read_clipboard()

# # # # print(df)


# # # lst1 = ['A1 B1 C1', 'A2 B2 D1', 'S1 M1 A3', 'A4 B3 G1','H1 K1 W1']

# # # import pandas as pd

# # # lst = ['A', 'B', 'C', 'D']
# # # print(''.join(lst))

# # # df = pd.DataFrame(columns=lst)

# # # # print(df)

# # # tmp_dict = {}

# # # for strg in lst1:
# # #     strg = strg.split()
# # #     for i in strg:
# # #         if i[0] in ''.join(lst):
            


# # #     # for val in lst:
# # #     #     if val in strg    



# # import pandas as pd

# # lst1 = ['A1 B1 C1', 'A2 B2 D1', 'S1 M1 A3', 'A4 B3 G1','H1 K1 W1']



# # cols = ['A', 'B', 'C', 'D']   ### cols for each string
# # df = pd.DataFrame(columns=cols)

# # ### Populating values
# # for elt in lst1:
# #     new = {}
# #     for sub_elt in elt.split(" "):
# #         if sub_elt[0] in cols:
# #             new[sub_elt[0]] = sub_elt
# #     df = df.append(pd.Series(new), ignore_index=True)

# # print(df)

# import pandas as pd

# lst1 = ['A1 B1 C1', 'A2 B2 D1', 'S1 M1 A3', 'A4 B3 G1','H1 K1 W1']

# df = pd.DataFrame()

# for lst in lst1:
#     df = df.append([sorted(lst.split())])

# print(df)