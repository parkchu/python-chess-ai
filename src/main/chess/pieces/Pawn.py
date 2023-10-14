from .Piece import Piece

class Pawn(Piece):
    def __init__(self, team):
        super().__init__(team, "p")
        self.distances = self.setDistances()


    def setDistances(self):
        if (self.isWhite()):
            return [(0, 1), (-1, 1), (1, 1)]
        return [(0, -1), (-1, -1), (1, -1)]


    def getMovablePositions(self, position):
        positions = []
        distances = self.distances.copy()

        if (self.isFirstMove):
            distances.append(self.getFirstMoveDistance())

        for distance in distances:
            movingPosition = chr(ord(position[0]) + distance[0]) + chr(ord(position[1]) + distance[1])
            availablePosition = self.getAvailablePosition(movingPosition)
            (positions.append(availablePosition) if availablePosition is not None else None)

        return positions
        

    def getFirstMoveDistance(self):
        if (self.isWhite()):
            return (0, 2)
        return (0, -2)

    def getAvailablePosition(self, position):
        x = position[0]
        y = position[1]
        if ('a' <= x <= 'h' and '1' <= y <= '8'):
            return position
