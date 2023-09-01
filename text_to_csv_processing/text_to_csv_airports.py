with open('../data_input/airports.txt', 'r') as file:
    lines = file.readlines()

data = []

for line in lines:
    fields = line.strip().split(',')
    data.append(fields)

output_file = '../data_output/airports.csv'

import csv

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["ID", "Name", "City", "Country", "IATA", "ICAO", "Latitude", "Longitude", "Altitude", "Timezone", "DST", "TzDatabase", "Type", "Source"])
    csvwriter.writerows(data)

