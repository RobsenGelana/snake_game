from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_screen()

    def update_screen(self):
        self.write(f"Score: {self.score}", align='center',  font=('Arial', 25, 'normal'))
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center',  font=('Arial', 25, 'normal'))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_screen()
       
        