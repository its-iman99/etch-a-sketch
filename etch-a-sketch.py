from turtle import Turtle, Screen

timmy = Turtle()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def clockwise():
    timmy.right(10)


def anticlockwise():
    timmy.left(10)


def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
