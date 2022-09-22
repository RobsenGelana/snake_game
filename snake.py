from turtle import Turtle
#Defining a CONSTANT variable
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVEMENT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self) -> None:
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_snake(position)
    def add_snake(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)
    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for snake_num in range(len(self.snakes) -1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVEMENT)  
    
    def up(self):
        if self.head.heading() != DOWN:
          self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
          self.head.setheading(LEFT)