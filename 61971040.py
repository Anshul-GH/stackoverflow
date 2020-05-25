# # # # # # # # # # import glob
# # # # # # # # # # from zipfile import ZipFile
# # # # # # # # # # import pandas as pd

# # # # # # # # # # path = r'/home/anshul/youtube/stackoverflow/zip_files' # use your path

# # # # # # # # # # #load all zip files in folder
# # # # # # # # # # all_files = glob.glob(path + "/*.zip")
# # # # # # # # # # # print(all_files)

# # # # # # # # # # df_master = pd.DataFrame()
# # # # # # # # # # flag = False

# # # # # # # # # # for filename in all_files:    
# # # # # # # # # #     zip_file = ZipFile(filename)
# # # # # # # # # #     for text_file in zip_file.infolist():
# # # # # # # # # #         if text_file.filename.endswith('Bezirke.csv'):
# # # # # # # # # #             df = pd.read_csv(zip_file.open(text_file.filename), 
# # # # # # # # # #             delimiter=';', 
# # # # # # # # # #             header=0, 
# # # # # # # # # #             index_col=['Timestamp'], 
# # # # # # # # # #             parse_dates=['Timestamp']
# # # # # # # # # #             )
# # # # # # # # # #     if not flag:
# # # # # # # # # #         df_master = df
# # # # # # # # # #         flag = True
# # # # # # # # # #     else:
# # # # # # # # # #         df_master = pd.concat([df_master, df])

# # # # # # # # # # print(df_master)    

# # # # # # # # #     # print(tmp_dict)
# # # # # # # # #     # df = pd.DataFrame(tmp_dict, index=['Timestamp'])

# # # # # # # # #     # if idx == 0:
# # # # # # # # #     #     df_master = df
# # # # # # # # #     #     idx += 1
# # # # # # # # #     # else:
# # # # # # # # #     #     df_master = pd.concat([df_master, df])

# # # # # # # # # #print dataframe in console
# # # # # # # # # # print(df_master)

# # # # # # # # # #prepare date to export to csv
# # # # # # # # # # frame = pd.concat(df, axis=0)

# # # # # # # # # #export to csv
# # # # # # # # # # frame.to_csv( "combined_zip_Bezirke.csv", encoding='utf-8-sig')
# # # # # # # # # # print("Export to CSV Successful")

# # # # # # # # # import pandas as pd
# # # # # # # # # import numpy as np

# # # # # # # # # cycling = pd.DataFrame(
# # # # # # # # #     {
# # # # # # # # #         'qty' : [1,0,2,1,1],
# # # # # # # # #         'item' : ['frame','frame',np.nan,'order including a saddle and other things','brake'],
# # # # # # # # #         'desc' : [np.nan,['bike','wheel'],['bike',['tire','tube']],['saddle',['seatpost','bag']],['bike','brakes']]
# # # # # # # # #     }
# # # # # # # # # )

# # # # # # # # # print(cycling)

# # # # # # # # import pandas as pd

# # # # # # # # df = pd.DataFrame({'id':[1,1,1,1,1,1,1,1,1,1],
# # # # # # # #                    'speed':[10,0,0,20,20,15,0,0,0,10],
# # # # # # # #                    'time':['2020-01-17 18:43:29',
# # # # # # # #                              '2020-01-17 18:43:48',
# # # # # # # #                              '2020-01-17 18:44:09',
# # # # # # # #                              '2020-01-17 18:44:28',
# # # # # # # #                              '2020-01-17 18:44:48',
# # # # # # # #                              '2020-01-17 18:46:05',
# # # # # # # #                              '2020-01-17 18:47:15',
# # # # # # # #                              '2020-01-17 18:47:24',
# # # # # # # #                              '2020-01-17 18:53:07',
# # # # # # # #                              '2020-01-17 18:58:36']})
# # # # # # # # df['time']=pd.to_datetime(df['time'])

# # # # # # # # df['time_diff']=(df['time'].shift(-1)-df['time']).dt.seconds

# # # # # # # # print(df)

# # # # # # # # df1 = df['time_diff'].cumsum()

# # # # # # # # print(df1)

# # # # # # # import pandas as pd

# # # # # # # df = pd.read_csv(r"/home/anshul/youtube/stackoverflow/College_Data")

# # # # # # # # print(df)
# # # # # # # # print(df.columns)
# # # # # # # # print(df.index)

# # # # # # # df.to_excel("/home/anshul/youtube/stackoverflow/College_Data.xlsx")

# # # # # # import pandas as pd

# # # # # # df = pd.DataFrame({'id': ['id1', 'id1', 'id2', 'id2'],
# # # # # #                   'value': ['1', '2', '10', '20'],
# # # # # #                   'index': ['day1', 'day2', 'day1', 'day2']})

# # # # # # print(df)

# # # # # # df1 = df.pivot('index', 'id', 'value')

# # # # # # print(df1)


# # # # # import pandas as pd
# # # # # df = pd.DataFrame({'A thing': 'foo bar foo bar foo bar foo foo'.split(),
# # # # #                    'B thing': 'one one two three two two one three'.split()})
# # # # # print(df.columns)
# # # # # print("=============")
# # # # # print( df.query('`A thing` == "bar"') )
# # # # # # print(df.query('"A thing" == "bar"'))
# # # # # # df1 = df.loc[df['A thing'] == "bar"]
# # # # # # print(df1)


