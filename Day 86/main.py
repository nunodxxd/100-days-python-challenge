import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=800)
screen.tracer(0)

bricks = Bricks.create_wall()
paddle = Paddle((0,-350))

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "a")
screen.onkeypress(paddle.go_right, "d")

ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect left and right wall Collision
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    #Detect top wall collision
    if ball.ycor() > 380:
        ball.bounce_y()

    #Detect paddle collision
    if ball.distance(paddle) < 50 and ball.ycor() > -330:
        ball.bounce_y()

    #Detect when paddle misses
    if ball.ycor() < -380:
        ball.reset_position()
        scoreboard.game_over()
        ball.stop()

    #Detect brick collision
    for brick in bricks:
        if brick.collision(ball) == "top" or brick.collision(ball) == "bottom":
            ball.bounce_y()
            brick.hit()
            scoreboard.point()
        elif brick.collision(ball) == "left" or brick.collision(ball) == "right":
            ball.bounce_x()
            brick.hit()
            scoreboard.point()


screen.exitonclick()