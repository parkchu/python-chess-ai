from .Piece import Piece
from .Piece import Team

class NonePiece(Piece):
    def __init__(self):
        super().__init__(Team.NONE, "*")
        