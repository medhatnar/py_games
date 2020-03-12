import turtle
import os

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle() 
        self.ball.speed(0) 
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = 2