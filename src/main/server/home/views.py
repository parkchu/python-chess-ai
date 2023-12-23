from django.shortcuts import render
from chess.board.Board import Board
from chess.ai.Ai import Ai

board = Board()
ai = Ai()

def index(request):
    board.initBoard()
    board.setPieces()
    return render(request, 'index.html')
