from .Piece import Piece

class Knight(Piece):
    def __init__(self, team):
        super().__init__(team, "n")
        self.distances=[(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
