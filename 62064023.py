# # # import pandas as pd
# # # import calendar

# # # d=dict(enumerate(calendar.day_name))
# # # c = calendar.Calendar(firstweekday=calendar.SUNDAY)
# # # year = 2020; month = 6

# # # data = {
# # #     'salary_day': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# # # }

# # # df = pd.DataFrame(data)
# # # df['req_dates'] = ''
# # # # print(df)


# # # monthcal = c.monthdatescalendar(year,month)
# # # day_counter = 0
# # # for week in monthcal:
# # #     for day in week:
# # #         day_counter += 1
# # #         if day.month == month:
# # #             if day_counter % 7 != 0:
# # #                 df.loc[df['salary_day'] == d[day.weekday()], 'req_dates'] += str(day)[-2:] + ','
# # #             else:



# # # print(df)
# # # # day_date = [{d[day.weekday()]: (str(day)[-2:])} for week in monthcal for day in week if day.month == month]



# # # creating a new dataframe with name and ltp values
# # # however, since the requirement is to have these within individual 
# # # columns and not rows, using transpose (T) to address it
# # df1 = pd.DataFrame([name,ltp]).T

# # # explicitly adding column names to the temp dataframe and the same will repeat
# # # everytime a new temp dataframe is formed. This will ensure that the new values
# # # get appended to the correct columns in the aggregated version
# # df1.columns = ['name', 'ltp']

# # # append the temp dataframe to the aggregated version to be published as final
# # df=df.append(df1,ignore_index=True)

# '''
# marker             place1       place2
# 45                  PQR           STU
# 145.0-100           ABC           DEF
# 267.0-175.8         GHI           KLM
# 145.0               ABC           DEF
# 267.0               GHI           KLM
# '''

# import pandas as pd
# import numpy as np

# df = pd.read_clipboard()

# # print(df)

# # #Split marker to temporary dataframe , split_m
# split_m = df.copy()

# # create the additional required columns with default 'NaN' values
# split_m.insert(1, 'firstkm', np.nan)
# split_m.insert(2, 'lastkm', np.nan)

# # unpack the splitted values to the columns. If nothing to unpack
# # for 'lastkm', it will become None
# split_m[['firstkm', 'lastkm']] = df.marker.str.split('-', expand=True)
# split_m.fillna(np.nan, inplace=True)

# print(split_m)
# # split_m.columns=['firstkm', 'lastkm'] #hitting error here
# # split_m = split_km[['firstkm', 'lastkm']].replace([None], np.nan)



# import re
# from urllib import request

# fhandler = request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_42.txt')

# res = list()
# pattern = re.compile(r'(((https?:\/\/)? | (www\.)?)+\S+\.(com|org)(\/\S+\/)*)')
# # pattern = re.compile(r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])')



# for line in fhandler:
#     line = line.decode().rstrip()
#     matches = pattern.findall(line)
    

#     if len(matches) != 0:
#         matches = list(matches[0])
#         matches = list(filter(None, matches))
#         matches = list(filter(' ', matches))
#         print(line)
#         print(matches)

#     if len(matches) != 0:
#         print(line)
#         print(matches, end='\n\n')

#         res.append(matches)

# print(res)


# tab separated data for read_clipboard()
# please make sure that you source data 
# has a separator other than space.
'''
marker	place1	place2
45	PQR	STU
145.0-100	ABC	DEF
267.0-175.8	GHI	KLM
145.0	ABC	DEF
267.0	GHI	KLM
P7.991-54.3	GHI	KLM
UPM Ex 0.5	PPP	SSS
'''

import pandas as pd
import numpy as np

df = pd.read_clipboard()

# #Split marker to temporary dataframe , split_m
split_m = df.copy()

# create the additional required columns with default 'NaN' values
split_m.insert(1, 'firstkm', np.nan)
split_m.insert(2, 'lastkm', np.nan)

# unpack the splitted values to the columns. If nothing to unpack
# for 'lastkm', it will become None
split_m[['firstkm', 'lastkm']] = df.marker.str.split('-', expand=True)
split_m.fillna(np.nan, inplace=True)

print(split_m)
# split_m.columns=['firstkm', 'lastkm'] #hitting error here
# split_m = split_km[['firstkm', 'lastkm']].replace([None], np.nan)