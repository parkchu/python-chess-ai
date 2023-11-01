import unittest
from chess.pieces.Queen import Queen

class QueenTest(unittest.TestCase):
    
    def test_make_white_queen(self):
        piece = Queen("white")
        
        self.assertEqual(piece.image, "q")


if __name__ == '__main__':
    unittest.main()