from pieces.Piece import Piece

class NonePiece(Piece):
    def __init__(self):
        super().__init__(None)
        self.image = self.setImage()

    def setImage(self):
        return "*"