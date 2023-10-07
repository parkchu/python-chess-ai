from pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, team):
        super().__init__(team, "p")
