# # # # '''
# # # # hops.name	hops.add	hops.attribute	hops.amount.value	hops.amount.unit	id	name                
# # # # Fuggles       	start   	bitter        	            25.00	grams           	 1	Buzz                               
# # # # First Gold    	start   	bitter        	            25.00	grams           	 1	Buzz                               
# # # # Fuggles       	middle  	flavour       	            37.50	grams           	 1	Buzz                               
# # # # First Gold    	middle  	flavour       	            37.50	grams           	 1	Buzz                               
# # # # Cascade       	end     	flavour       	            37.50	grams           	 1	Buzz                               
# # # # Amarillo      	start   	bitter        	            13.80	grams           	 2	Trashy Blonde                      
# # # # Simcoe        	start   	bitter        	            13.80	grams           	 2	Trashy Blonde                      
# # # # Amarillo      	end     	flavour       	            26.30	grams           	 2	Trashy Blonde                      
# # # # Motueka       	end     	flavour       	            18.80	grams           	 2	Trashy Blonde                      
# # # # Bramling Cross	middle  	bitter        	            10.00	grams           	 3	Berliner Weisse With Yuzu  BSides
# # # # '''

# # # # # import pandas as pd

# # # # # df = pd.read_clipboard()

# # # # # print(df)

# # # # data1 = {
# # # # "hops.name":["Fuggles","FirstGold","Fuggles","FirstGold","Cascade","Amarillo","Simcoe","Amarillo","Motueka","BramlingCross"],
# # # # "hops.add":["start","start","middle","middle","end","start","start","end","end","middle"],
# # # # "hops.attribute": ["bitter","bitter","flavour","flavour","flavour","bitter","bitter","flavour","flavour","bitter"],
# # # # "id": [1,1,1,1,1,2,2,2,2,3],
# # # # "name":["Buzz","Buzz","Buzz","Buzz","Buzz","Trashy Blonde","Trashy Blonde","Trashy Blonde","Trashy Blonde","Berliner Weisse With Yuzu - B-Sides"]
# # # # }

# # # # data2 = {
# # # #     "method.mash_temp.duration": [75.0,10.0,30.0], 
# # # #     "id": [1,2,3],
# # # #     "name":["Buzz","Trashy Blonde","Berliner Weisse With Yuzu - B-Sides"]

# # # # }

# # # # import pandas as pd
# # # # from functools import reduce

# # # # merged_count = 0

# # # # df1 = pd.DataFrame(data1)
# # # # df2 = pd.DataFrame(data2)

# # # # list_of_df = [df2, df2, df2, df2]

# # # # def merge_dfs(df_a, df_b):
# # # #     # df = df_a.merge(df_b, on=['id', 'name'], how='inner')
# # # #     df = pd.merge(df_a, df_b, on=['id', 'name'], how='inner')

# # # #     print(df)

# # # #     print(df_a.shape[0])
# # # #     print(df_b.shape[0])
# # # #     print(df.shape[0])

# # # #     global merged_count
# # # #     merged_count += df_a.shape[0] + df_b.shape[0] - df.shape[0]
# # # #     print(merged_count)
# # # #     print("-----------------")
# # # #     return df

# # # # # use reduce function to get the final merged dataframe
# # # # df_final = reduce(merge_dfs, list_of_df)

# # # # print(merged_count)

# # # # # df3 = df = df1.merge(df2, on=['id', 'name'], how='outer')

# # # # # merged_count = df1.shape[0] + df2.shape[0] - df3.shape[0]

# # # # # # print(df1)
# # # # # # print(df2)

# # # # # print(df3)
# # # # # print(merged_count)


# # # import pandas as pd
# # # import numpy as np

# # # arr = np.ones((4,3))

# # # data = {"lists": list(arr)}

# # # df = pd.DataFrame(data, columns=['lists'])

# # # print(df)

# # '''
# # Animal
# # 22 dogs
# # 1 dog
# # 1 cat
# # 3 dogs
# # 32 chats
# # '''

# # import pandas as pd
# # import re

# # df = pd.read_clipboard("!")

# # # print(df)

# # import re

# # list1 = ['dogs', 'dog', 'chien', 'chiens']
# # list2 = ['cats', 'cat', 'chat', 'chats']

# # df['New_col'] = [(re.search(r'(\w+)', val).group(1).strip()+"-00") if re.search(r'([a-zA-Z]+)', val).group(1).strip() in list1 else ("00-" + re.search(r'(\w+)', val).group(1).strip()) if re.search(r'([a-zA-Z]+)', val).group(1).strip() in list2 else val for val in list(df['Animal'])]

# # print(df)

# import pandas as pd

# example = pd.DataFrame({
#             'name': ['alice','bob','charlie'],
#             'age': [25,26,27],
#             'job': ['manager','clerk','policeman'],
#             'gender': ['female','male','male'],
#             'nationality': ['french','german','american']
#         })

# example['age_times_two']= example['age'] *2

# cols = example.columns.tolist()

# cols = cols[:2]+cols[-1:]+cols[2:-1]

# example = example[cols]

# print(example)

