# # # # # # # # # # # # # # # # # # # # # # # from pandas import to_datetime

# # # # # # # # # # # # # # # # # # # # # # # val = to_datetime("2020-01-01", format='%Y-%m-%d')

# # # # # # # # # # # # # # # # # # # # # # # print(val)

# # # # # # # # # # # # # # # # # # # # # # # sample dummy data I created based on the 6 rows shared in the question
# # # # # # # # # # # # # # # # # # # # # # # made sure that a couple of stocks cross the 80% barrier
# # # # # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # # # # Date    Stock   Volume
# # # # # # # # # # # # # # # # # # # # # # 01/02    APPL   1000000
# # # # # # # # # # # # # # # # # # # # # # 01/02    YUSS     200000
# # # # # # # # # # # # # # # # # # # # # # 01/02    DISN    1500000
# # # # # # # # # # # # # # # # # # # # # # 02/02    APPL    100000
# # # # # # # # # # # # # # # # # # # # # # 02/02    YUSS   1250000
# # # # # # # # # # # # # # # # # # # # # # 02/02    DISN    2000000
# # # # # # # # # # # # # # # # # # # # # # 03/02    APPL    100000
# # # # # # # # # # # # # # # # # # # # # # 03/02    YUSS   1250000
# # # # # # # # # # # # # # # # # # # # # # 03/02    DISN    2000000
# # # # # # # # # # # # # # # # # # # # # # 04/02    APPL    100000
# # # # # # # # # # # # # # # # # # # # # # 04/02    YUSS   1250000
# # # # # # # # # # # # # # # # # # # # # # 04/02    DISN    2000000
# # # # # # # # # # # # # # # # # # # # # # 05/02    APPL    100000
# # # # # # # # # # # # # # # # # # # # # # 05/02    YUSS   1250000
# # # # # # # # # # # # # # # # # # # # # # 05/02    DISN    2000000
# # # # # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # # # # # # # filter = 500000

# # # # # # # # # # # # # # # # # # # # # # df['vol_flag'] = [1 if val > filter else 0 for val in df['Volume']]

# # # # # # # # # # # # # # # # # # # # # # df1 = df.groupby(['Stock', 'Date']).sum().reset_index()[['Stock', 'vol_flag']]

# # # # # # # # # # # # # # # # # # # # # # df2 = df1.groupby(level=['Stock']).apply(lambda g: g / g.sum())

# # # # # # # # # # # # # # # # # # # # # # print(df2)


# # # # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # # # d1 = {'data': ['python','Python','PYTHON','conda', 'COnda', 'CONDA', ],
# # # # # # # # # # # # # # # # # # # # #         'Value': [50,25,30,25,40,25]
# # # # # # # # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # # # # # # # # df = pd.DataFrame(d1, columns = ['data', 'Value']) 

# # # # # # # # # # # # # # # # # # # # # df['data'] = [val.title() for val in df['data']]

# # # # # # # # # # # # # # # # # # # # # df1 = df.groupby('data', sort=False).sum().reset_index()

# # # # # # # # # # # # # # # # # # # # # print(df1)

# # # # # # # # # # # # # # # # # # # # my_list = ['a,b,c']

# # # # # # # # # # # # # # # # # # # # my_list = ''.join(my_list).split(',')

# # # # # # # # # # # # # # # # # # # # print(my_list)
# # # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # # key value
# # # # # # # # # # # # # # # # # # # 2   21
# # # # # # # # # # # # # # # # # # # 2   32
# # # # # # # # # # # # # # # # # # # 2   455
# # # # # # # # # # # # # # # # # # # 3   12
# # # # # # # # # # # # # # # # # # # 3   45
# # # # # # # # # # # # # # # # # # # 3   21
# # # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # # # # # df.index = df['key']
# # # # # # # # # # # # # # # # # # # # # df = df['value']

# # # # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # # # # # # dct = df.to_dict('records')

# # # # # # # # # # # # # # # # # # # d = df.groupby(['key'])['value'].agg(list).to_dict()

# # # # # # # # # # # # # # # # # # # print(d)

# # # # # # # # # # # # # # # # # # # # print(dct)
# # # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # # # Users     ActivityCount
# # # # # # # # # # # # # # # # # # User0     220
# # # # # # # # # # # # # # # # # # User1     190
# # # # # # # # # # # # # # # # # # User2     105
# # # # # # # # # # # # # # # # # # User3     109
# # # # # # # # # # # # # # # # # # User4     271
# # # # # # # # # # # # # # # # # # User5     265
# # # # # # # # # # # # # # # # # # User95     64
# # # # # # # # # # # # # # # # # # User96     15
# # # # # # # # # # # # # # # # # # User97    168
# # # # # # # # # # # # # # # # # # User98    251
# # # # # # # # # # # # # # # # # # User99    278
# # # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # # # print(df)

# # # # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # # #    year product_name  billamount
# # # # # # # # # # # # # # # # # 0  2016        Sugar  37760979.0
# # # # # # # # # # # # # # # # # 1  2018        Sugar        25.0
# # # # # # # # # # # # # # # # # 2  2019        Sugar         NaN
# # # # # # # # # # # # # # # # # 3  2016     Kerosene  31576566.0
# # # # # # # # # # # # # # # # # 4  2017          NaN        14.0
# # # # # # # # # # # # # # # # # 5  2018     Kerosene         7.0
# # # # # # # # # # # # # # # # # 6  2016    ToorDhall  27108315.0
# # # # # # # # # # # # # # # # # 7  2019    ToorDhall       240.0
# # # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # # # df1 = df.loc[df['product_name'].notna()].loc[df['billamount'].notna()]

# # # # # # # # # # # # # # # # # print(df1)


# # # # # # # # # # # # # # # # response = '''
# # # # # # # # # # # # # # # # [
# # # # # # # # # # # # # # # # {
# # # # # # # # # # # # # # # #     "_index": "product",
# # # # # # # # # # # # # # # #     "_type": "_doc",
# # # # # # # # # # # # # # # #     "_id": "23234sdf",
# # # # # # # # # # # # # # # #     "_score": 2.2295187,
# # # # # # # # # # # # # # # #     "_source": {
# # # # # # # # # # # # # # # #         "SERP_KEY": "",
# # # # # # # # # # # # # # # #         "r_variant_info": "",
# # # # # # # # # # # # # # # #         "s_asin": "",
# # # # # # # # # # # # # # # #         "pid": "394",
# # # # # # # # # # # # # # # #         "r_gtin": "00838128000547",        
# # # # # # # # # # # # # # # #         "additional_attributes_remarks": "publisher:0|size:0",            
# # # # # # # # # # # # # # # #         "s_gtin": "",            
# # # # # # # # # # # # # # # #         "r_category": "",
# # # # # # # # # # # # # # # #         "confidence_score": "2.4545",      
# # # # # # # # # # # # # # # #         "title_match": "45.45"
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # # },
# # # # # # # # # # # # # # # # {
# # # # # # # # # # # # # # # #     "_index": "product",
# # # # # # # # # # # # # # # #     "_type": "_doc",
# # # # # # # # # # # # # # # #     "_id": "23234sdf",
# # # # # # # # # # # # # # # #     "_score": 2.2295187,
# # # # # # # # # # # # # # # #     "_source": {
# # # # # # # # # # # # # # # #         "SERP_KEY": "",
# # # # # # # # # # # # # # # #         "r_variant_info": "",
# # # # # # # # # # # # # # # #         "s_asin": "",
# # # # # # # # # # # # # # # #         "pid": "394",
# # # # # # # # # # # # # # # #         "r_gtin": "00838128000547",        
# # # # # # # # # # # # # # # #         "additional_attributes_remarks": "publisher:0|size:0",            
# # # # # # # # # # # # # # # #         "s_gtin": "",            
# # # # # # # # # # # # # # # #         "r_category": "",
# # # # # # # # # # # # # # # #         "confidence_score": "2.4545",      
# # # # # # # # # # # # # # # #         "title_match": "45.45"
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # # }
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # # from pandas.io import json as js
# # # # # # # # # # # # # # # # import json

# # # # # # # # # # # # # # # # data = json.loads(response)
# # # # # # # # # # # # # # # # df = js.json_normalize(data)
# # # # # # # # # # # # # # # # print(df.columns)

# # # # # # # # # # # # # # # # # these are the columns that you get in the final dataframe

# # # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # # col1	col2
# # # # # # # # # # # # # # # A	[{'Id':42,'prices':['30','78']},{'Id': 44,'prices':['20','47','89']}]
# # # # # # # # # # # # # # # B	[{'Id':47,'prices':['30','78']},{'Id':94,'prices':['20']},{'Id':84,'prices':['20','98']}]
# # # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # # df1 = df.set_index("col1")["col2"].str.strip("[]").str.replace("’", "'").map(eval).apply(
# # # # # # # # # # # # # # #     pd.Series
# # # # # # # # # # # # # # # ).stack().apply(pd.Series).reset_index(0).reset_index(drop=True)

