# # '''
# # brand        model      year       engine    transmission   suspension   brakes   Overall_Score
# # Acura        CL         1999          3           2           1           3          1
# # Acura        CL         2000          5           3           7           2          3
# # BMW          520        2015          22          4           10          11         2
# # BMW          520        2008          1           6           3           6          4
# # Chevrolet    Impala     1997          0           2           2           5          1
# # Chevrolet    Impala     2002          9           3           8           4          1
# # '''

# # import pandas as pd

# # # df = pd.read_clipboard()

# # # df.set_index('brand', inplace=True)

# # # df.to_json('62050988.json', orient='index')

# # # print(df)

# # from pandas.io.json import json_normalize
# # import json

# # import pandas as pd

# # with open('output.json') as jsonfile:
# #     data = json.load(jsonfile)
# # # data = json.load('output.json')

# # # data = pd.read_json('output.json')

# # print(data)

# # nz_data = json_normalize(data)

# # print(nz_data)


# '''
# Name	Private IP
# bastion001	10.238.2.166
# logicmonitor001	10.238.2.52
# logicmonitor002	44.21.2.13
# '''

# import pandas as pd

# df = pd.read_clipboard()

# print(list(df['Name']))

# for val in list(df['Name']):
#     print(val)


list_of_df = [df_hops,df_method_mash_temp,df_ingredients_malt,whole_table]

merged_count = 0

def merge_dfs(df_a, df_b):
    df = df_a.merge(df_b, on=['id', 'name'], how='outer')

    global merged_count
    merged_count += df_a.shape[0] + df_b.shape[0] - df.shape[0]
    return df

# use reduce function to get the final merged dataframe
df_final = reduce(merge_dfs, list_of_df)

print(merged_count)