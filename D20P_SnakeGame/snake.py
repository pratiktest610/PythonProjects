from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []
        self.create(3)
        self.head = self.segments[0]

    def create(self, no):
        for i in range(no):
            new_segment = Turtle("turtle")
            new_segment.pu()
            new_segment.color("#D75281")
            new_segment.goto(0, 0)
            self.segments.append(new_segment)

    def move(self):
        heading = self.head.heading()
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
            self.segments[index].seth(heading)
        self.segments[0].fd(20)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments = []
        self.create(3)
        self.head = self.segments[0]




    def turn_right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)
