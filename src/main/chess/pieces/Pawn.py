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
    

    def getDistances(self):
        distances = self.distances.copy()
        if (self.isFirstMove):
            distances.append(self.getFirstMoveDistance())
        return distances
        

    def getFirstMoveDistance(self):
        if (self.isWhite()):
            return (0, 2)
        return (0, -2)


    def containsDistance(self, distance):
        return distance in self.distances[1:]
