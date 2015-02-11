# 72 hours starting with midnight Jan 1st, 2011
import json
import pandas as pd
from numpy import random
from pandas import Series
from pandas import DataFrame

#loading message
json_data_m=open('data/mm_aapl.json')
json_str_m = json_data_m.read()
json_dict_m = json.loads(json_str_m)

#loading price
json_data_p=open('data/pn_aapl.json')
json_str_p = json_data_p.read()
json_dict_p = json.loads(json_str_p)

frame_p = DataFrame(json_dict_p)
frame_p['date'] = pd.to_datetime(frame_p['date'])

frame_m = DataFrame(json_dict_m, columns=['timestamp', 'date', 'messages'])
frame_m['date'] = pd.to_datetime(frame_m['timestamp'])
frame_m.drop('timestamp', 1)

#this may work but it's ugly. 
'''
for j in frame_p['date']:
    #print('p: ', j)
    for i in frame_m['date']:
        if j == i:
            print(i)
            print("found")
'''       

print(pd.merge(frame_m, frame_p, on='date', how='outer'))
