from turtle import Turtle, Screen

screen = Screen()
kish = Turtle()


def move_forward():
    kish.forward(20)

def move_backward():
    kish.backward(20)

def right():
    kish.setheading(kish.heading() + 10)

def left():
    kish.setheading(kish.heading() - 10)
    
def clear():
    kish.clear()
    kish.penup()
    kish.home()
    kish.pendown()

screen.listen()
screen.onkey(move_forward, "space")
screen.onkey(move_backward, "v")
screen.onkey(right, "h")
screen.onkey(left, "d")
screen.onkey(clear, "c")

screen.exitonclick()
