import json
json_data=open('data/m_aapl.json')
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
with open('test.json', 'w') as outfile:
    json.dump(json_dict, outfile)
         
json_data.close()