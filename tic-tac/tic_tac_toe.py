import turtle
from message import Message
from board import Board
from x_or_o import X_or_O
# from winner_line import Winner_line

game_on = True


class Game:
    def __init__(self):
        self.current_player = "X"
        self.moves_made = 0
        self.message = Message("Turtle Tic-Tac-Toe", 'white', 32)

        self.wn = turtle.Screen()
        self.wn.title("Tic_Tac_Toe by @narshah1n")
        self.wn.bgcolor("pink")
        self.wn.setup(width=800, height=700)

        self.board = Board()

        self.wn.listen()
        self.wn.onclick(self.move_player)

    def move_player(self, x, y):
        self.message.clear()
        if self.in_bounds(x, y):
            letter = X_or_O(x, y, self.current_player)
            self.update_game(x, y, letter)
        else:
            self.message.clear()
            self.message = Message(
                'Please select a square within the grid.', "red", 24)

        if self.moves_made > 8:
            self.message.clear()
            self.message = Message(f"It is a Draw!", "red", 32)
            self.wn.exitonclick()
        else:
            is_winner = self.check_winner(self.board.grid)
            if is_winner:
                self.message.clear()
                self.message = Message(
                    f"Player {is_winner} is the winner!", "white", 32)
                # attach coordinates to each letter in grid array
                # when winner is found, return the three matches made
                # pull them from grid array to get coordinates.
                # use that to draw line
                self.wn.exitonclick()

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def in_bounds(self, x, y):
        return (x < 250 and x > -250) and (y < 200 and y > -200)

    def update_game(self, x, y, letter):
        spot = self.board.square_index(x, y)

        if self.board.spot_taken(spot):
            self.message.clear()
            self.message = Message(
                'That spot is taken. Pick another!', "red", 24)
            letter.clear()
        else:
            self.board.grid[spot] = self.current_player
            self.moves_made += 1
            self.change_player()

    def check_winner(self, grid):
        # diagonal check
        if grid[0] == grid[4] and grid[0] == grid[8]:
            return grid[0]
        elif grid[2] == grid[4] and grid[2] == grid[6]:
            return grid[2]
        # horizontal check
        for square in range(0, len(grid), 3):
            if grid[square] == grid[square+1] and grid[square] == grid[square+2]:
                return grid[square]
        # vertical check
        for square in range(3):
            if grid[square] == grid[square+3] and grid[square] == grid[square+6]:
                return grid[square]
        return False


game = Game()

while game_on:
    game.wn.update()
