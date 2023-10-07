from pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, team):
        super().__init__(team, "q")
