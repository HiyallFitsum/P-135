import pandas as pd
import csv
import matplotlib

rows = []

with open("main.csv")as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
headers[0] = "row_num"

temp_star_data_rows = list(star_data_rows)
for star_data in temp_star_data_rows:
    star_distance = star_data[2]
    star_mass = star_data[3]
    star_radius = star_data[4] 
    star_gravity = star_data[5]




