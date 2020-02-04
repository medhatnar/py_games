import pytest
from tic_tac_toe import Board, Letter


def test_letter():
    letter = Letter()
    

@pytest.mark.skip(reason="Letter test first")
def test_board():
    board = Board()
    board_length = len(board)
    
    assert board_length == 3
    for cell in board_length:
        assertEqual(len(cell),3)
