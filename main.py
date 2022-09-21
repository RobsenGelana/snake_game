from turtle import Turtle, Screen


screen = Screen()
#creating a screen size for the game
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0,0), (-20, 0), (-40, 0)]
for position in starting_position:
    turtle = Turtle('square')
    turtle.color('white')
    turtle.goto(position)















screen.exitonclick()