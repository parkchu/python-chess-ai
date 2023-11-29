import unittest
from chess.pieces.Knight import Knight
from chess.pieces.Piece import Team

class KnightTest(unittest.TestCase):
    
    def test_make_white_knight(self):
        piece = Knight(Team.WHITE)
        
        self.assertEqual(piece.image, "n")


if __name__ == '__main__':
    unittest.main()
