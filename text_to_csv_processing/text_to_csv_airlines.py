with open('../data_input/airlines.txt', 'r') as file:
    lines = file.readlines()

data = []

for line in lines:
    fields = line.strip().split(',')
    data.append(fields)

output_file = '../data_output/airlines.csv'

import csv

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Airline ID", "Name", "Alias", "IATA", "ICAO", "Callsign", "Country", "Active"])
    csvwriter.writerows(data)

