from .Piece import Piece

class Knight(Piece):
    def __init__(self, team):
        super().__init__(team, "n")
