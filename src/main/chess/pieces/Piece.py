from chess.board.Positions import Positions

class Piece:

    def __init__(self, team, image, distances=[], directions=[]):
        self.team = team
        self.image = self.setImage(image)
        self.distances = distances
        self.directions = directions
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
        positions = Positions.empty()
        print(positions.getToString())
        for distance in self.distances:
            movablePosition = position.move(distance)
            positions.append(movablePosition)

        return positions
    

    def getMovableEndPositions(self, position):
        positions = Positions.empty()

        for direction in self.directions:
            nextPosition = position
            while (nextPosition.move(direction).isAvailable()):
                nextPosition = nextPosition.move(direction)
            positions.append(nextPosition)

        return positions
    
    
    def move(self):
        self.isFirstMove = False
