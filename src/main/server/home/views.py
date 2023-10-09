from django.shortcuts import render
from chess.board.Board import Board

board = Board()

def index(request):
    board.initBoard()
    return render(request, 'index.html')
