from turtle import Turtle
from random import randint
from settings import wall_x_max,wall_x_min,wall_y_max,wall_y_min

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 
        self.speed("fastest")
        self.change_pos()
        
    def change_pos(self):
        self.penup()
        random_x = randint(wall_x_min,wall_x_max)
        random_y = randint(wall_y_min,wall_y_max)
        x_y = (random_x,random_y)
        self.goto(x_y)
        self.pendown()