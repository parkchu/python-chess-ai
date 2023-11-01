import unittest
from chess.pieces.Rook import Rook

class RookTest(unittest.TestCase):
    
    def test_make_white_rook(self):
        piece = Rook("white")
        
        self.assertEqual(piece.image, "r")


if __name__ == '__main__':
    unittest.main()
