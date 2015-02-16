#Converts csv to json and put data in order of older to newest

import csv
import json
import glob
import re

data_reverse = []

#extracting file name
start = '/'
end = '.csv'
#get all files path from folder that end in csv and put in list
fileList = glob.glob('prices/*.csv')
#extract the filename (stockSymbol) for each path
for filename in fileList:
    stockSymbol = re.search('%s(.*)%s' % (start, end), filename).group(1)
    #create new filename path for output
    filePathOut = 'testFolder/' + stockSymbol + '.json'

    with open(filename, 'rt') as fin:
        cin = csv.DictReader(fin)
        test = [row for row in cin]
        for da in range((len(test)-1), -1, -1):
            data_reverse.append(test[da])    
            
    with open(filePathOut, 'w') as outfile:
        json.dump(data_reverse, outfile)
