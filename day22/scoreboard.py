from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore,align="center",font=('Courier',80,'normal'))
        self.goto(100,200)
        self.write(self.rscore,align="center",font=('Courier',80,'normal'))
    def l_point(self):
        self.lscore += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()