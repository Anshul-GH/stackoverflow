# # # # # # # with open('62112164.txt') as f:
# # # # # # #     for val in f:
# # # # # # #         # print(val)
# # # # # # #         val = val.split().strip('$')
# # # # # # #         print(val)

# # # # # # # # data = f.readlines()
# # # # # # # # print(data)


# # # # # data = """
# # # # # <magento_api>
# # # # # <data_item>
# # # # # <code>400</code>
# # # # # <message>Attribute weight is not applicable for product type Configurable Product</message>
# # # # # </data_item>
# # # # # <data_item>
# # # # # <code>400</code>
# # # # # <message></message>
# # # # # </data_item>
# # # # # <data_item>
# # # # # <code></code>
# # # # # <message>abc</message>
# # # # # </data_item>
# # # # # <data_item>
# # # # # <code></code>
# # # # # <message></message>
# # # # # </data_item>
# # # # # </magento_api>
# # # # # """
# # # # # import re

# # # # # def drop_empty_tags(lst):
# # # # #     lst_tmp = []
# # # # #     recur = False
# # # # #     for val in lst:
# # # # #         if re.match(r'\<\w+\>\n?\<\/\w+\>', val.strip()) is None:
# # # # #             lst_tmp.append(val)
# # # # #             recur=False
# # # # #         else:
# # # # #             recur=True
# # # # #     if recur:
# # # # #         lst_tmp = drop_empty_tags(lst_tmp)
# # # # #     else:
# # # # #         return lst_tmp

# # # # #     # # drop values that just have closing and opening tags
# # # # #     # df1 = [val for val in df if re.match(r'\<\w+\>\n?\<\/\w+\>', val.strip()) is None]
# # # # #     # return df1

# # # # # # strip leading and trailing \n and then split the remaining values on \n
# # # # # data = data.strip("\n").split('\n')

# # # # # # join back to get the trimmed string as needed
# # # # # data1 = drop_empty_tags(data)

# # # # # data1 = '\n'.join(data1)

# # # # # print(data1)



# # # # data = """
# # # # <magento_api>
# # # # <data_item>
# # # # <code>400</code>
# # # # <message>Attribute weight is not applicable for product type Configurable Product</message>
# # # # </data_item>
# # # # <data_item>
# # # # <code>400</code>
# # # # <message></message>
# # # # </data_item>
# # # # <data_item>
# # # # <code></code>
# # # # <message>abc</message>
# # # # </data_item>
# # # # <data_item>
# # # # <code></code>
# # # # <message></message>
# # # # </data_item>
# # # # </magento_api>
# # # # """
# # # # data = data.strip()
# # # # data = data.replace("</","")
# # # # data = data.replace("<","|")
# # # # data = data.replace(">","+")
# # # # data = data.replace("/","+")
# # # # data = data.replace("\n","")

# # # # print(data)

# # # from lxml import etree

# # # tree = etree.parse(r"/home/anshul/youtube/stackoverflow/62112278.xml")
# # # notags = etree.tostring(tree, encoding='utf8', method='text')
# # # print(notags)

# # '''
# # Person	Activity	Duration
# # 1	A	1 00:00
# # 2	A	1 00:00
# # 3	B	0 21:17
# # 4	C	0 17:11
# # '''

# # import pandas as pd

# # df = pd.read_clipboard("\t")

# # df['Duration'] = df['Duration'].str.split(' ')

# # df['Duration'] = ['24:00' if int(val[0]) == 1 else val[1] for val in df['Duration']]

# # print(df)
# '''
# Name:	Tags:
# 'One'	['tag1','tag3']
# 'Two'	[]
# 'Three'	['tag1']
# '''

# import pandas as pd
# df = pd.read_clipboard('\t')

# df['Tags:'] = df['Tags:'].astype(list) # [val. for val in ]

# # df['Tags:'] = [val.append('tag2') for list(val) in df['Tags:']]

# print(df)


'''
ColumnA
"ABC X1"
"BCS X2"
"CCC X3"
'''

import pandas as pd
import re

df = pd.read_clipboard("!")

print(df)

check_list = ["X1", "X3"]

# df['ColumnB'] = [val.find(r'X[13]') for val in df['ColumnA']]
#[val.split(' ')[1] if val.find(r'X[13]') != -1 else val for val in df['ColumnA']]
df['ColumnB'] =  [re.findall(r'X[13]', str(val)) for val in df['ColumnA']]


print(df)