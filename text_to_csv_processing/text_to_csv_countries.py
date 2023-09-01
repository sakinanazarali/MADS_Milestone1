with open('../data_input/countries.txt', 'r') as file:
    lines = file.readlines()

data = []

for line in lines:
    fields = line.strip().split(',')
    data.append(fields)

import csv

output_file = '../data_output/countries.csv'

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["name", "iso_code", "dafif_code"])
    csvwriter.writerows(data)
