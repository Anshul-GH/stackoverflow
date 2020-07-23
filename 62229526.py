# # # '''
# # # Location	Month	Date	Ratio
# # # A	June	Jun 1	0.2
# # # A	June	Jun 2	0.3
# # # A	June	Jun 3	0.4
# # # B	June	Jun 1	0.6
# # # B	June	Jun 2	0.7
# # # B	June	Jun 3	0.8
# # # '''

# # # import pandas as pd

# # # df1 = pd.read_clipboard("\t")

# # # print(df1)


# # # data = {
# # # 'Location': ['A','B'],
# # # 'Month': ['June','June'],
# # # 'Value': [1000,2000]
# # # }

# # # df2 = pd.DataFrame(data)

# # # print(df2)

# # # df3 = df1.join(df2, on=['location', 'Month'], how='left')

# # # print(df3)

# # # # mask = df1['Month'] == df2['Month']

# # # # df1['Value'] = df1.loc[mask]['Ratio'] * df2.loc[mask]['Value']

# # # # print(df1)



# # '''
# # item_id	item_name	item_desc	rating	item_type	price
# # it1	laptop		6.0	asus	50000.0
# # it1	laptop		7.0	acer	30000.0
# # it1	laptop		3.0	hp	20000.0
# # it2	smartphone		6.0	iphone	600000.0
# # it2	smartphone		5.0	samsung	750000.0
# # it1	laptop		4.0	dell	10000.0
# # it3	radio	Bestradio	8.0	tech	30000.0
# # it3	radio	Bestradio	9.0	tech	30000.0
# # '''

# # import pandas as pd

# # df = pd.read_clipboard()

# # print(df)


# # df1 = df.groupby(['item_id']).sum()

# # print(df1)

# '''
# id	col1a	col1b	col2a	col2b	col3a	col3b
# 1	11	12	NaN	NaN	NaN	NaN
# 2	NaN	NaN	21	86	NaN	NaN
# 3	22	87	NaN	NaN	NaN	NaN
# 4	NaN	NaN	NaN	NaN	545	32
# '''

# import pandas as pd

# df = pd.read_clipboard()

# print(df)



import pandas as pd
data = {'Brand':['residential','unclassified','tertiary','residential','unclassified','primary','residential'],
    'Price': [22000,25000,27000,"NA","NA",10000,"NA"]
    }

df = pd.DataFrame(data, columns = ['Brand', 'Price'])

print (df)

repl_data = {
    "residential": 1000, 
    "unclassified": 2000
}


df['Price'] = [repl_data[val] for val in df['Brand'] if df.loc[df['Brand'] == val]['Price'] is 'NA']
# [repl_data[val['Brand']] for val in df[['Brand', 'Price']]]

print(df)