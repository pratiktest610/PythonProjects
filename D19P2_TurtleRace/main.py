from turtle import Turtle, Screen
import random

display = Screen()
display.setup(500, 400)
users_bet = display.textinput("Make you bet!!", "Enter you turtle's color.")
on = False

colors = "purple indigo blue green yellow orange red".split(" ")
turtles = []
y = -90

for color in colors:
    turtle = Turtle("turtle")
    turtle.pu()
    turtle.color(color)
    turtle.goto(-230, y)
    y += 30
    turtles.append(turtle)

if users_bet:
    on = True

while on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            on = False
            win_color = turtle.pencolor()
            if win_color == users_bet:
                print(f"You WON. {win_color} turtle finished first")
            else:
                print(f"You LOST. {win_color} turtle finished first")

        dist = random.randint(0, 10)
        turtle.fd(dist)

display.exitonclick()
