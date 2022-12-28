from genericpath import exists
from turtle import Turtle, Screen
from random import randint, random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

valid_input = False
while not valid_input:
    input = screen.textinput(
        title="Make your bet", prompt="Whick turtle will win the race? enter a color: ")
    if input in colors:
        valid_input = True

y_height = -100
for index, turtle_color in enumerate(colors):
    turtle_color = Turtle(shape="turtle")
    turtle_color.color(colors[index])
    turtle_color.penup()
    turtle_color.goto(x=-230, y=y_height)
    y_height += 40
    all_turtle.append(turtle_color)

is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == input:
                print(f"User win! turtle {winner} win!")
            else:
                print(f"User lose! turtle {winner} win!")
            is_race_on = False
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
