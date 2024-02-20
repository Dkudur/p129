import pandas as pd
import csv

d1 = []
d2 = []

with open("converted_data.csv", "r") as f:
    a = csv.reader(f)
    for row in a:
        d1.append(row)

with open("bright_stars.csv", "r") as f:
    a = csv.reader(f)
    for row in a:
        d2.append(row)

headers1 = d1[0]
headers2 = d2[0]

planet_data1 = d1[1:]
planet_data2 = d2[1:]

headers = headers1 + headers2

planet_data = []


for i in planet_data1:
    planet_data.append(i)

for i in planet_data2:
    planet_data.append(i)

with open("final.csv", "a+") as f:
    a = csv.writer(f)
    a.writerow(headers)
    a.writerows(planet_data)

