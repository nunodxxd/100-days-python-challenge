from turtle import Turtle, position

class Bricks(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(2.3,2.5)
        self.penup()
        self.goto(position)
        self.width = self.shapesize()[0] * 10
        self.height = self.shapesize()[1] * 10

    @staticmethod
    def create_wall():
        bricks = []
        for i in range(-270, 290, 54):
            for j in range(300, 0, -50):
                new_brick = Bricks((i, j))
                new_brick.stamp()
                bricks.append(new_brick)
        return bricks

    def collision(self, ball):
        # calculate the coordinates of the edges of the brick
        brick_top = self.ycor() + self.shapesize()[0] * 10
        brick_bottom = self.ycor() - self.shapesize()[0] * 10
        brick_left = self.xcor() - self.shapesize()[1] * 10
        brick_right = self.xcor() + self.shapesize()[1] * 10

        # calculate the coordinates of the edges of the ball
        ball_left = ball.xcor() - ball.radius
        ball_right = ball.xcor() + ball.radius
        ball_top = ball.ycor() + ball.radius
        ball_bottom = ball.ycor() - ball.radius

        if ball_bottom <= brick_top and ball_top >= brick_bottom and ball_right >= brick_left and ball_left <= brick_right:
            if ball_bottom <= brick_top and ball_top >= brick_top - 5:
                return "top"
            elif ball_top >= brick_bottom and ball_bottom <= brick_bottom + 5:
                return "bottom"
            elif ball_right >= brick_left and ball_left <= brick_left + 5:
                return "left"
            elif ball_left <= brick_right and ball_right >= brick_right - 5:
                return "right"
            return None
        
    def hit(self):
        self.hideturtle()
        self.clear()
        self.goto(1000,1000)