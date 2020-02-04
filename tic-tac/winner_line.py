from turtle import *

class Winner_Line:
    def __init__(self, x, y):
        self.line = Turtle()
        self.line.hideturtle()
        self.line.goto(x,y)