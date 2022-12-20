from turtle import Turtle, Screen

# instantiate and print a new object of the class Turtle
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)

# instantiate a new object of the class Screen
my_screen = Screen()
# atribute of the screen
print(my_screen.canvheight)
# method of the screen
my_screen.exitonclick()
