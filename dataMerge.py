#load json price and message data and merge
import json
import pandas as pd
import numpy as np

from pandas import DataFrame

#loading message
json_data_m=open('newData/m_aapl.json')
json_str_m = json_data_m.read()
json_dict_m = json.loads(json_str_m)
json_data_m.close()

#loading price
json_data_p=open('newData/p_aapl.json')
json_str_p = json_data_p.read()
json_dict_p = json.loads(json_str_p)
json_data_p.close()

frame_p = DataFrame(json_dict_p)
frame_p['date'] = pd.to_datetime(frame_p['date'])

frame_m = DataFrame(json_dict_m, columns=['timestamp', 'date', 'messages'])
frame_m['date'] = pd.to_datetime(frame_m['timestamp'])
frame_m.drop('timestamp', 1)

frame = pd.merge(frame_m, frame_p, on='date', how='outer')
frame = frame[frame.timestamp != np.nan]

#dropping empty rows in timestamp
frame = frame.dropna(subset=['timestamp'])

#padding the missing weekend and holidays - fill values forward
frame = frame.fillna(method='pad')
#print(frame.timestamp)
frame.to_json('data/frame_aapl.json', orient='index')
frame.to_csv('data/frame_aapl.csv')