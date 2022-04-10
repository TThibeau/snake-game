from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import os
from time import sleep
from settings import WINDOW_HEIGHT,WINDOW_WIDTH,wall_y_min,wall_x_max,wall_x_min,wall_y_max
os.system('cls || clear')

screen = Screen()
screen.setup(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
screen.title(titlestring="Snake game")
screen.tracer(0)
screen.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    sleep(0.1)
    
    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        food.change_pos()
        snake.extend()

    collision = snake.detect_collision()

    if snake.head.xcor()<wall_x_min or snake.head.xcor()>wall_x_max or snake.head.ycor()<wall_y_min or snake.head.ycor()>wall_y_max or collision:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()