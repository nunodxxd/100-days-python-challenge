#####open without lib
""" with open("weather-data.csv") as file:
    data = file.read().splitlines()

print(data) """

####open with csv lib
""" import csv

with open("weather-data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures) """

####open with panda lib
import pandas

data = pandas.read_csv("weather-data.csv")
#print(data["temp"])

#### conversion example ####
#data_dict = data.to_dict()

#### challenge temperature mean ####
## my solution:
""" temp_list = data["temp"].to_list()
average = sum(temp_list)/len(temp_list)
print(average) """

## best solution:
#print(data["temp"].mean())

#### challenge temperature max ####
#print(data["temp"].max())
# or
#print(data.temp.max())

#### Get data in row ####
#print(data[data.day =="Monday"])

#### Challenge get row data of day with max temperature ###
#print(data[data.temp == data.temp.max()])

#### acess data row with specific field ####
""" monday = data[data.day =="Monday"]
print(monday.condition)
 """
#### challenge convert temperature to fahrenheit
""" monday = data[data.day =="Monday"]
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)
 """

#### create a dataframe from scratch
""" data_dict = {
    "students": ["amy"],
    "scores": [76]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
 """