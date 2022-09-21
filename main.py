from turtle import Turtle, Screen, xcor
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
    for snake_num in range(len(snakes) -1, 0, -1):
        new_x = snakes[snake_num - 1].xcor()
        new_y = snakes[snake_num - 1].ycor()
        snakes[snake_num].goto(new_x, new_y)
    snakes[0].forward(20)














screen.exitonclick()