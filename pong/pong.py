import turtle
import os
from datetime import datetime
import time
import math

from ball import Ball

wn = turtle.Screen()
wn.title("Pong by @narshah1n")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score 
score_a = 0
score_b = 0

ball = Ball().ball

# Paddle A
paddle_a = turtle.Turtle() 
paddle_a.speed(0) 
paddle_a.shape("square")
paddle_a.color("#1a50bc")
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
paddle_b.color("#1a50bc")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "bold"))

paddle_speed = 8
keys_down = {}

# Keyboard binding 
wn.listen()
def set_key_down(key):
    def result():
        keys_down[key] = 2
    return result
def set_key_up(key):
    def result():
        del keys_down[key]
    return result
wn.onkeypress(set_key_down('w'), "w")
wn.onkeyrelease(set_key_up('w'), "w")
wn.onkeypress(set_key_down('s'), "s")
wn.onkeyrelease(set_key_up('s'), "s")
wn.onkeypress(set_key_down('Up'), "Up")
wn.onkeyrelease(set_key_up('Up'), "Up")
wn.onkeypress(set_key_down('Down'), "Down")
wn.onkeyrelease(set_key_up('Down'), "Down")

def min_max_corners(box):
    center_x = box.xcor()
    center_y = box.ycor()
    shape = box.shapesize()
    return (center_x - shape[1] * 10,
            center_x + shape[1] * 10,
            center_y - shape[0] * 10,
            center_y + shape[0] * 10)

def collides(box_a, box_b):
    min_a_x, max_a_x, min_a_y, max_a_y = min_max_corners(box_a)
    min_b_x, max_b_x, min_b_y, max_b_y = min_max_corners(box_b)
    return min_a_x <= max_b_x and\
           min_a_y <= max_b_y and\
           max_a_x >= min_b_x and\
           max_a_y >= min_b_y

def vec_length(vec):
    return math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])
def vec_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])
def vec_divide(a, b):
    return (a[0] / b, a[1] / b)
def vec_mul(a, b):
    return (a[0] * b, a[1] * b)

def collision_with_dir(pos_a, pos_b, old_dir):
    #print(pos_a)
    #print(pos_b)
    direction = vec_sub(pos_a, pos_b)
    direction = (direction[0], direction[1] / 2)
    #print(direction)
    if direction[0] == 0 and direction[1] == 0:
        direction[0] = old_dir[0]
    old_length = vec_length(old_dir)
    dir_normalized = vec_divide(direction, vec_length(direction))
    return vec_mul(dir_normalized, old_length * 1.25)

pressed_times = {}

#  Main game loop
start_of_frame = datetime.now()
while True:
    wn.update()

    keys_and_paddles = [('w', paddle_a, paddle_speed),
                        ('s', paddle_a, -paddle_speed),
                        ('Up', paddle_b, paddle_speed),
                        ('Down', paddle_b, -paddle_speed)]
    for key, paddle, speed in keys_and_paddles:
        if key in keys_down:
            pressed_times[key] = 2
        if key in pressed_times:
            paddle.sety(max(-260, min(260, paddle.ycor() + speed)))
            pressed_times[key] -= 1
            if pressed_times[key] == 0:
                del pressed_times[key]

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
        ball.dx = 2
        ball.dy = -2
        pen.clear()
        score_a += 1
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
        os.system("afplay error.wav&")

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = -2
        ball.dy = -2
        pen.clear()
        score_b += 1
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
        os.system("afplay error.wav&")

# Paddle and ball collisions
    #if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
    if ball.dx > 0 and collides(ball, paddle_b):
        #ball.setx(340)
        collision_dir = collision_with_dir((ball.xcor(), ball.ycor()), (paddle_b.xcor(), paddle_b.ycor()), (ball.dx, ball.dy))
        ball.dx = min(-2, collision_dir[0])
        ball.dy = collision_dir[1]

        os.system("afplay high-beep.wav&")

    #if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
    if ball.dx < 0 and collides(ball, paddle_a):
        #ball.setx(-340)
        collision_dir = collision_with_dir((ball.xcor(), ball.ycor()), (paddle_a.xcor(), paddle_a.ycor()), (ball.dx, ball.dy))
        ball.dx = max(2, collision_dir[0])
        ball.dy = collision_dir[1]
        os.system("afplay low-beep.wav&")

    end_of_frame = datetime.now()
    time_passed = end_of_frame - start_of_frame
    while time_passed.total_seconds() < 1.0 / 60.0:
        time.sleep(0.001)
        end_of_frame = datetime.now()
        time_passed = end_of_frame - start_of_frame
    start_of_frame = end_of_frame
