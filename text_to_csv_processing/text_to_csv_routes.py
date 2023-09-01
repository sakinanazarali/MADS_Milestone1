with open('../data_input/routes.txt', 'r') as file:
    lines = file.readlines()

data = []

for line in lines:
    fields = line.strip().split(',')
    data.append(fields)

import csv

output_file = '../data_output/routes.csv'

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Airline", "Airline ID", "Source Airport", "Source Airport ID", "Destination Airport", "Destination Airport ID", "Codeshare", "Stops", "Equipment"])
    csvwriter.writerows(data)