# # # # # # # # # # # # # # # print(df1)

# # # # # # # # # # # # # # '''
# # # # # # # # # # # # # # Time                         Event   Location    ID
# # # # # # # # # # # # # # 2020-05-25 23:22:04.784622   start   UK          50
# # # # # # # # # # # # # # 2020-05-25 23:43:07.060629   end     UK          50
# # # # # # # # # # # # # # 2020-05-25 23:44:15.000566   start   US          30
# # # # # # # # # # # # # # 2020-05-25 23:48:23.416348   start   Italy       70
# # # # # # # # # # # # # # 2020-05-26 00:48:06.820164   end     US          30
# # # # # # # # # # # # # # 2020-05-26 01:33:42.454450   end     Italy       70
# # # # # # # # # # # # # # '''

# # # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # df = pd.read_clipboard()

# # # # # # # # # # # # # # df1 = df.groupby(['ID']) #, columns='Event', values='Time'

# # # # # # # # # # # # # # print(df1)

# # # # # # # # # # # # # # import os

# # # # # # # # # # # # # # sudoPass = 'Poco@123'
# # # # # # # # # # # # # # command = "launchctl list | grep -v com.apple"
# # # # # # # # # # # # # # x = os.system('echo %s|sudo -S %s' % (sudoPass, command))

# # # # # # # # # # # # # import numpy as np
# # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # # from uncertainties import unumpy as unp

# # # # # # # # # # # # # x = unp.uarray([1, 2, 3], [0.11, 0.21, 0.3])
# # # # # # # # # # # # # y = unp.uarray([5, 4, 3], [0.21, 0.08, 0.23])
# # # # # # # # # # # # # bar = np.array([7.2, 5.1, 3.7])

# # # # # # # # # # # # # df = pd.DataFrame({ 'x':x, 'y':y, 'bar':bar })
# # # # # # # # # # # # # df["z"] = df["x"]**2 + 2*df["y"]
# # # # # # # # # # # # # df["zz"] = 1/df["x"] + unp.sin(df["y"])

# # # # # # # # # # # # # print(type(df['x']))

# # # # # # # # # # # # # # print(df.nsmallest(1, "x"))
# # # # # # # # # # # # '''
# # # # # # # # # # # # time	value
# # # # # # # # # # # # 2020-03-04 22:08:00	0.023
# # # # # # # # # # # # NaN	0.039
# # # # # # # # # # # # NaN	0.104
# # # # # # # # # # # # 2020 03-04 22:11:00	0.192
# # # # # # # # # # # # '''

# # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # import numpy as np

# # # # # # # # # # # # df = pd.read_clipboard('\t')

# # # # # # # # # # # # # df['time'] = df['time'].fillna(method='ffill')
# # # # # # # # # # # # df['time'] = (pd.to_datetime(df['time'].dropna()
# # # # # # # # # # # #                                        .astype(np.int64)
# # # # # # # # # # # #                                        .reindex(df.index).interpolate()))

# # # # # # # # # # # # print(df)


# # # # # # # # # # # #binary text classification
# # # # # # # # # # # import numpy as np
# # # # # # # # # # # from keras.datasets import imdb
# # # # # # # # # # # from keras import models
# # # # # # # # # # # from keras import layers,optimizers
# # # # # # # # # # # import pandas.plotting._matplotlib as plt
# # # # # # # # # # # #loading data from the dataset
# # # # # # # # # # # (train_data,train_labels), (test_data,test_labels) = imdb.load_data(num_words = 10000)
# # # # # # # # # # # #keeping only top 10000 repeated words in th etraining data and discarding the others
# # # # # # # # # # # #creating binary matrix of the given data
# # # # # # # # # # # def vector_sequences(sequences,dimension = 1000):
# # # # # # # # # # #     results = np.zeros((len(sequences),dimension))
# # # # # # # # # # #     for i,sequence in enumerate(sequences):
# # # # # # # # # # #         results[i,sequence] = 1
# # # # # # # # # # #     return results
# # # # # # # # # # # #feeding training data in the x branch
# # # # # # # # # # # x_train = vector_sequences(train_data)
# # # # # # # # # # # x_test = vector_sequences(test_data)
# # # # # # # # # # # #vectorizing and feeding label in the y branch
# # # # # # # # # # # y_train = np.asarray(train_labels).astype('float32')
# # # # # # # # # # # y_test = np.asarray(test_labels).astype('floate32') 
# # # # # # # # # # # #Adding model layers and definition
# # # # # # # # # # # model = models.Sequential()
# # # # # # # # # # # model.add(layers.Dense(16,activation='relu',input_shape = (10000,)))
# # # # # # # # # # # model.add(layers.Dense(16,activation='relu'))
# # # # # # # # # # # model.add(layers.Dense(1,activation='sigmoid'))
# # # # # # # # # # # #making an optimizer and compiling
# # # # # # # # # # # model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])


