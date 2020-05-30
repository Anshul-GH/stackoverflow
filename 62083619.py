# # # import xmltodict
# # # import pandas as pd
# # # from lxml import objectify
# # # import pandas as pd

# # # with open('62083619.xml', 'r') as f:
# # #     data = xmltodict.parse(f.read())['tv']

# # # print(data)

# # # data_pd = {'programme': [data['programme']],
# # #            'title': [data['title']],
# # #            'category': [data['category']]}

# # # df = pd.DataFrame(data_pd)
# # # print(df)

# # from lxml import objectify
# # import pandas as pd

# # xml = objectify.parse(open(r"C:\BAU\Code\03_Personal\stackoverflow\62083619.xml"))

# # root = xml.getroot()
# # print(root.getchildren()[0].getchildren())

# # # df = pd.DataFrame()




# import pandas as pd 
# import requests 
# from bs4 import BeautifulSoup

# url = 'https://www.worldometers.info/coronavirus/'

# req = requests.get(url)

# page = BeautifulSoup(req.content, 'html.parser')

# table = page.find_all('table',id="main_table_countries_today")[0]

# # with open("62083619.txt", 'w+') as f:
# #     print(table, file=f)

# # print(table)

# df = pd.read_html(str(table))[0]

# # print(type(df))

# print(df)

# import numpy as np

# arr = np.array([[0.04079875],
#        [0.03456873],
#        [0.05971941],
#        [0.20677155],
#        [0.24261144],
#        [0.08530033],
#        [0.01146799],
#        [0.09208623],
#        [0.10507914],
#        [0.25772226]])


# import pandas as pd

# df = pd.DataFrame(list(arr), columns=['values'])

# print(df)

import pandas as pd
import numpy as np

# source data for the dataframe
data = {
"ID":["x","y","z","x","y","z","x","y","a","b","x"],
"Date":["May 01","May 02","May 04","May 01","May 01","May 02","May 01","May 05","May 06","May 08","May 10"],
"Amount":[10,20,30,40,50,60,70,80,90,100,110]
}

df = pd.DataFrame(data)

# convert the Date column to datetime and still maintain the format like "May 01"
df['Date'] = pd.to_datetime(df['Date'], format='%b %d').dt.strftime('%b %d')

# sort the values on ID and Date
df.sort_values(by=['ID', 'Date'], inplace=True) #axis=1, 
df.reset_index(inplace=True, drop=True)

print(df)

# create a list of unique ids
list_id = sorted(list(set(df['ID'])))

# create an empty list that would contain dataframes
df_list = []

# count of iterations that must be seperated out
# for example if we want to record 3 entries for 
# each id, the iter would be 3. This will create
# three new dataframes that will hold transactions
# respectively. 
iter = 4
for i in range(iter):
    df_list.append(pd.DataFrame())


for val in list_id:
    tmp_df = df.loc[df['ID'] == val].reset_index(drop=True)

    # consider only the top iter(=3) values to be distributed
    counter = np.minimum(tmp_df.shape[0], iter)
    for idx in range(counter):
        df_list[idx] = df_list[idx].append(tmp_df.loc[tmp_df.index == idx])

for df in df_list:
    df.reset_index(drop=True, inplace=True)
    print(df)