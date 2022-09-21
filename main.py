from turtle import Turtle, Screen
import time

screen = Screen()
#creating a screen size for the game
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Creating a snake body with three square shape side by side
starting_position = [(0,0), (-20, 0), (-40, 0)]
snakes = []
for position in starting_position:
    snake = Turtle('square')
    snake.color('white')
    snake.penup()
    snake.goto(position)
    snakes.append(snake)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for snake in snakes:
        snake.forward(20)
        














screen.exitonclick()