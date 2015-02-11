#this reverses json data files both for messages and prices

import json
from pprint import pprint
#json_data=open('data/p_msft.json')
json_data=open('data/p_twtr.json')
new_data = []
data = json.load(json_data)
for da in range((len(data)-1), -1, -1):
    new_data.append(data[da])
json_data.close()
with open('data/pn_twtr.json', 'w') as outfile:
    json.dump(new_data, outfile)
    
'''
numbers = range(0, 10)
for number in range(10, -1, -1):
    print(number)
'''    