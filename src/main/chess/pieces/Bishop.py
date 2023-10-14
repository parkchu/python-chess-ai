from .Piece import Piece

class Bishop(Piece):
    def __init__(self, team):
        super().__init__(team, "b")
        self.directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]


    def getMovablePositions(self, position):
        positions = []

        for direction in self.directions:
            positions2 = []
            nextPosition = self.moveDirection(position, direction)
            while (self.checkAvailablePosition(nextPosition)):
                positions2.append(nextPosition)
                nextPosition = self.moveDirection(nextPosition, direction)
            positions.append(positions2)

        return positions


    def checkAvailablePosition(self, position):
        x = position[0]
        y = position[1]
        return 'a' <= x <= 'h' and '1' <= y <= '8'


    def moveDirection(self, position, direction):
        x = chr(ord(position[0]) + direction[0])
        y = chr(ord(position[1]) + direction[1])
        return x + y
