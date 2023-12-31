from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import MoveRequestSerializer
from .serializers import PromoteRequestSerializer
from .serializers import UndoRequestSerializer
from rest_framework.parsers import JSONParser
from home.views import board
from home.views import ai
from chess.board.Position import Position
from chess.screen.Screen import Screen
from chess.pieces.Piece import Team
from chess.pieces.Queen import Queen
from chess.pieces.Bishop import Bishop
from chess.pieces.Knight import Knight
from chess.pieces.Rook import Rook

@api_view(['POST'])
def movePiece(request):
    data = JSONParser().parse(request)
    serializer = MoveRequestSerializer(data=data)
    if serializer.is_valid():
        currentPosition = Position.new(serializer.data["currentPosition"])
        targetPosition = Position.new(serializer.data["targetPosition"])
        isCastling = board.isCastling(currentPosition, targetPosition)
        board.move(currentPosition, targetPosition)
        Screen.showBoard(board)
        response = makeResponse(currentPosition, targetPosition, isCastling)
        return JsonResponse(response, status=200)
    return JsonResponse(serializer.errors, status=400)


def makeResponse(currentPosition, targetPosition, isCastling):
    response = {
        "currentPosition": currentPosition.get(),
        "targetPosition": targetPosition.get(),
        "isPromotion": board.isPromotion(targetPosition),
        "isCastling": isCastling
    }
    return response


@api_view(['GET'])
def getMovablePositions(request, position):
    positions = board.getMovablePositions(Position.new(position))
    response = {
        "positions": positions.getToString()
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def promote(request):
    data = JSONParser().parse(request)
    serializer = PromoteRequestSerializer(data=data)
    if serializer.is_valid():
        position = Position.new(serializer.data["position"])
        pieceType = eval(serializer.data["pieceType"])
        board.promote(position, pieceType)
        Screen.showBoard(board)
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def isCheck(request, team):
    team = Team.get(team)
    response = {
        "isCheck": board.isCheck(team),
        "isCheckmate": board.isCheckmate(team),
        "kingPosition": board.kingPosition[team].get()
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def undo(request):
    data = JSONParser().parse(request)
    serializer = UndoRequestSerializer(data=data)
    if serializer.is_valid():
        team = Team.get(serializer.data["team"])
        notations = board.undo(team)
        notations = list(map(lambda notation:notation.toDict(), notations))
        response = {
            "notations": notations,
            "team": team.getType()
        }
        Screen.showBoard(board)
        return JsonResponse(response, status=200)
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def moveAi(request, team):
    team = Team.get(team)
    notation = ai.getMovePosition(board, team)
    response = notation.toDict()
    return JsonResponse(response, status=200)
