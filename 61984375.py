# # # # # # # import pandas as pd

# # # # # # # df = pd.read_csv("/home/anshul/youtube/stackoverflow/61984375.csv", header=None, sep='", "')

# # # # # # # # df[0] = df[0].str.replace('"', '')
# # # # # # # # df.iloc[:,-1] = df.iloc[:,-1].str.replace('"', '')

# # # # # # # df.iloc[:, 0] = df.iloc[:, 0].str.replace('"', '')
# # # # # # # df.iloc[:,-1] = df.iloc[:,-1].str.replace('"', '')

# # # # # # # # df = df.astype(str).replace('"', '')

# # # # # # # print(df.reset_index(drop=True))


# # # # # # # # df = pd.read_csv("/home/anshul/youtube/stackoverflow/61984375.csv", sep = ",", 
# # # # # # # # encoding = "ISO-8859-1", quotechar = '"', header=None)


# # # # # # '''
# # # # # #     A   B   C  
# # # # # # A   1   3   0    
# # # # # # B   3   2   5     
# # # # # # C   0   5   4  
# # # # # # '''

# # # # # # import pandas as pd

# # # # # # df = pd.read_clipboard()

# # # # # # # df1 = df.stack().reset_index().agg(tuple, 1).tolist()

# # # # # # df1 = [*df.stack().iteritems()]

# # # # # # print(df1)

# # # # # num = -123456

# # # # # # def get_sum(num):
# # # # # #     sum = 0
# # # # # #     while num != 0:
# # # # # #         sum += num%10
# # # # # #         num = num//10
# # # # # #         # print(num, sum)
# # # # # #     return sum

# # # # # # final_sum = get_sum(num)
# # # # # # if final_sum%10 != 0:
# # # # # #     final_sum = get_sum(final_sum)

# # # # # # print(final_sum)

# # # # # print((num-1)%9 + 1)

    

# # # # from urllib.request import urlopen
# # # # import time
# # # # from bs4 import BeautifulSoup as bs


# # # # html = urlopen("https://www.familysearch.org/search/record/results?q.birthLikePlace=italy&f.collectionId=1410078&m.defaultFacets=on&m.queryRequireDefault=on&m.facetNestCollectionInCategory=on&count=20&offset=0")
# # # # # time.sleep(5)
# # # # bsObj = bs(html, features="html.parser")
# # # # result = bsObj.find("div", {"class":"table table-element-table"})
# # # # print(bsObj)
# # # # print(result)

# # # '''
# # # 74° 18' 01.8963" E 32° 56' 40.2788" N
# # # 76° 05' 57.9815" E 31° 24' 25.0336" N
# # # 75° 02' 45.5176" E 30° 25' 19.6260" N
# # # 73° 23' 12.3829" E 31° 47' 47.4578" N
# # # 74° 18' 01.8963" E 32° 56' 40.2788" N
# # # '''

# # # import pandas as pd

# # # # df = pd.read_clipboard(header=None)

# # # # using some random seperator to get the entire row as one column
# # # df = pd.read_csv("coordinates.csv", sep="!", header=None)
# # # df.columns = ['coord']

# # # # added separate columns will blanks for lat and lon (I assumed them to be)
# # # df['lat'] = ''*len(df['coord'])
# # # df['lon'] = ''*len(df['coord'])

# # # print(df)

# # # import re

# # # # assuming each coordinate will end with either of one directional indicators - E, W, N or S
# # # pattern = '[EWNS]'

# # # for i, val in enumerate(list(df['coord'])):
# # #     idx = re.search(pattern, val).start()
# # #     df['lat'][i] = df['coord'][i][:idx+1]
# # #     df['lon'][i] = df['coord'][i][idx+1:]
    
# # # print(df)
# # # # df['lat'] = df[0]+df[1]+df[2]+df[3]
# # # # df['lon'] = df[4]+df[5]+df[6]+df[7]
# # # # print(indexes)
# # # # print(df)

# # # # for idx in indexes:
# # # #     df['lat'] = df.iloc[:17, 'coord']
# # import pandas as pd

# # df = pd.read_csv("coordinates2.csv", sep="'''", header=None)
# # # df.columns = ['coord']

# # # # added separate columns will blanks for lat and lon (I assumed them to be)
# # # df['lat'] = ''*len(df['coord'])
# # # df['lon'] = ''*len(df['coord'])

# # print(df)



# from bs4 import BeautifulSoup
# import pandas as pd
# from selenium import webdriver
# import pandas as pd

# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# fretes=[] #List to store rating of the product
# driver = webdriver.Firefox()
# # driver.implicitly_wait(30)
# driver.get("https://lista.mercadolivre.com.br/macbook")
# content = driver.page_source
# # print(content)
# soup = BeautifulSoup(content, 'html.parser')
# print(soup)
# # for a in soup.findAll('li',href=True, attrs={'class':'results-item'}):
# #     name=a.find('span', attrs={'class':'main-title'})
# #     price=a.find('span', attrs={'class':'price__fraction'})
# #     frete=a.find('span', attrs={'class':'text-shipping'})
# #     products.append(name.text)
# #     prices.append(price.text)
# #     fretes.append(frete.text)
# #     data = dict({'Product Name': products,
# #                  'Price': prices,
# #                  'Frete': fretes
# #                  })
# #     # create dataframe
# #     products_df = pd.DataFrame(
# #         dict([(k, pd.Series(v)) for k, v in data.items()])
# #         )    
# #     products_df.to_csv(r"/home/anshul/youtube/stackoverflow/mac.csv")

# # print(products_df)