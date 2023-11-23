from enum import Enum

class Piece:

    def __init__(self, team, image):
        self.team = team
        self.image = self.setImage(image)
        self.distances = []
        self.directions = []
        self.isFirstMove = True


    def setImage(self, image):
        if (self.isBlack()):
            return image.upper()
        return image
    

    def isWhite(self):
        return self.team.isWhite()
    

    def isBlack(self):
        return self.team.isBlack()
    
    
    def isNone(self):
        return self.team.isNone()
    

    def isEnemy(self, piece):
        if (self.isNone() or piece.isNone()):
            return False
        return self.team != piece.team
    

    def isIt(self, pieceType):
        return type(self) is pieceType
    
    
    def move(self):
        self.isFirstMove = False

    
    def getDistances(self):
        return self.distances
    

    def getDirections(self):
        return self.directions
    

    def containsDistance(self, distance):
        return distance in self.distances
    

    def containsDirection(self, direction):
        return direction in self.directions
    

class Team(Enum):
    WHITE = "white"
    BLACK = "black"
    NONE = "none"

    def isWhite(self):
        return self.value == "white"
    

    def isBlack(self):
        return self.value == "black"
    

    def isNone(self):
        return self.value == "none"
    
    def getEnemy(self):
        if (self.isWhite()):
            return Team.BLACK
        return Team.WHITE
