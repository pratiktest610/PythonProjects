# using csv module
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# using pandas

import pandas
data = pandas.read_csv("weather_data.csv")

# avg_temp = round(sum(temp_list) / len(temp_list), 2)
# print(avg_temp)
# print(data["temp"].mean())
#
# print(data["temp"].max())

# geting a row
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
temp = monday.temp

#  creating a data frame
data_dict = {
    "students": ["arjun", "bheem", "chatur"],
    "score": [90, 95, 80]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("data.csv")
