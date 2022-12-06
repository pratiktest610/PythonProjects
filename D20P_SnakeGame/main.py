import tkinter
import random
from turtle import Screen
import time
from snake import Snake
from food import Food
from scorboard import ScoreBoard

colors = ["#293462", "#1CD6CE", "#D61C4E",  "#D61C4E", "#224B0C"]


def change_screen_color():
    display.bgcolor(random.choice(colors))
# setting up screen

display = Screen()
display.setup(600, 600)
display.bgcolor("#7DCE13")
display.title("Snake Game")
display.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
scoreboard.print_score()

display.listen()
display.onkey(snake.turn_right, "Right")
display.onkey(snake.turn_left, "Left")
display.onkey(snake.up, "Up")
display.onkey(snake.down, "Down")

game_on = True
while game_on:
    snake.move()
    display.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        display.tracer(0)
        snake.create(1)
        scoreboard.increase_score()
        change_screen_color()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.gameover()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.gameover()
            snake.reset()



display.exitonclick()
