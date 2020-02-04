from turtle import *

my_turtle = Turtle()

while True:
    my_turtle.speed('slowest')
    my_turtle.color('green')
    # my_turtle.shape("triangle")
    my_turtle.width(5)
    my_turtle.goto(100,100)
    my_turtle.forward(100)
    my_turtle.penup()
    my_turtle.goto(50,50)
    my_turtle.stamp()
    my_turtle.pendown()
    my_turtle.backward(300)
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(360)
    my_turtle.pendown()
    my_turtle.circle(10, 18)
    my_turtle.pendown()

    