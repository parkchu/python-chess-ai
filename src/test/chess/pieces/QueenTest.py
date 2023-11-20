import unittest
from chess.pieces.Queen import Queen
from chess.pieces.Piece import Team

class QueenTest(unittest.TestCase):
    
    def test_make_white_queen(self):
        piece = Queen(Team.WHITE)
        
        self.assertEqual(piece.image, "q")


if __name__ == '__main__':
    unittest.main()