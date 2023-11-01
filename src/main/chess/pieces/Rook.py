from .Piece import Piece

class Rook(Piece):
    def __init__(self, team):
        super().__init__(team, "r")
        self.directions=[(0, 1), (1, 0), (0, -1), (-1, 0)]
    