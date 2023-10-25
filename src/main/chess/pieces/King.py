from .Piece import Piece

class King(Piece):
    def __init__(self, team):
        super().__init__(team, "k", distances=[(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)])
