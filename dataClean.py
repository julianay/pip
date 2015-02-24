#Converts csv to json and put data in order of older to newest

import csv
import json
import glob
import re



#extracting file name
start = '/'
end = '.csv'
#get all files path from folder that end in csv and put in list
fileList_csv = glob.glob('rawData/*.csv')
#extract the filename (stockSymbol) for each path
for filename in fileList_csv:
    data_reverse = []
    stockSymbol = re.search('%s(.*)%s' % (start, end), filename).group(1)
    #create new filename path for output
    filePathOut = 'newData/' + "p_" + stockSymbol + '.json'

    with open(filename, 'rt') as fin:
        cin = csv.DictReader(fin)
        pRow = [row for row in cin]
        for da in range((len(pRow)-1), -1, -1):
            pRow[da]['stock'] = stockSymbol
            data_reverse.append(pRow[da])
            
    with open(filePathOut, 'w') as outfile:
        json.dump(data_reverse, outfile)

#also look for json files in folder and reverse
fileList_json = glob.glob('rawData/*.json')

end = '.json'

for filename in fileList_json:
    stockSymbol = re.search('%s(.*)%s' % (start, end), filename).group(1)
    #create new filename path for output
    filePathOut = 'newData/' + "m_" + stockSymbol + '.json'
    json_data=open(filename)
    new_data = []
    data = json.load(json_data)
    for da in range((len(data)-1), -1, -1):
        #changes volume_score to messages
        data[da]['messages'] = data[da].pop('volume_score')
        data[da]['stock'] = stockSymbol
        new_data.append(data[da])
        json_data.close()
        with open(filePathOut, 'w') as outfile:
            json.dump(new_data, outfile)           
