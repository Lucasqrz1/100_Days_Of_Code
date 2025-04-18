
## Opening and printing data as a list

# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#
# # Selecting specific data
# import csv
#
# with open ("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
#
data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # Calculating average
# average = sum(temp_list) / len (temp_list)
# print(average)
#
# #Another form of calculating average
# print(data["temp"].mean())
#
# # Get max value
# print(data["temp"].max())
#
# #Get data in columns
# print(data["condition"])
# # or
# print(data.condition)

#Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# converting to Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 +32
print(monday_temp_F)

# Creat dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
