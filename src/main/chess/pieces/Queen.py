from .Piece import Piece

class Queen(Piece):
    def __init__(self, team):
        super().__init__(team, "q")
        self.directions=[(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
