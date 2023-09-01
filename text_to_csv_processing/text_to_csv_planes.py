with open('../data_input/planes.txt', 'r') as file:
    lines = file.readlines()

data = []

for line in lines:
    fields = line.strip().split(',')
    data.append(fields)

output_file = '../data_output/planes.csv'

import csv

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "IATA Code", "ICAO Code"])
    csvwriter.writerows(data)