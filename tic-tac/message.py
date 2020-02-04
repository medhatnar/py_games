import turtle

class Message:
    def __init__(self, new_message, color, size):
        self.message = new_message
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed('fastest')
        self.pen.color(color)
        self.pen.penup()
        self.pen.goto(0, 260)
        self.pen.write(f"{self.message}", align="center",
                       font=("Courier", size, "bold"))

    def clear(self):
        self.pen.clear()