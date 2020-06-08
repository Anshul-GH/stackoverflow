# # # # # # # # # import json
# # # # # # # # # import pandas as pd

# # # # # # # # # # data = json.load('62073763.json')

# # # # # # # # # data = pd.read_json('62073763.json')

# # # # # # # # # print(data)

# # # # # # # # '''
# # # # # # # # "cat"	"waverly way"	"foo"	10.0
# # # # # # # # "cat"	"smokey st"	"moo"	9.7
# # # # # # # # "rabbit"	"rapid ave"	"foo"	6.6
# # # # # # # # "rabbit"	"far blvd"	"too"	3.2
# # # # # # # # '''

# # # # # # # # import pandas as pd

# # # # # # # # df = pd.read_clipboard(header=None)

# # # # # # # # df.columns = ['A', 'B', 'C', 'D']

# # # # # # # # print(df)

# # # # # # # # filter = ['foo,moo']

# # # # # # # # df['C'] = df[['A', 'B', 'C', 'D']].groupby(by=['A'])['C'].transform(lambda x: ','.join(x))

# # # # # # # # df1 = df.loc[~df['C'].isin(filter)].reset_index(drop=True)

# # # # # # # # print(df1)



# # # # # # # number = int(input())
# # # # # # # collect = [] #collect number from input
# # # # # # # for i in range(number):
# # # # # # #   x = int(input())
# # # # # # #   collect.append(x)
# # # # # # # print(collect)
# # # # # # # for j in [ele for ind, ele in enumerate(collect,1) if ele not in collect[ind:]]:
# # # # # # #     count = 0
# # # # # # #     for ele in collect:
# # # # # # #         if j == el:
# # # # # # #             count += 1
# # # # # # #         else:
# # # # # # #             pass
# # # # # # #     if count != 0:
# # # # # # #         print("{} : {} Items".format(ind, count))
# # # # # # #     else:
# # # # # # #         print("{} : {} Item".format(j, count))


# # # # # # val = [{'Name': 'Total', 'Value': 50, 'Unit': 'Units'}]

# # # # # # dct = dict(val[0])

# # # # # # print(dct)
# # # # # # print(type(dct))


# # # # # import requests
# # # # # import time
# # # # # from bs4 import BeautifulSoup


# # # # # # driver = webdriver.Firefox()
# # # # # url= "https://www.adb.org/projects/tenders/sector/information-and-communication-technology-1066"
# # # # # content = requests.get(url)

# # # # # soup = BeautifulSoup(content.text,"html.parser")
# # # # # print(soup)
# # # # # div_tags = []
# # # # # for tags in soup.findAll("div", class_="item-title"):
# # # # #     div_tags.append(tags)
# # # # # print(div_tags)
# # # # # for tags in div_tags:
# # # # #     a_tag=tags.find('a')
# # # # #     link=a_tag.get('href')
# # # # #     print(link)

# # # # '''
# # # # brand        model      year       engine    transmission   suspension   brakes   Overall_Score
# # # # Acura        CL         1999          3           2           1           3          1
# # # # Acura        CL         2000          5           3           7           2          3
# # # # BMW          520        2015          22          4           10          11         2
# # # # BMW          520        2008          1           6           3           6          4
# # # # Chevrolet    Impala     1997          0           2           2           5          1
# # # # Chevrolet    Impala     2002          9           3           8           4          1
# # # # '''

# # # # import pandas as pd

# # # # df = pd.read_clipboard()

# # # # columns = df.select_dtypes(include='int').columns

# # # # df[columns] = df[columns].astype(float)

# # # # print(df)

# # # '''
# # # year	key	val
# # # 2019	a  	3
# # # 2019	a  	4
# # # 2019	b  	3
# # # 2019	c  	5
# # # 2020	d  	6
# # # 2020	e  	1
# # # 2020	f  	2
# # # '''

# # # import pandas as pd

# # # df = pd.read_clipboard()
# # # df.set_index(['year'], inplace=True)



# # # # print(df)

# # # mask = list(df.reset_index()['year'])[-1]

# # # # # data['year'][-1]

# # # print(mask)

# # # # mask = df.groupby(['year', 'key']).sum()

# # # # print(df[mask])


# # data = {'data': 'key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47, 
# #  key=0Sr4C, age=68, key=CGEqo, age=76, key=IxKVQ, age=79, key=eD221, age=29,
# #  key=XZbHV, age=32, key=k1SN5, age=88, key=4SCsU, age=65, key=q3kG6, age=33,
# #  key=MGQpf, age=13, key=Kj6xW, age=14, key=tg2VM, age=30, key=WSnCU, age=24,
# #  key=f1Vvz, age=46, key=dOS7A, age=72, key=tDojg, age=82, key=nZyJA, age=48,
# #  key=R8JTk, age=29, key=005Ot, age=66, key=HHROm, age=12, key=5yzG8, age=51,
# #  key=xMJ5D, age=38, key=TXtVu, age=82, key=Hz38B, age=84}

# '''
# 544299
# {'kWh': '-107.368'}
# {'kWh': '-143.982'}
# '''

# import pandas as pd

# df = pd.read_clipboard("!")

# print(df)

# df['544299'] = df['544299'].str.extract(r'(-?\d+\.\d+)').astype(float)

# print(df)