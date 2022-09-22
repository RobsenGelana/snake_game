from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
#creating a screen size for the game
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecting collision food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    #Detecting collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score_board.game_over() 
    #Detecting collision with tail
    for x in snake.snakes[1:]:
      if snake.head.distance(x) < 10:
        game_on = False
        score_board.game_over()















screen.exitonclick()