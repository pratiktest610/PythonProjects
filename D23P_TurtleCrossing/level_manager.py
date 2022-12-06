from turtle import Turtle


class LevelManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 18, "bold"))
        self.time = 0.1

    def level_up(self):
        self.clear()
        self.level += 1
        self.time *= 0.9
        self.write(f"Level: {self.level}", align="center", font=("Courier", 18, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 48, "bold"))


