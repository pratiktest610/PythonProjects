from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos, color):
        super().__init__()
        self.shape("square")
        self.seth(90)
        self.shapesize(1, 5)
        self.color(color)
        self.pu()
        self.goto(pos, 0)

    def up(self):
        if self.ycor() < 240:
            self.fd(50)

    def down(self):
        if self.ycor() > -240:
            self.bk(50)
