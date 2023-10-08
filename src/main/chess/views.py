from django.shortcuts import render
from .chess.pieces.Pawn import Pawn

def index(request):
    print(Pawn)
    return render(request, 'index.html')
