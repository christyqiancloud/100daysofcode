from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def f():
    tim.forward(10)

def b():
    tim.backward(10)

def tl():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def tr():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def c():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(f, "Up")
screen.onkey(b, "Down")
screen.onkey(tl, "Left")
screen.onkey(tr, "Right")
screen.onkey(c, "c")

screen.exitonclick()
