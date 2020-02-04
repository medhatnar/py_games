import turtle
import os

wn = turtle.Screen()
wn.title("Pong by @narshah1n")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score 
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() 
paddle_a.speed(0) 
paddle_a.shape("square")
paddle_a.color("white")
# by default this paddle is 20x20 px len 1 means keep default
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# by default turtles draw lines as they move. we don't need that here. hence penup.
paddle_a.penup()
# below are the coordinates we want paddle A to start at.
paddle_a.goto(-350, 0)

    
# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "bold"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    if (y + 20) >= 260:
        y = paddle_a.ycor()
    else:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if (y - 20) <= -260:
        y = paddle_a.ycor()
    else:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if (y + 20) >= 260:
        y = paddle_b.ycor()
    else:
        y += 20

    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()

    y -= 20
    paddle_b.sety(y)

# Keyboard binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#  Main game loop

while True:
    wn.update()

# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay error.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay error.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        score_a += 1
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
        os.system("afplay error.wav&")

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        score_b += 1
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
        os.system("afplay error.wav&")

# Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay high-beep.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay low-beep.wav&")
