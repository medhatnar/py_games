import turtle

class X_or_O:
    def __init__(self, x, y, player):
        self.letter = turtle.Turtle()
        self.letter.hideturtle()
        self.letter.speed('fast')
        self.letter.width(5)
        self.letter.color("white")
        self.letter.penup()

        if player == 'O':
            self.letter.goto(x, y-20)
            self.letter.pendown()
            self.letter.circle(50)
        else:
            self.letter.goto(x, y)
            self.letter.pendown()
            self.draw_x(self.letter)

    def draw_x(self, t):
        half_length = 100 / 2
        hypotenuse = (2 * half_length**2)**0.5
        t.hideturtle()

        t.pendown()
        t.right(45)
        t.forward(half_length)
        t.left(135)

        t.penup()
        t.forward(hypotenuse)
        t.pendown()

        t.left(135)
        t.forward(100)
        t.right(135)

        t.penup()
        t.forward(hypotenuse)
        t.pendown()

        t.right(135)
        t.forward(half_length)
        t.left(45)
        t.penup()

    def clear(self):
        self.letter.clear()