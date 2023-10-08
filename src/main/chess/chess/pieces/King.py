from .Piece import Piece

class King(Piece):
    def __init__(self, team):
        super().__init__(team)
        self.image = self.setImage()

    def setImage(self):
        if (self.isWhite):
            return "K"
        return "k"
