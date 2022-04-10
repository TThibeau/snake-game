from turtle import Turtle
from settings import WINDOW_HEIGHT

ALIGNMENT = "center"
FONT = ('Arial',24,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0,(WINDOW_HEIGHT/2)-40)
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Game over - Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)
