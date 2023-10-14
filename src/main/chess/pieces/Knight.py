from .Piece import Piece

class Knight(Piece):
    def __init__(self, team):
        super().__init__(team, "n")
        self.distances = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]


    def getMovablePositions(self, position):
        positions = []
        distances = self.distances.copy()

        for distance in distances:
            movingPosition = chr(ord(position[0]) + distance[0]) + chr(ord(position[1]) + distance[1])
            availablePosition = self.getAvailablePosition(movingPosition)
            (positions.append([availablePosition]) if availablePosition is not None else None)

        return positions


    def getAvailablePosition(self, position):
        x = position[0]
        y = position[1]
        if ('a' <= x <= 'h' and '1' <= y <= '8'):
            return position
