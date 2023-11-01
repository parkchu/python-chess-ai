from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import MoveRequestSerializer
from rest_framework.parsers import JSONParser
from home.views import board
from chess.board.Position import Position
from chess.screen.Screen import Screen

@api_view(['POST'])
def movePiece(request):
    data = JSONParser().parse(request)
    serializer = MoveRequestSerializer(data=data)
    if serializer.is_valid():
        currentPosition = Position.new(serializer.data["currentPosition"])
        targetPosition = Position.new(serializer.data["targetPosition"])
        board.move(currentPosition, targetPosition)
        Screen.showBoard(board)
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def getMovablePositions(request, position):
    positions = board.getMovablePositions(Position.new(position))
    return JsonResponse(positions.getToString(), safe=False, status=200)
