import csv
import json

filename = 'products.csv'
with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        # print(row['additional_fields'])
        json_field = json.loads(row['additional_fields'])
        row['additional_fields'] = json_field
        print(row)