from pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, team):
        super().__init__(team, "r")
