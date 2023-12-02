class Notation:

    def __init__(self, currentPosition, targetPosition, currentPiece, targetPiece):
        self.currentPosition = currentPosition
        self.targetPosition = targetPosition
        self.currentPiece = currentPiece
        self.targetPiece = targetPiece

    
    def isWhite(self):
        return self.currentPiece.isWhite()
    

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
