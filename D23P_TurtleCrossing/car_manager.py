from turtle import Turtle
import random
COLORS = "red orange yellow purple green pink black gold2 maroon3".split(" ")


class CarManager:

    def __init__(self):
        self.cars = []
        self.make_cars()

    def make_cars(self):
        for color in COLORS:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(color)
            y = random.randint(-240, 240)
            new_car.goto(310, y)
            new_car.seth(180)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            step = random.randint(0, 10)
            car.fd(step)

            if car.xcor() < -300:
                y = random.randint(-240, 240)
                car.goto(310, y)


