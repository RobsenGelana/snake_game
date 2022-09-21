from turtle import Turtle
#Defining a CONSTANT variable
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVEMENT = 20
class Snake:
    def __init__(self) -> None:
        self.snakes = []
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITION:
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(position)
            self.snakes.append(snake)

    def move(self):
        for snake_num in range(len(self.snakes) -1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.snakes[0].forward(MOVEMENT)  