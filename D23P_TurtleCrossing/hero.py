from turtle import Turtle


class Hero(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow green")
        self.seth(90)
        self.goto(0, -280)

    def up(self):
        self.fd(10)
