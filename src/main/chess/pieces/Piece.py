class Piece:
    def __init__(self, team, image):
        self.team = team
        self.image = self.setImage(image)
        self.isFirstMove = True


    def isWhite(self):
        return self.team == "white"
    

    def isBlack(self):
        return self.team == "black"
    
    
    def isNone(self):
        return self.team == None
    

    def isEnemy(self, piece):
        if (self.isNone() or piece.isNone()):
            return False
        return self.team != piece.team
    

    def isIt(self, pieceType):
        return type(self) is pieceType
    

    def setImage(self, image):
        if (self.isBlack()):
            return image.upper()
        return image
    

    def getMovablePositions(self, position):
        return []
    
    
    def move(self):
        self.isFirstMove = False
