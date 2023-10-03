from pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, team):
        super().__init__(team)
        self.image = self.setImage()

    def setImage(self):
        if (self.isWhite):
            return "Q"
        return "q"