# # # # # # # # # # '''
# # # # # # # # # # level	Parent	Child
# # # # # # # # # # 0	z	z
# # # # # # # # # # 1	z	o
# # # # # # # # # # 1	z	p
# # # # # # # # # # 2	p	t
# # # # # # # # # # 2	p	q
# # # # # # # # # # 2	o	r
# # # # # # # # # # '''

# # # # # # # # # # import pandas as pd

# # # # # # # # # # df = pd.read_clipboard(sep='\t')
# # # # # # # # # # df1=df.pivot(columns='level',values='Child')
# # # # # # # # # # df1.fillna('-',inplace=True)
# # # # # # # # # # print(df1)

# # # # # # # # # '''
# # # # # # # # # output_condition
# # # # # # # # # AND
# # # # # # # # # OR
# # # # # # # # # THEN 'Unsolicited Question From Field'
# # # # # # # # # THEN 'Unsolicited Question Direct'
# # # # # # # # # AND
# # # # # # # # # AND
# # # # # # # # # OR
# # # # # # # # # THEN 'Introduction'
# # # # # # # # # '''


# # # # # # # # # import pandas as pd

# # # # # # # # # df = pd.read_clipboard(sep="!")

# # # # # # # # # df['output_condition'].replace('AND', '', inplace=True)
# # # # # # # # # df['output_condition'].replace('OR', '', inplace=True)

# # # # # # # # # print(df)


# # # # # # # # def getCases():
# # # # # # # #     excel_file = 'path of excel'
# # # # # # # #     result = pd.read_excel(excel_file)
# # # # # # # #     count_row = result.shape[0]
# # # # # # # #     for i in range(count_row):
# # # # # # # #         r = result.iloc[i]
# # # # # # # #         return [r]

# # # # # # # # @pytest.fixture(params=PWC.getCases())
# # # # # # # # def getData(self, request):
# # # # # # # #     return request.param 


# # # # # # # Album = namedtuple('Album', 'id artist title year songs')  
# # # # # # # Song = namedtuple('Song', 'track title length play_count')  


# # # # # # # def get_song_input():
# # # # # # #     """Prompt user input."""
# # # # # # #     songtrack = input('Enter the song\'s track:\n')
# # # # # # #     songtitle = input('Enter the song\'s title:\n')
# # # # # # #     songlength = input('Enter the song\'s length:\n')
# # # # # # #     songplaycount = input('Enter the song\'s play_count:\n')
# # # # # # #     song_info = Song(songtrack, songtitle, songlength, songplaycount)
# # # # # # #     return song_info

# # # # # # # print(get_song_input)

# # # # # # lst=[15,18,20,1,19,65]

# # # # # # lst.insert(0, 'dummy')

# # # # # # print(lst[1]) # prints 15
# # # # # # print(lst[2]) # prints 18
# # # # # # print(lst[3]) # prints 20



# # # # # response = '''{
# # # # # 	"VIC": [
# # # # # 		{
# # # # # 			"type": "House",
# # # # # 			"suburb": "Carlton North",
# # # # # 			"street": "114 Garton Street",
# # # # # 			"oldRange": "$4,400,000 - $4,800,000",
# # # # # 			"newRange": "$4,100,000",
# # # # # 			"dollarDelta": "-$700,000",
# # # # # 			"percentDelta": "-14%",
# # # # # 			"daysDelta": 42
# # # # # 		},
# # # # # 		{
# # # # # 			"type": "House",
# # # # # 			"suburb": "Fitzroy North",
# # # # # 			"street": "24 Egremont Street",
# # # # # 			"oldRange": "$1,600,000 - $1,750,000",
# # # # # 			"newRange": "$1,950,000 - $2,100,000",
# # # # # 			"dollarDelta": "$350,000",
# # # # # 			"percentDelta": "20%",
# # # # # 			"daysDelta": 62
# # # # # 		},
# # # # # 		{
# # # # # 			"type": "House",
# # # # # 			"suburb": "Hamlyn Heights",
# # # # # 			"street": "6 Heritage Drive",
# # # # # 			"oldRange": "$1,180,000 - $1,280,000",
# # # # # 			"newRange": "$990,000 - $1,050,000",
# # # # # 			"dollarDelta": "-$230,000",
# # # # # 			"percentDelta": "-17%",
# # # # # 			"daysDelta": 82
# # # # # 		},
# # # # # 		{
# # # # # 			"type": "House",
# # # # # 			"suburb": "Caulfield South",
# # # # # 			"street": "24 Emma Street",
# # # # # 			"oldRange": "$1,900,000 - $2,089,999",
# # # # # 			"newRange": "$1,800,000 - $1,980,000",
# # # # # 			"dollarDelta": "-$109,999",
# # # # # 			"percentDelta": "-5%",
# # # # # 			"daysDelta": 33
# # # # # 		}
# # # # # 	]
# # # # # }'''

