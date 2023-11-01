import unittest
from chess.pieces.Pawn import Pawn

class PieceTest(unittest.TestCase):

    def test_make_white_piece(self):
        piece = Pawn("white")
        
        self.assertEqual(piece.team, "white")
        self.assertEqual(piece.image, "p")


    def test_make_black_piece(self):
        piece = Pawn("black")
        
        self.assertEqual(piece.team, "black")
        self.assertEqual(piece.image, "P")


if __name__ == '__main__':
    unittest.main()
