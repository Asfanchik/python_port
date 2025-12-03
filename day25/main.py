# with open("weather_data.csv") as data:
#     wether = data.readlines()
#     print(wether)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data =  csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] !="temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#import monday
import pandas

#data = pandas.read_csv("weather_data.csv") # open file
#print(data["temp"])

#data_dict = data.to_dict()#convert DataFrame to dictionare
#print(data_dict)

# temp_list = data["temp"].to_list()# - return list of values
# print(len(temp_list))
#
# ava = sum(temp_list) / len(temp_list)
# print(ava)
#
# max_value = max(temp_list)
# print(max_value)
#
# print(data.day)
#
# #Get Data is Colums
# print(data["condition"])
# print(data.condition)
#
# #Get Data in Row
#print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
#monday = data[data.day == "Monday"]
#monday_temp = monday.temp[0]
#monday_temp_F = monday_temp * 9/5 + 32
#print(monday_temp_F)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(grey)
print(red)
print(black)