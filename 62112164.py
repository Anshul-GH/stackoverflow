# # # # with open('62112164.txt') as f:
# # # #     for val in f:
# # # #         # print(val)
# # # #         val = val.split().strip('$')
# # # #         print(val)

# # # # # data = f.readlines()
# # # # # print(data)


# # data = """
# # <magento_api>
# # <data_item>
# # <code>400</code>
# # <message>Attribute weight is not applicable for product type Configurable Product</message>
# # </data_item>
# # <data_item>
# # <code>400</code>
# # <message></message>
# # </data_item>
# # <data_item>
# # <code></code>
# # <message>abc</message>
# # </data_item>
# # <data_item>
# # <code></code>
# # <message></message>
# # </data_item>
# # </magento_api>
# # """
# # import re

# # def drop_empty_tags(lst):
# #     lst_tmp = []
# #     recur = False
# #     for val in lst:
# #         if re.match(r'\<\w+\>\n?\<\/\w+\>', val.strip()) is None:
# #             lst_tmp.append(val)
# #             recur=False
# #         else:
# #             recur=True
# #     if recur:
# #         lst_tmp = drop_empty_tags(lst_tmp)
# #     else:
# #         return lst_tmp

# #     # # drop values that just have closing and opening tags
# #     # df1 = [val for val in df if re.match(r'\<\w+\>\n?\<\/\w+\>', val.strip()) is None]
# #     # return df1

# # # strip leading and trailing \n and then split the remaining values on \n
# # data = data.strip("\n").split('\n')

# # # join back to get the trimmed string as needed
# # data1 = drop_empty_tags(data)

# # data1 = '\n'.join(data1)

# # print(data1)



# data = """
# <magento_api>
# <data_item>
# <code>400</code>
# <message>Attribute weight is not applicable for product type Configurable Product</message>
# </data_item>
# <data_item>
# <code>400</code>
# <message></message>
# </data_item>
# <data_item>
# <code></code>
# <message>abc</message>
# </data_item>
# <data_item>
# <code></code>
# <message></message>
# </data_item>
# </magento_api>
# """
# data = data.strip()
# data = data.replace("</","")
# data = data.replace("<","|")
# data = data.replace(">","+")
# data = data.replace("/","+")
# data = data.replace("\n","")

# print(data)

from lxml import etree

tree = etree.parse(r"/home/anshul/youtube/stackoverflow/62112278.xml")
notags = etree.tostring(tree, encoding='utf8', method='text')
print(notags)