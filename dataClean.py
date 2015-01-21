import csv
import json
empty_dict = {}
with open('historicalPrices/msft.csv', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['date', 'close', 'volume', 'open', 'high', 'low'])
    test = [row for row in cin]
    #print(test)
    for i in reversed(test): 
        print(i) 
        

with open('p_msft.json', 'w') as outfile:
    json.dump(test, outfile)

#myList = [i for i in range(10)]
#print(myList)


'''
for i in reversed(myList): 
    print(i) 
'''    