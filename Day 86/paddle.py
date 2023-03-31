from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1,5)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    