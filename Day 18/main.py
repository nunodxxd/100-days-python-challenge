from turtle import Screen, Turtle
import random
import turtle

timmy = Turtle()
timmy.shape("arrow")

# dash line - challenge 2
"""
for _ in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
"""

# draw shapes with random colors - challenge 3
"""
def r(): return random.randint(0, 1)
def draw_shape(start_num_sides, last_num_sides):
    angle = 360
    for x in range(start_num_sides, last_num_sides):
        timmy.pencolor(r(), r(), r())
        for _ in range(x):
            timmy.forward(100)
            timmy.right(angle/x)
draw_shape(3, 12)
"""

# Random walk - challenge 4
"""
def r(): return random.randint(0,1)
def angle(): return random.choice([90,180,270,360])
timmy.speed(10)
timmy.pensize(10)

def walk(times):
    for _ in range(times):
        timmy.pencolor(r(), r(), r())
        timmy.forward(50)
        timmy.setheading(angle())

walk(100)
"""

# make a spirograph - challenge 5
"""
def r(): return random.randint(0,1)
timmy.speed(0)

def draw_circle(degree_between):
    for _ in range(round(360 / degree_between)):
        timmy.pencolor(r(), r(), r())
        timmy.setheading(timmy.heading() + degree_between)
        timmy.circle(100)
        
draw_circle(5)
"""

# Final project
screen = Screen()
screen.setworldcoordinates(-50,-50,500,500)
screen.colormode(255)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
timmy.penup()
timmy.hideturtle()
timmy.speed(10)

def draw_dots(number):
    for x in range(0,number):
        timmy.sety(x*50)
        for y in range(0,number):
            timmy.setx(y*50)
            timmy.dot(20,random.choice(color_list))

#draw 10 lines of dots with 10 dots each one          
draw_dots(10)

screen.exitonclick()
