from .Piece import Piece

class Bishop(Piece):
    def __init__(self, team):
        super().__init__(team, "b", 3)
        self.directions=[(-1, 1), (1, 1), (1, -1), (-1, -1)]
