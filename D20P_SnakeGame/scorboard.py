from turtle import Turtle



class ScoreBoard(Turtle):

    def __init__(self,):
        super().__init__()
        self.color("#80558C")
        self.pu()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as file:
            score = file.read()
        self.high_score = int(score)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 16, "bold"))

    def increase_score(self):
        self.score += 1
        self.print_score()

    def gameover(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.print_score()
        self.score = 0
        self.print_score()
