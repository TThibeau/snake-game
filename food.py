from turtle import Turtle
from random import randint
from settings import min_x,max_x,min_y,max_y,MOVE_DISTANCE

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
        random_x = randint(min_x,max_x)*MOVE_DISTANCE
        random_y = randint(min_y,max_y)*MOVE_DISTANCE
        x_y = (random_x,random_y)
        self.goto(x_y)
        self.pendown()