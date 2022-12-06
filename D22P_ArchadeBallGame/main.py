from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

display = Screen()
display.setup(1000, 600)
display.bgcolor("#66BFBF")
display.title("PONG")
display.tracer(0)

for y_cor in range(-300, 301, 60):
    segment = Turtle("square")
    segment.shapesize(1.5, 0.025)
    segment.pu()
    segment.speed("fastest")
    segment.color("#EAF6F6")
    segment.goto(0, y_cor)

paddler = Paddle(450, "#FF0063")
paddlel = Paddle(-450, "#FAEA48")
scoreboardr = ScoreBoard(100, "#FF0063")
scoreboardl = ScoreBoard(-100, "#FAEA48")

display.listen()
display.onkey(paddler.up, "Up")
display.onkey(paddler.down, "Down")
display.onkey(paddlel.up, "w")
display.onkey(paddlel.down, "s")

ball = Ball()

on = True
while on:

    display.update()
    time.sleep(ball.time)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddler) < 50 and ball.xcor() > 430 or ball.distance(paddlel) < 50 and ball.xcor() < -430:
        ball.hitback()
        ball.intensefyi()

    if ball.xcor() > 500:
        ball.home()
        ball.hitback()
        scoreboardl.increase_score()
        ball.reset_time()

    if ball.xcor() < -500:
        ball.home()
        ball.hitback()
        scoreboardr.increase_score()
        ball.reset_time()


display.exitonclick()
