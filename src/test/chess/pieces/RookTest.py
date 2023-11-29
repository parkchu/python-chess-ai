import unittest
from chess.pieces.Rook import Rook
from chess.pieces.Piece import Team

class RookTest(unittest.TestCase):
    
    def test_make_white_rook(self):
        piece = Rook(Team.WHITE)
        
        self.assertEqual(piece.image, "r")


if __name__ == '__main__':
    unittest.main()
