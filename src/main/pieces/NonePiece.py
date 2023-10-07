from pieces.Piece import Piece

class NonePiece(Piece):
    def __init__(self):
        super().__init__(None, "*")
        