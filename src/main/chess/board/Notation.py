from chess.pieces.NonePiece import NonePiece
from chess.pieces.Rook import Rook

class Notation:

    def __init__(self, currentPosition, targetPosition, currentPiece, targetPiece):
        self.currentPosition = currentPosition
        self.targetPosition = targetPosition
        self.currentPiece = currentPiece
        self.targetPiece = targetPiece

    
    def isWhite(self):
        return self.currentPiece.isWhite()
    

    def isCastling(self):
        distance = self.currentPosition.getDistance(self.targetPosition)
        return self.currentPiece.isCastling(distance)


    def getCastlingNotation(self):
        rookPosition = self.targetPosition.getCastlingRookPosition()
        position = self.targetPosition.move(rookPosition.getDirection(self.targetPosition))
        return Notation(rookPosition, position, Rook(self.currentPiece.team), NonePiece())


    def toDict(self):
        return {
            "currentPosition": self.currentPosition.get(),
            "targetPosition": self.targetPosition.get(),
            "currentPiece": {
                "pieceType": self.currentPiece.getType(),
                "team": self.currentPiece.team.getType()
            },
            "targetPiece": {
                "pieceType": self.targetPiece.getType(),
                "team": self.targetPiece.team.getType()
            }
        }
