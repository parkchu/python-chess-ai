from pieces.Piece import Piece

class King(Piece):
    def __init__(self, team):
        super().__init__(team, "k")
