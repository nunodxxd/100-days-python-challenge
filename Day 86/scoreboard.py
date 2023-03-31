from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",70,"normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle() 
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250,310) 
        self.write(f'{self.score}', align=ALIGNMENT,font=FONT) 
  
    def point(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,-100)
        self.write("Game Over", align=ALIGNMENT,font=FONT)