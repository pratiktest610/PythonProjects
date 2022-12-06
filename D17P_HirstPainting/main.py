# import colorgram
#
# colors = colorgram.extract("image.jpeg", 30)
#
# colors_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_rgb = (r, g, b)
#     colors_rgb.append(color_rgb)
#
# print(colors_rgb)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
colors = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

display = Screen()
tim = Turtle()
tim.pu()
tim.goto(-230, -230)
tim.pd()
for h in range(10):
    for i in range(10):
        tim.color(random.choice(colors))
        tim.dot(20)
        tim.pu()
        tim.fd(50)
    tim.left(90)
    tim.fd(50)
    tim.right(90)
    tim.bk(500)

display.exitonclick()


