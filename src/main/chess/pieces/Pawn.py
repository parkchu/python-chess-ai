from .Piece import Piece

class Pawn(Piece):

    def __init__(self, team):
        super().__init__(team, "p")
        self.initDistances()


    def initDistances(self):
        self.distances=self.setDistances()
        

    def setDistances(self):
        if (self.isWhite()):
            return [(0, 1), (-1, 1), (1, 1)]
        return [(0, -1), (-1, -1), (1, -1)]


    def getMovablePositions(self, position):
        positions = super().getMovablePositions(position)
        if (self.isFirstMove):
            distance = self.getFirstMoveDistance()
            movablePosition = position.move(distance)
            positions.append(movablePosition)
            
        return positions
        

    def getFirstMoveDistance(self):
        if (self.isWhite()):
            return (0, 2)
        return (0, -2)
