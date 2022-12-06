import random
import turtle
from turtle import Turtle, Screen

display = Screen()
display.bgcolor("grey")

tim = Turtle()
tim.shape("turtle")
tim.color("yellow green")

# # Draw a square
# for i in range(4):
#     tim.fd(100)
#     tim.right(90)

# # Draw a dashed line
# for i in range(50):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()

# # Draw polygons
# import random
# colors = "red green blue orange yellow pink".split(" ")
# for sides in range(3, 12):
#     tim.color(random.choice(colors))
#     angle = 360/sides
#     for side in range(sides):
#         tim.fd(100)
#         tim.right(angle)

# # Random Walk
# # speed thick
# colors = "red green blue orange yellow pink brown".split(" ")
# tim.speed("fastest")
# tim.pensize(10)
# for i in range(10000):
#     tim.color(random.choice(colors))
#     tim.fd(75)
#     heading = random.choice([0, 90, 180, 270])
#     tim.seth(heading)

# # Random color gen
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r, g, b)
#     return color
#
#
# tim.speed("fastest")
# tim.pensize(10)
# for i in range(300):
#     tim.color(random_color())
#     tim.fd(75)
#     heading = random.choice([0, 90, 180, 270])
#     tim.seth(heading)

# spirograph
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


display.bgcolor("white")
tim.speed(0)
tim.shape("arrow")
for i in range(0, 360, 10):
    tim.color(random_color())
    tim.seth(i)
    tim.circle(100)



display.exitonclick()
