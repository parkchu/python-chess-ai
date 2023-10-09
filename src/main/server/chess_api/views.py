from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import PositionsSerializer
from rest_framework.parsers import JSONParser
from chess.board.Board import Board
from chess.screen.Screen import Screen

board = Board()

def index(request):
    board.initBoard()
    return render(request, 'index.html')

@api_view(['POST'])
def movePiece(request):
    data = JSONParser().parse(request)
    serializer = PositionsSerializer(data=data)
    if serializer.is_valid():
        currentPosition = Screen.checkPosition(serializer.data["currentPosition"])
        targetPosition = Screen.checkPosition(serializer.data["targetPosition"])
        board.move(currentPosition, targetPosition)
        Screen.showBoard(board)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
