
## Opening and printing data as a list

# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# Selecting specific data
import csv

with open ("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