# # # # # import json
# # # # # from pandas.io import json as js
# # # # # import pandas as pd

# # # # # data = json.loads(response)
# # # # # df = js.json_normalize(data['VIC'])

# # # # # print(df.columns)
# # # # # print(df)


# # # # import pandas as pd
# # # # # from geopy.distance import geodesic

# # # # df1 = pd.DataFrame({'name':['a','b','c','d'], 'lat':[37.51, 41.33,37.51, 41.33], 'long':[71.81, 77.89,71.81, 77.89]})

# # # # df2 = pd.DataFrame({'id':[1,2], 'loc_a':['a','c'],'loc_z':['b','d']})

# # # # print(df1)
# # # # print(df2)

# # # # # df2['loc_a'] = [val['lat'] for val in df1 if df1['name'] == df2['loc_a']]
# # # # #df2.loc[df2['loc_a'] == df1['name']]['lat']

# # # # print(df2)

# # # import pandas as pd

# # # measures = ['BRQPP1', 'BRQPP110', 'BRQPP112', 'BRQPP236', 'BRQPP370', 'BRQPP438', 'ECQM122V7', 'ECQM124V7', 'ECQM125V7', 'ECQM128V7', 'ECQM129V8', 'ECQM131V7', 'ECQM133V7', 'ECQM134V7', 'ECQM135V7', 'ECQM142V7', 'ECQM143V7', 'ECQM144V7', 'ECQM145V7', 'ECQM146V7', 'ECQM147V8', 'ECQM149V7', 'ECQM153V7', 'ECQM154V7', 'ECQM157V7', 'ECQM161V7', 'ECQM165V7', 'ECQM177V7', 'ECQM249V1', 'ECQM347V2', 'ECQM50V7', 'ECQM56V7', 'ECQM645V2', 'ECQM66V7', 'ECQM771V1', 'ECQM90V8', 'GLQPP1', 'GLQPP110', 'GLQPP112', 'GLQPP236', 'GLQPP370', 'GLQPP438', 'LHQPP1', 'LHQPP110', 'LHQPP112', 'LHQPP236', 'LHQPP370', 'LHQPP438', 'QPP1', 'QPP102', 'QPP104', 'QPP110', 'QPP112', 'QPP116', 'QPP117', 'QPP118', 'QPP119', 'QPP12', 'QPP126', 'QPP127', 'QPP137', 'QPP138', 'QPP14', 'QPP141', 'QPP143', 'QPP144', 'QPP145', 'QPP146', 'QPP147', 'QPP154', 'QPP155', 'QPP164', 'QPP167', 'QPP168', 'QPP176', 'QPP177', 'QPP178', 'QPP180', 'QPP182', 'QPP185', 'QPP187', 'QPP19', 'QPP191', 'QPP195', 'QPP205', 'QPP21', 'QPP218', 'QPP219', 'QPP222', 'QPP225', 'QPP23', 'QPP236', 'QPP24', 'QPP243', 'QPP249', 'QPP250', 'QPP254', 'QPP258', 'QPP259', 'QPP260', 'QPP261', 'QPP264', 'QPP265', 'QPP268', 'QPP275', 'QPP277', 'QPP279', 'QPP282', 'QPP283', 'QPP286', 'QPP288', 'QPP290', 'QPP291', 'QPP293', 'QPP303', 'QPP304', 'QPP320', 'QPP322', 'QPP323', 'QPP324', 'QPP326', 'QPP331', 'QPP332', 'QPP333', 'QPP335', 'QPP336', 'QPP337', 'QPP338', 'QPP340', 'QPP342', 'QPP348', 'QPP350', 'QPP351', 'QPP354', 'QPP355', 'QPP356', 'QPP357', 'QPP358', 'QPP360', 'QPP364', 'QPP370', 'QPP374', 'QPP383', 'QPP384', 'QPP385', 'QPP386', 'QPP387', 'QPP389', 'QPP39', 'QPP390', 'QPP391', 'QPP392', 'QPP393', 'QPP395', 'QPP396', 'QPP397', 'QPP398', 'QPP400', 'QPP401', 'QPP404', 'QPP405', 'QPP406', 'QPP408', 'QPP409', 'QPP410', 'QPP412', 'QPP413', 'QPP414', 'QPP415', 'QPP416', 'QPP418', 'QPP419', 'QPP420', 'QPP421', 'QPP422', 'QPP424', 'QPP429', 'QPP430', 'QPP432', 'QPP433', 'QPP434', 'QPP435', 'QPP436', 'QPP437', 'QPP438', 'QPP439', 'QPP440', 'QPP441', 'QPP443', 'QPP444', 'QPP445', 'QPP448', 'QPP450', 'QPP451', 'QPP452', 'QPP453', 'QPP455', 'QPP457', 'QPP459', 'QPP463', 'QPP464', 'QPP465', 'QPP468', 'QPP469', 'QPP470', 'QPP471', 'QPP478', 'QPP48', 'QPP5', 'QPP50', 'QPP52', 'QPP6', 'QPP65', 'QPP66', 'QPP69', 'QPP7', 'QPP70', 'QPP76', 'QPP8', 'QPP91', 'QPP93']
# # # codes = ['ICD-9, ICD-10, SNOMED-CT', 'CPT-4, SNOMED-CT', 'Other', 'ICD-9, ICD-10, SNOMED-CT', 'HCPCS, LOINC, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT, HCPCS, LOINC', 'ICD-9, ICD-10, SNOMED-CT', 'Other', 'Other', 'ICD-10, SNOMED-CT', 'Other, CPT-4, ICD-9, LOINC, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, LOINC, ICD-10, SNOMED-CT', 'ICD-9, LOINC, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, LOINC, ICD-10, SNOMED-CT', 'CPT-4, ICD-9, LOINC, ICD-10, SNOMED-CT', 'ICD-10, SNOMED-CT', 'CPT-4, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'Other, LOINC, ICD-10, SNOMED-CT', 'ICD-10, SNOMED-CT', 'CPT-4, ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'Other', 'ICD-9, LOINC, ICD-10, SNOMED-CT', 'SNOMED-CT', 'CPT-4, HCPCS, SNOMED-CT', 'HCPCS, ICD-9, Other, ICD-10, RXNORM, SNOMED-CT', 'CPT-4, SNOMED-CT', 'Other', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4, SNOMED-CT', 'Other', 'ICD-9, ICD-10, SNOMED-CT', 'HCPCS, LOINC, ICD-10, SNOMED-CT', 'HCPCS, ICD-9, LOINC, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4, SNOMED-CT', 'Other', 'ICD-9, ICD-10, SNOMED-CT', 'HCPCS, LOINC, ICD-10, SNOMED-CT', 'HCPCS, ICD-9, LOINC, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'Other, CPT-4, HCPCS, ICD-9, LOINC, ICD-10, SNOMED-CT', 'Other, CPT-4, HCPCS, ICD-9, LOINC, ICD-10, SNOMED-CT', 'CPT-4, SNOMED-CT', 'Other', 'ICD-10', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4, HCPCS, LOINC, ICD-10', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4, ICD-10, SNOMED-CT', 'CPT-4, ICD-10, SNOMED-CT', 'ICD-9, ICD-10', 'CPT-4, ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10', 'CPT-4, ICD-9, ICD-10, SNOMED-CT', 'CPT-4, ICD-9, LOINC, ICD-10, SNOMED-CT', 'CPT-4, HCPCS', 'CPT-4, ICD-9, ICD-10', 'CPT-4', 'CPT-4, ICD-9, LOINC, ICD-10, SNOMED-CT', 'CPT-4, ICD-9, LOINC, ICD-10, SNOMED-CT', 'CPT-4', 'CPT-4', 'CPT-4', 'GPI, NDC, UMLS, CPT-4, HCPCS, ICD-9, ICD-10, RXNORM, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4', 'CPT-4, HCPCS, ICD-9, ICD-10', 'ICD-9, ICD-10', 'HCPCS, ICD-9, LOINC, ICD-10, SNOMED-CT', 'CPT-4, SNOMED-CT', 'CPT-4', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4', 'ICD-10', 'ICD-10', 'CPT-4, HCPCS', 'CPT-4, ICD-9, ICD-10', 'CPT-4', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4, ICD-10, SNOMED-CT', 'CPT-4, ICD-10', 'CPT-4, ICD-10', 'ICD-9, ICD-10', 'Other, ICD-10', 'CPT-4', 'CPT-4, ICD-10', 'CPT-4', 'ICD-9, ICD-10', 'Other, ICD-9, ICD-10, CPT-4, HCPCS', 'CPT-4', 'ICD-9, Other, ICD-10, SNOMED-CT', 'CPT-4, HCPCS, ICD-9, ICD-10', 'ICD-9, ICD-10', 'CPT-4, HCPCS, ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10, SNOMED-CT', 'CPT-4', 'CPT-4', 'CPT-4, HCPCS, ICD-10', 'CPT-4', 'CPT-4', 'CPT-4', 'ICD-10', 'ICD-10', 'HCPCS, ICD-10, RXNORM', 'ICD-10', 'Other, ICD-9, ICD-10, SNOMED-CT', 'CPT-4', 'HCPCS, ICD-9, ICD-10, RXNORM', 'ICD-9, ICD-10, SNOMED-CT', 'ICD-10', 'SNOMED-CT', 'CPT-4, ICD-10', 'CPT-4', 'CPT-4', 'CPT-4', 'CPT-4', 'CPT-4', 'CPT-4', 'CPT-4', 'CPT-4, HCPCS', 'CPT-4, HCPCS', 'HCPCS, LOINC, ICD-10, SNOMED-CT', 'HCPCS, SNOMED-CT', 'NDC, HCPCS, ICD-10, RXNORM', 'CPT-4', 'CPT-4', 'ICD-9, ICD-10, SNOMED-CT', 'HCPCS', 'CPT-4', 'Other, ICD-9, ICD-10', 'ICD-9, ICD-10', 'ICD-10, SNOMED-CT', 'Other, CPT-4, ICD-9, ICD-10', 'CPT-4, ICD-10', 'CPT-4, ICD-9, ICD-10', 'ICD-9, ICD-10', 'CPT-4, ICD-9, ICD-10', 'ICD-9, ICD-10', 'CPT-4, HCPCS, ICD-9, ICD-10, SNOMED-CT', 'ICD-9, ICD-10', 'CPT-4, HCPCS, SNOMED-CT', 'CPT-4, HCPCS', 'CPT-4, HCPCS', 'HCPCS, RXNORM', 'CPT-4, ICD-9, ICD-10, SNOMED-CT', 'NDC, HCPCS, ICD-9, ICD-10, RXNORM', 'HCPCS, RXNORM', 'CPT-4, ICD-10, SNOMED-CT', 'HCPCS', 'CPT-4, HCPCS, LOINC, ICD-10', 'CPT-4, HCPCS, LOINC, ICD-10', 'Other, CPT-4, ICD-10', 'HCPCS, ICD-9, ICD-10, SNOMED-CT', 'CPT-4, ICD-9, ICD-10', 'CPT-4, HCPCS', 'Other, CPT-4, ICD-10', 'CPT-4, LOINC', 'Other, CPT-4', 'Other, RXNORM, CPT-4, ICD-9, ICD-10, SNOMED-CT', 'Other, CPT-4', 'Other, CPT-4', 'Other, CPT-4', 'ICD-10, SNOMED-CT', 'CPT-4, HCPCS', 'CPT-4', 'HCPCS, ICD-9, LOINC, ICD-10, SNOMED-CT', 'CPT-4, HCPCS', 'CPT-4, ICD-9, ICD-10', 'CPT-4, HCPCS, ICD-10', 'Other', 'ICD-10, SNOMED-CT', 'CPT-4', 'Other', 'Other, HCPCS, ICD-9, ICD-10, RXNORM, SNOMED-CT', 'HCPCS, ICD-9, ICD-10, RXNORM', 'ICD-10, HCPCS, ICD-9', 'HCPCS, ICD-10', 'ICD-10, HCPCS, SNOMED-CT', 'HCPCS, ICD-10, SNOMED-CT', 'CPT-4', 'CPT-4, HCPCS, SNOMED-CT', 'ICD-9, ICD-10', 'Other, CPT-4, ICD-10', 'NDC, HCPCS, ICD-10, RXNORM', 'CPT-4', 'CPT-4', 'CPT-4', 'HCPCS, ICD-10', 'Other', 'ICD-9, LOINC, ICD-10, SNOMED-CT, CPT-4', 'Other, CPT-4, ICD-9, ICD-10, SNOMED-CT', 'HCPCS, ICD-9, ICD-10', 'ICD-10', 'ICD-10, SNOMED-CT', 'HCPCS, ICD-10, SNOMED-CT', 'ICD-9, ICD-10', 'ICD-9, ICD-10, SNOMED-CT, CPT-4, HCPCS, LOINC', 'ICD-9, ICD-10', 'CPT-4', 'ICD-9, LOINC, ICD-10, SNOMED-CT, HCPCS', 'ICD-9, ICD-10', 'ICD-10']

