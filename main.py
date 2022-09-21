from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
#creating a screen size for the game
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Creating a snake body with three square shape side by side
# starting_position = [(0,0), (-20, 0), (-40, 0)]
# snakes = []
# for position in starting_position:
#     snake = Turtle('square')
#     snake.color('white')
#     snake.penup()
#     snake.goto(position)
#     snakes.append(snake)

snake = Snake()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    #looping through the len of the snakes to hold the x and y axis of the snakes
    snake.move()
    














screen.exitonclick()