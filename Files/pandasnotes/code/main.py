# TODO: Open CSV File and read data
# with open("./weather_data.csv") as weather_file:
#     weather_list = []
#     for weather in weather_file.readlines():
#         striped_name = weather.strip("\n")
#         weather_list.append(striped_name)
# print(weather_list)
# The list that is printed is hard to work with
    # ['day,temp,condition', 'Monday,12,Sunny', 'Tuesday,14,Rain', etc...]
    # so, instead we can use built-in library to help us work with csv
#***********************************************************************************
# built-in csv reading and writing library
# import csv
# TODO: Open CSV File and read data
# with open("./weather_data.csv") as weather_file:
#     # csv.reader(), takes the file passed in, reads it and outputs the data
#     # returns a csv reader object, that can be looped through
#     weather_data = csv.reader(weather_file)
#     # print(weather_data)# csv reader object


    # get each row in the data
    # for row in weather_data:
    #     print(row)
    # print(weather_data)# csv reader object

# # TODO: loop through the data and add the temperatures as numbers to the temperatures list
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#****************************************************************

# # TODO: loop through the data and add the temperatures as numbers to the temperatures list
    # temperatures = []
    # my_list = []
    # for row in weather_data:
    #     my_list.append(row[1])
    # my_list.remove("temp")
    # for temp in my_list:
    #     new_temp = int(temp)
    #     temperatures.append(new_temp)
    # print(temperatures)
#******************************************************************************************
# the built-in csv module can be hard to work with if we have a lot of data
# This is where Pandas come in
import pandas


# TODO: Open CSV File and read data
weather_data = pandas.read_csv("./weather_data.csv")
# # Pandas********************************************************
# print(f"Data Frame Object:\n{weather_data}")
# # type is a pandas data frame object
# # print(type(weather_data))
# # Pandas********************************************************
# # # TODO: loop through the data and add the temperatures as numbers to the temperatures list
# # Pandas automatically knows how to find the data in the "temp" column, so no need to use loop
# # TODO Get all the temperatures(Get Data Column)
# # Treating it as a dictionary and getting each column by the key
# print(f"Panda Data Series Object:\n{weather_data["temp"]}")# type is a panda data series object
# # Pandas********************************************************
# # Treating it like an object
# # Under the hood, Pandas takes each of the columns headings and converts them to attributes
# print(f"Alternative Panda Data Series Object:\n{weather_data.temp}")# type is a panda data series object
# # Pandas********************************************************
# # to_dict() converts the data to a dictionary
# data_dict = weather_data.to_dict()
# print(f"Dictionary:\n{data_dict}")
# # Pandas********************************************************
# # to_list() can convert a series to a list
# temp_list = weather_data["temp"].to_list()
# print(f"List:\n{temp_list}")
#
# # TODO: Get the average of the temperatures
# # Python**************************************************
# # average_temp = sum(temp_list) / len(temp_list)
#
# # Pandas********************************************************
# # with pandas, you can get the mean, median, mode etc...
# average_temp = weather_data["temp"].mean()
# print(f"Average: {average_temp}")
# # Pandas********************************************************
# # TODO: Get the max value from the temperatures
# max_temp = weather_data["temp"].max()
# print(f"Max: {max_temp}")
# Pandas********************************************************
# TODO: Get row of data
# get the entire row where the day is equal to Monday
# monday_row = weather_data[weather_data.day == "Monday"]
#OR******************************************************
# monday_row = weather_data[weather_data["day"] == "Monday"]
# print(f"Monday Row:\n{monday_row}")
#
# # TODO: Get the entire row of data which has the highest temperature
# highest_temp = weather_data[weather_data.temp == weather_data["temp"].max()]
# print(f"Row with Highest Temperature:\n{highest_temp}")
# Pandas********************************************************

# TODO Get a particular piece of data from the row
# monday_row = weather_data[weather_data["day"] == "Monday"]
# # # Get Monday's row condition
# # print(monday_row.condition)
#
# # Get Monday's row temperature in Far
# # print(monday_row.temp)# returns 0    12
# # print(monday_row.temp[0])# returns 12
# celsius_temp = monday_row.temp[0]
# fahrenheit_temp = (celsius_temp * 9/5) + 32
# print(fahrenheit_temp)
#**********************************************************


# TODO: Create a Data Frame
data_dict = {
    "students": ["James", "Lisa", "Rita", "Keon", "Rider"],
    "scores": [89, 76, 82, 100, 73]
}
my_data = pandas.DataFrame(data_dict)
print(my_data)

# TODO: Convert Data to CSV File
my_data.to_csv("new_data.csv")
#************************************************************************************************
# from numpy.ma.extras import average
# average_temp = average(temp_list)
# print(average_temp)