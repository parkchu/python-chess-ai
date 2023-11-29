from .Piece import Piece

class King(Piece):
    def __init__(self, team):
        super().__init__(team, "k")
        self.distances=[(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

    
    def getDistances(self):
        distances = self.distances.copy()
        if (self.isFirstMove):
            distances += [(2, 0), (-2, 0)]
        return distances
    

    def isCastling(self, distance):
        return self.isFirstMove and distance in [(2, 0), (-2, 0)]
        