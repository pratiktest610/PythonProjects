from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#EAF6F6")
        self.penup()
        self.xmove = 15
        self.ymove = 15
        self.time = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1

    def hitback(self):
        self.xmove *= -1

    def intensefyi(self):
        self.time *= 0.9

    def reset_time(self):
        self.time = 0.1
