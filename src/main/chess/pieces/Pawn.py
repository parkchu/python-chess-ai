from .Piece import Piece

class Pawn(Piece):
    def __init__(self, team):
        super().__init__(team, "p")
        self.distances = [(0, 1), (0, 2), (-1, 1), (1, 1)]

    def getMovablePositions(self, position):
        if (super().isWhite()):
            return self.test2(position)
        return []
    
    def test2(self, position):
        positions = []
        for distance in self.distances:
            movingPosition = chr(ord(position[0]) + distance[0]) + chr(ord(position[1]) + distance[1])
            availablePosition = self.getAvailablePosition(movingPosition)
            (positions.append(availablePosition) if availablePosition is not None else None)
        return positions
    
    def getAvailablePosition(self, position):
        x = position[0]
        y = position[1]
        if ('a' <= x <= 'h' and '1' <= y <= '8'):
            return position
