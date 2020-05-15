'''
Q	GDP
2008q3	14891.6 
2008q4	14577.0 
2009q1	14375.0 
2009q2	14355.6
'''

# import pandas as pd

# df = pd.read_clipboard(sep='\s\s+')

# # print(df.reset_index(inplace=True))
# # print(df['GDP'].min())
# # print(df.loc[df['GDP'].idxmin()]['Q'])
# print(df)
# # print(type(df.loc[df['GDP'] == df['GDP'].min()]['Q']))
# print(type(df.loc[df['GDP'].idxmin()]['Q']))

# # df2 = df.groupby(['a']) #.sort_values(['c'])
# # print(df2)

# # df.drop(labels=0, axis=1, inplace=True)

# # print(df)

# from collections import defaultdict

# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}

# print(type(ContinentDict))

# dictionary = defaultdict(list)
# for key, value in ContinentDict.items():
#     dictionary[value].append(key)

# print(dictionary)

# '''
#    ENG  KIS BIO PHY HIS GEO CRE  POINTS
#    10    9   7   9           8     36
#     3    5       5       7   3     20
#     5    7   4       9       6     27
#     6    9      10   7  11         36
#     3   10   4  12   8             25

# '''

# import pandas as pd

# df = pd.DataFrame({'ENG':[10,3,5,6,3],'KIS':[9,5,7,9,10],'BIO':[10,0,4,0,4],'PHY':[9,5,0,10,12],'HIS':[0,0,9,7,8],'GEO':[0,7,0,11,0],'CRE':[8,3,6,0,0]})

# # a transposed DF of optional subjects
# df_opt = df.T[2:]

# collect sum of top two scores in the transposed columns
# score = []

# for col in df_opt.columns:
#     score.append(df_opt.nlargest(2, [col])[col].sum())

# print(score)

# df['Points'] = df['ENG'] + df['KIS'] + score

# print(df)


# import pandas as pd

# series = [('Stranger Things', 3, 'Millie'),
#           ('Game of Thrones', 8, 'Emilia'), ('La Casa De Papel', 4, 'Sergio'),
#           ('Westworld', 3, 'Evan Rachel'), ('Stranger Things', 3, 'Millie'),
#          ('La Casa De Papel', 4, 'Sergio')]

# # Create a DataFrame object
# dfObj = pd.DataFrame(series, columns=['Name', 'Seasons', 'Actor'])

# # Find a duplicate rows
# duplicateDFRow = dfObj[dfObj.duplicated(['Name', 'Seasons'])]

# dfRes = dfObj.subtract(duplicateDFRow, fill_value=0)
# #pd.merge(dfObj, duplicateDFRow, how='inner')

# # for row in dfObj:
# #     if row not in duplicateDFRow:
# #         dfObj['dup'] = 1
# #     else:
# #         dfObj['dup'] = 2

# print(dfObj)

# print(duplicateDFRow)

# print(dfRes)

# '''
# Name        Team        Games
# Trevor      SAC         32
# Trevor      TOT         50
# Trevor      POR         18
# Kyle        MEM         59
# LeMarcus    SAS         43
# Jordan      TOT         50
# Jordan      MIN         35
# Jordan      ATL         15
# Will        DEN         53
# '''

# import pandas as pd

# df = pd.read_clipboard(sep='\s\s+')

# # print(df)
# # print(df.columns)

# df_tot = df.loc[df['Team']=='TOT']
# df_dup = df.drop_duplicates(subset=['Name'], keep=False)
# df_merged = pd.concat([df_tot, df_dup]).reset_index()


# import pandas as pd

# '''
# FIRST	SECOND	COUNT
# 1	['A','B']	['2','1']
# 2	['C','D']	['1','1']
# 1	['A','E']	['1','1']
# 2	['C','F']	['2','1']
# '''

# df = pd.read_clipboard(sep='\s\s+')

# print(df)

import pandas as pd


def get_word_count(text,df):
    #text is a lowercase list of words
    #df is a dataframe with 2 columns: word and count
    #this function updates the word  counts


    #f=open('stopwords.txt','r')
    #stopwords=f.read()
    stopwords='in the and an - '

    for word in text:
        if word not in stopwords:

            if word in df['word'].tolist():
                df.loc[df['word']==word, 'count']=df['count']+1
            else:
                df.loc[0]=[word,1]
                df.index=df.index+1

    return df


if __name__ == '__main__':
    word_df=pd.DataFrame(columns=['word','count'])
    sentence1='[first] - missing "" in the text [first] word'.split()
    print(sentence1)
    y=get_word_count(sentence1, word_df)
    sentence2="error: wrong word in the [second] text".split()
    print(sentence2)
    y=get_word_count(sentence2, word_df)

    print(y)