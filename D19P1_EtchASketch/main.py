from turtle import Turtle, Screen

tim = Turtle()
display = Screen()


def move_fd():
    tim.fd(10)


def move_bk():
    tim.bk(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def clear():
    tim.home()
    tim.clear()


display.listen()
display.onkey(move_fd, "w")
display.onkey(move_bk, "s")
display.onkey(move_right, "d")
display.onkey(move_left, "a")
display.onkey(clear, "c")


display.exitonclick()
