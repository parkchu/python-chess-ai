import unittest
from chess.pieces.Pawn import Pawn
from chess.pieces.Piece import Team

class PieceTest(unittest.TestCase):

    def test_make_white_piece(self):
        piece = Pawn(Team.WHITE)
        
        self.assertEqual(piece.team, Team.WHITE)
        self.assertEqual(piece.image, "p")


    def test_make_black_piece(self):
        piece = Pawn(Team.BLACK)
        
        self.assertEqual(piece.team, Team.BLACK)
        self.assertEqual(piece.image, "P")


if __name__ == '__main__':
    unittest.main()