# # # df = pd.DataFrame(list(zip(measures, codes)), 
# # #                columns =['Measure_No', 'codesystem'])

# # # print(df)

# # # '''
# # # codesystem	category
# # # CPT-4,HCPCS	Procedure specific
# # # ICD-9,ICD-10,SNOMED-CT	Problem specific
# # # LOINC	Result specific
# # # Other,UMLS	Other
# # # RXNORM,NDC,GPI	Medications
# # # '''

# # # df1 = pd.read_clipboard()

# # # df3 = df.join(df1, on='codesystem', how='left', lsuffix='_l', rsuffix='_r')

# # # print(df3.head(10))


# # '''
# # Paris 25	Trouses	black	99
# # Paris 25	Jumper	Blue	48
# # London 66	Trouses	black	None
# # London 66	Skirt	white	34
# # London 66	Skirt	black	34
# # Tokyo 77	Jacket	white	45
# # Tokyo 77	Jumper	red	7
# # Tokyo 77	Trouses	Blue	87
# # London 66	Skirt	green	10
# # Paris 25	Jumper	Blue	48
# # Sydney 78	Jumper	red	7
# # NaN	Jumper	white	4
# # NaN	Skirt	green	8
# # '''

# # '''
# # Mall_1 (25 Ps)	Trouses	black	99
# # Mall_1 (25 Ps)	Jumper	Blue	48
# # Mall_2 (66 Ld)	Trouses	black	None
# # Mall_2 (66 Ld)	Skirt	white	34
# # Mall_2 66 Ld	Skirt	black	34
# # Tokyo 77	Jacket	white	45
# # Mall_3 (77 Tk)	Jumper	red	7
# # Mall_3 (77 Tk)	Trouses	Blue	87
# # London 66	Skirt	green	10
# # Mall_1 25 Ps	Jumper	Blue	48
# # Sydney 78	Jumper	red	7
# # Mall_4 59 Mn	Jumper	white	4
# # Milan 59	Skirt	green	8
# # '''

