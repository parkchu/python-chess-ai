from django.shortcuts import render
from chess.board.Board import Board

board = Board()

def index(request):
    board.initBoard()
    board.setPieces()
    return render(request, 'index.html')
