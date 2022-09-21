from turtle import Turtle, Screen


screen = Screen()
#creating a screen size for the game
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

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
    for snake in snakes:
        snake.forward(20)
        














screen.exitonclick()