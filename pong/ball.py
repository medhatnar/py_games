import turtle
import os

class Ball:
    def __init__(self):
        ball = turtle.Turtle() 
        ball.speed(0) 
        ball.shape("square")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 2
        ball.dy = 2