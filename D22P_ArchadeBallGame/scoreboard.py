from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, pos, color):
        super().__init__()
        self.score = 0
        self.color(color)
        self.hideturtle()
        self.penup()
        self.goto(pos, 150)
        self.write(f"{self.score}", font=("Courier", 100, "bold"), align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", font=("Courier", 100, "bold"), align="center")
