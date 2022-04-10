from turtle import Turtle
from settings import START_LENGTH,SNAKE_WIDTH, MOVE_DISTANCE,UP,DOWN,LEFT,RIGHT

class Snake:
    def __init__(self):
        self.tail_squares = []
        self.create_snake()
        self.head = self.tail_squares[0]
        self.head.setheading(0)

    def create_snake(self):
        for pos in range(START_LENGTH):
            self.add_segment((0,0))

    def add_segment(self,pos):
            tail = Turtle(shape="square")
            tail.color("white")
            tail.penup()
            tail.speed("fastest")
            tail.goto(pos)
            
            self.tail_squares.append(tail)

    def extend(self):
        self.add_segment(self.tail_squares[-1].position())

    def detect_collision(self):
        for square in self.tail_squares[1:]:
            if self.head.distance(square)<15 and self.head.distance(square) <15:
                return True

    def move(self):
        for square in range(len(self.tail_squares) - 1, 0, -1):
            new_x = self.tail_squares[square - 1].xcor()
            new_y = self.tail_squares[square - 1].ycor()
            self.tail_squares[square].goto(new_x,new_y)
            
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
