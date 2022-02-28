import json
import csv

with open('01x01.json') as json_file:
    data = json.load(json_file)

script = data['01x01']

data_file = open('01x01.csv', 'w', newline='')

csv_writer = csv.writer(data_file, delimiter='/')

count = 0

for  quote in script:
    if count == 0:

        header = quote.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(quote.values())

data_file.close()

