from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('green')
        self.speed('fastest')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()
               
    def refresh(self):
        x_rand = random.randint(-270, 270)
        y_rand = random.randint(-270, 270)
        self.goto(x_rand, y_rand)