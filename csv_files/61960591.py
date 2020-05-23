# # # # # '''
# # # # #         Data_Value
# # # # # Month_Day   
# # # # # 01-01     1.1
# # # # # 01-02     3.9
# # # # # 01-03     3.9
# # # # # 01-04     4.4
# # # # # '''

# # # # # import pandas as pd

# # # # # df = pd.read_clipboard()

# # # # # df.reset_index(inplace=True)

# # # # # df['Month_Day'] = pd.to_datetime(df['Month_Day'], format='%m-%d')

# # # # # # you can replace the year with any value, using 2020 as an example
# # # # # df['Month_Day'] = [val.replace(year=2020) for val in df['Month_Day']]

# # # # # print(df)

# # # # # import matplotlib.pyplot as plt

# # # # # # generate the plot
# # # # # plt.scatter(df['Month_Day'], df['Data_Value'])
# # # # # plt.show()

# # # # '''
# # # #     col1    col2    col3    col4    col5
# # # # 0   False   False   True    True    False
# # # # 1   False   True    True    False   False
# # # # '''

# # # # import pandas as pd

# # # # df = pd.read_clipboard()

# # # # print(df)
# # # # df1 = df.loc[:,df.any()] 
# # # # print(df1)

# # # import pandas as pd
# # # print(pd.__version__)

# # import os
# # import glob
# # import pandas as pd

# # # replace "/dir" with the location that contains the files
# # os.chdir("/home/anshul/youtube/stackoverflow/csv_files/")

# # extn = 'csv'
# # filenames = [i for i in glob.glob('*.{}'.format(extn))]

# # combined_csv = pd.concat([pd.read_csv(f) for f in filenames ])
# # combined_csv.to_csv( "/home/anshul/youtube/stackoverflow/csv_files/combined_csv.csv", index=False)


# a = [(0, 0.6249995), (1, 0.12500015), (2, 0.12500016), (3, 0.12500015)]

# # import pandas as pd

# # df = pd.DataFrame(a)
# # df.columns = ['topics', 'probabilities']

# # print(df)

# # print(df.loc[df['probabilities'].max()])

# print(max(a, key=lambda x: x[1]))


import pandas as pd

df = pd.DataFrame({'a':[0,1,2], 'text':["I love a dog", "He is smart", "I hate this"]})

def edit(input_text):
    output = input_text[:4]
    return output


df['text'] = df['text'].apply(lambda x: edit(x))

print(df)