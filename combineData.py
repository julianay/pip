# on the messages data, changes 'volume_score' to messages 
# because prices also has a field named 'volume_score"

import json
json_data=open('data/m_twtr.json')
json_str = json_data.read()
json_dict = json.loads(json_str)
#print(json_dict[0].keys())
#for key in json_dict[0].items():
    #print(key)

for i in json_dict: 
    i['messages'] = i.pop('volume_score')
    #print(i['messages'])
    #print(i['volume_score'])

print(json_dict)    
with open('data/mm_twtr.json', 'w') as outfile:
    json.dump(json_dict, outfile)
         
json_data.close()