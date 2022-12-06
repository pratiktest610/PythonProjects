from turtle import Turtle, Screen
from car_manager import CarManager
from level_manager import LevelManager
from hero import Hero
import time

display = Screen()
display.bgcolor("Grey")
display.setup(600, 600)
display.title("Turtle Crossing")
display.tracer(0)

hero = Hero()
level_manager = LevelManager()
car_manager = CarManager()

display.listen()
display.onkey(hero.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(level_manager.time)
    display.update()
    car_manager.move_cars()

    for car in car_manager.cars:
        if hero.distance(car) < 17:
            level_manager.game_over()
            game_is_on = False

    if hero.ycor() > 260:
        hero.goto(0, -280)
        level_manager.level_up()


display.exitonclick()
