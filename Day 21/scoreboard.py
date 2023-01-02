from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",24,"normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)  
        self.score = 0
        self.update_scoreboard() 

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT,font=FONT)