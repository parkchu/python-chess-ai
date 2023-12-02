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
    

    def isCastling(self, distance):
        return False
    

    def getEnemy(self):
        return self.team.getEnemy()


    def getType(self):
        return type(self).__name__
    

class Team(Enum):
    WHITE = "8"
    BLACK = "1"
    NONE = "0"

    def isWhite(self):
        return self == Team.WHITE
    

    def isBlack(self):
        return self == Team.BLACK
    

    def isNone(self):
        return self == Team.NONE
    

    def getEnemy(self):
        if (self.isWhite()):
            return Team.BLACK
        return Team.WHITE


    def getEndRank(self):
        return self.value
    
    
    def get(team):
        if (team == "white"):
            return Team.WHITE
        return Team.BLACK
    

    def getType(self):
        if (self.isWhite()):
            return "white"
        return "black"