# # # # # # import pandas as pd
# # # # # # df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
# # # # # #                    'B': 'one one two three two two one three'.split()})
# # # # # # print(df)
# # # # # # print("=============")
# # # # # # print( df.query('A== "bar"') )

# # # # # import pandas as pd
# # # # # print(pd.__version__)

# # # # '''
# # # # a	b	c	d
# # # # 1	2020-01-20 01:00:00	32	jajskdn
# # # # 2	NaN	23	2aksn
# # # # 3	2020-05-20 02:00:00	asjn	sdn
# # # # 4	NaN	sdn	cas
# # # # 7	NaN	nf	cka
# # # # '''

# # # # import pandas as pd
# # # # # from datetime import datetime

# # # # df = pd.read_clipboard('\t')

# # # # print(df)

# # # # df1 = df.loc[df['b'].notna()] #.tz_convert('America/New_York')
# # # # # df1['b'] = pd.to_datetime(df1['b'])
# # # # # df1['b'] = df1['b'].tz_localize('UTC').tz_convert('US/Eastern')
# # # # df1['b'] = pd.to_datetime(df1['b']).dt.tz_localize('UTC').dt.tz_convert('America/New_York')

# # # # df_converted = pd.concat([df1, df.loc[df['b'].isna()]]).sort_values(['a'])

# # # # # print(type(df1['b']))
# # # # # pd.to_datetime(

# # # # # print(df1.tz_convert('America/New_York'))

# # # # # .tz_convert['America/New_York']

# # # # print(df1)
# # # # print(df_converted)

# # # '''
# # #                  Iris-setosa  Iris-versicolor  Iris-virginica
# # # Iris-setosa                4                0               0
# # # Iris-versicolor            0                1               3
# # # Iris-virginica             0                0               7
# # # '''
# # # '''
# # # 	Iris-setosa	Iris-versicolor	Iris-virginica
# # # Iris-setosa	6	0	0
# # # Iris-versicolor	0	2	2
# # # Iris-virginica	0	0	5
# # # '''

# # # import pandas as pd

# # # df1 = pd.read_clipboard()

# # # print(df1)

# # # df2 = df1.copy()
# # # df2['Iris-setosa'][0] = 4
# # # df2['Iris-versicolor'][1] = 1
# # # df2['Iris-virginica'][1] = 3
# # # df2['Iris-virginica'][2] = 7

# # # print(df1.reset_index(drop=True))
# # # print(df2.reset_index(drop=True))

# # # df3 = df1 + df2

# # # print(df3)

# # import pandas as pd
# # import numpy as np

# # df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
# #                              'foo', 'bar', 'foo', 'foo',
# #                          'foo', 'bar', 'foo', 'bar',
# #                              'foo', 'bar', 'foo', 'foo', 'bar'],
# #                        'B' : ['one', 'one', 'two', 'three',
# #                              'two', 'two', 'one', 'three',
# #                              'one', 'one', 'two', 'three',
# #                              'two', 'two', 'one', 'three', 'four'],
# #                        'C' : np.random.randn(17), 'D' : np.random.randn(17)})

# # print(df)

# # parts = 4



# # for part in range(parts):


# '''
# Branch	City	count
# 0	A	Naypyitaw	2
# 1	A	Yangon	292
# 2	B	Mandalay	289
# 3	C	Naypyitaw	289
# '''

# # sample data I created to match your requirement as per the description
# '''
# Branch	City
# A	Naypyitaw
# A	Yangon
# A	Yangon
# A	Yangon
# A	Yangon
# B	Mandalay
# B	Mandalay
# B	Yangon
# C	Naypyitaw
# C	Naypyitaw
# C	Naypyitaw
# C	Mandalay
# '''

# import pandas as pd

# df = pd.read_clipboard()

# df1 = df.groupby(['Branch','City']).size().reset_index().rename(columns={0:'count'}).sort_values(['count'], ascending=False)
# print(df1)

# df2 = df1.groupby(['Branch']).max().reset_index()
# print(df2)

# df['City'] = df['Branch'].map(df2.set_index('Branch')['City'])
# print(df)

# # df3 = df.join(df2[['Branch', 'City']], on=['Branch'], how='left', lsuffix='_l', rsuffix='_r')

# # df3 = pd.concat([df, df2], axis=1, sort=False)

# # print(df3)

# df['City'] = df['Branch'].map(df2.set_index('Branch')['City'])

# # df1['Sex'] = df1['Name'].map(df2.set_index('Name')['Sex'])

# # df1[['Branch', 'count']].groupby(['Branch']).max()
#  #df1.loc[df1['count'].max()]

# print(df)
# # print(df2)
# # mask = df1.loc[df['Branch']]




import requests
from bs4 import BeautifulSoup

# Send GET request
r = requests.get('https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=c.1789.hamburger_menu_fly_out_banner&_lc=Vk4wMzkwMTUwMDk=')

# Parse HTML text
soup = BeautifulSoup(r.text, 'html.parser')

# def scrape_tiki(url="https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=c.1789.hamburger_menu_fly_out_banner&_lc=Vk4wMzkwMTUwMDk="):

# Get parsed HTML
#     soup = get_url(url)


product = soup.find('div',{'class','product-item'})

rating = product.find('span',{'class':'rating-content'})
print (rating)