import glob
from zipfile import ZipFile
import pandas as pd

path = r'/home/anshul/youtube/stackoverflow/zip_files' # use your path

#load all zip files in folder
all_files = glob.glob(path + "/*.zip")
# print(all_files)

df_master = pd.DataFrame()
flag = False

for filename in all_files:    
    zip_file = ZipFile(filename)
    for text_file in zip_file.infolist():
        if text_file.filename.endswith('Bezirke.csv'):
            df = pd.read_csv(zip_file.open(text_file.filename), 
            delimiter=';', 
            header=0, 
            index_col=['Timestamp'], 
            parse_dates=['Timestamp']
            )
    if not flag:
        df_master = df
        flag = True
    else:
        df_master = pd.concat([df_master, df])

print(df_master)    

    # print(tmp_dict)
    # df = pd.DataFrame(tmp_dict, index=['Timestamp'])

    # if idx == 0:
    #     df_master = df
    #     idx += 1
    # else:
    #     df_master = pd.concat([df_master, df])

#print dataframe in console
# print(df_master)

#prepare date to export to csv
# frame = pd.concat(df, axis=0)

#export to csv
# frame.to_csv( "combined_zip_Bezirke.csv", encoding='utf-8-sig')
# print("Export to CSV Successful")