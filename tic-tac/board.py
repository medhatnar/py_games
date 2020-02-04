import turtle

class Board:

    def __init__(self):
        self.grid = [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9,
        ]
        self.board = turtle.Turtle()
        self.board.color("red")
        self.board.width(5)

        # vertical left line
        self.board.penup()
        self.board.setx(-100)
        self.board.pendown()
        self.board.left(90)
        self.board.forward(200)

        self.board.backward(400)

        # vertical right line
        self.board.penup()
        self.board.setx(100)
        self.board.pendown()
        self.board.forward(400)

        self.board.backward(275)

        # horizontal bottom line
        self.board.penup()
        self.board.left(90)
        self.board.pendown()
        self.board.backward(150)

        self.board.forward(500)

        # travel vertical left
        self.board.penup()
        self.board.backward(150)
        self.board.right(90)
        self.board.forward(150)

        # horizontal top line
        self.board.right(90)
        self.board.pendown()
        self.board.backward(150)
        self.board.forward(500)
        self.board.hideturtle()
    
    def find_column(self,x):
        if x > 100:
           return 'Right'
        elif x > -80:
            return 'Center'
        else:
            return 'Left'
    
    def spot_taken(self,index):
        return isinstance(self.grid[index], str)
    
    def square_index(self, x, y):
        column = self.find_column(x)
        if column == 'Left':
            if (x >= -250 and x <= -100) and y >= 90:
                print('upper left!')
                return 0
            elif (x >= -250 and x <= -100) and (y >= -45 and y <= 60):
                print('mid Left')
                return 3
            elif (x >= -250 and x <= -130) and (y <= -95 and y >= -195):
                print('Bottom left')
                return 6
        elif column == 'Right':
            if (x <= 250 and x >= 100) and y >= 90:
                print('right upper!')
                return 2
            elif (x >= 115 and x <= 250) and (y <= 55 and y >= -65):
                print('right mid')
                return 5
            elif(x >= 150 and x <= 250) and (y >= -195 and y < -130):
                print('right Bottom')
                return 8
        else:
            if(x >= -90 and x <= 90) and y >= 90:
                print('center top')
                return 1
            elif(x >= -85 and x <= 85) and (y >= -50 and y <= 30):
                print('C E N T E R')
                return 4
            elif(x >= -85 and x <= 85) and (y <= -100 and y >= -200):
                print('center Bottom')
                return 7