# # import pandas as pd

# # df1 = pd.read_clipboard('\t')

# # print(df1)

# # dct = {
# # "Code": ["25 Ps","66 Ld","77 Tk","78 Sn","23 NY"], "Value": ["Paris 25","London 66","Tokyo 77","Sydney 78","New York 23"]
# # }


# # df2 = pd.DataFrame(dct)

# # print(df2)

# # df2

# import pandas as pd
# from functools import reduce

# data1 = {
# "Id": [1,2,3,4,5], 
# "Data": ['a', 'b', 'c', 'd', 'e']
# }

# data2 = {
# "Id": [2,3,4,5,6], 
# "Data": ['b', 'c', 'd', 'e', 'f']
# }

# data3 = {
# "Id": [3,4,5,6,7], 
# "Data": ['c', 'd', 'e', 'f', 'g']
# }

# data4 = {
# "Id": [4,5,6,7,8], 
# "Data": ['d', 'e', 'f', 'g', 'h']
# }

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# df3 = pd.DataFrame(data3)
# df4 = pd.DataFrame(data4)

# # define a counter variable to be used as a global
# merged_count = 0

# # define the function to be called via reduce
# def merge_dfs(df_a, df_b):
#     df = df_a.merge(df_b, on=['Id', 'Data'], how='outer')
    
#     global merged_count
#     merged_count += df_a.shape[0] + df_b.shape[0] - df.shape[0]
#     return df

# # use reduce function to get the final merged dataframe
# df_final = reduce(merge_dfs, [df1, df2, df3, df4])

# print(df_final)
# print(merged_count)

# # merged_rows = len(df1) + len(df2) + len(df3) + len(df4) - len(df_final)
# # merged_rows = df1.shape[0]+df2.shape[0]+df3.shape[0]+df4.shape[0]



#     # df = pd.concat([df_a, df_b], join='inner', keys=['Id'], axis=0).reset_index(drop=True)
#     # df = df_a.join(df_b, on = ['Id'], how='left', lsuffix='_l', rsuffix='_r')
#     # df.drop(columns=['Data_r', 'Id_r'], inplace=True)
#     # df.rename(columns={"Data_l": "Data", "Id_l": "Id"}, inplace=True)