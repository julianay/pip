#load json price and message data and merge
import json
import pandas as pd
from pandas import DataFrame
import numpy as np
import glob
import re

#extracting file name
start = '/'
end = '.json'
#get all files path from folder that end in csv and put in list
fileList_json = glob.glob('newData/*.json')
#extract the filename (stockSymbol) for each path
for filename in fileList_json:
    stockSymbol = re.search('%s(.*)%s' % (start, end), filename).group(1)
    #selecting only the message files (to avoid duplicating the files since there are also price files)
    if(stockSymbol[0]== 'm'):
        #setting file name for messages, and cutting the "m_" part of the chars
        fileMessage = 'newData/' + "m_" + stockSymbol[2:] + '.json'
        #setting file name for prices
        filePrice = 'newData/' + "p_" + stockSymbol[2:] + '.json'
        #setting output file name
        filePathOut = 'data/' + "frame_" + stockSymbol[2:] + '.json'

        #loading message
        json_data_m=open(fileMessage)
        json_str_m = json_data_m.read()
        json_dict_m = json.loads(json_str_m)
        json_data_m.close()

        #loading price
        json_data_p=open(filePrice)
        json_str_p = json_data_p.read()
        json_dict_p = json.loads(json_str_p)
        json_data_p.close()
        
        #converting dates on price and message files to merge the data
        frame_p = DataFrame(json_dict_p)
        frame_p['date'] = pd.to_datetime(frame_p['date'])
        
        #select the columns that will be used in dataframe
        frame_m = DataFrame(json_dict_m, columns=['timestamp', 'date', 'messages'])
        frame_m['date'] = pd.to_datetime(frame_m['timestamp'])
        frame_m.drop('timestamp', 1)
        
        #merging message and price
        frame = pd.merge(frame_m, frame_p, on='date', how='outer')
        frame = frame[frame.timestamp != np.nan]

        #dropping empty rows in timestamp
        frame = frame.dropna(subset=['timestamp'])

        #padding the missing weekend and holidays - fill values forward
        frame = frame.fillna(method='pad')
        #print(frame.timestamp)
        frame.to_json(filePathOut, orient='records')
        frame.to_csv('data/' + stockSymbol + '.csv')