from pieces.Pawn import Pawn
from board.board import Board

def run():
    board = Board()
    showBoard(board.getBoard())

def showBoard(board):
    for pieces in board:
        print(" ".join(pieces))

run()



            


