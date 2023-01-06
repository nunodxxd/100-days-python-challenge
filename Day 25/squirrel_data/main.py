from turtle import color
import pandas 

data = pandas.read_csv("squirrel-data.csv")

# my solution if we unknow the colors
""" colors = {}
for color in data:
    if color not in colors:
        if str(color) != "nan":
            colors[color] = 0
    else:
        colors[color] += 1    

print(colors) """


grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Grey","Cinnamon","Black"],
    "Count" : [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")