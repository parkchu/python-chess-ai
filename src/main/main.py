from pieces.Pawn import Pawn
from board.board import Board

def run():
    pawn = Pawn("white")
    print(pawn.isWhite())
    print(pawn.team)
def run_board():
    board = Board()
    print(board.gameboard)
run_board()



            


