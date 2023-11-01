import unittest
from chess.pieces.Knight import Knight

class KnightTest(unittest.TestCase):
    
    def test_make_white_knight(self):
        piece = Knight("white")
        
        self.assertEqual(piece.image, "n")


if __name__ == '__main__':
    unittest.main()
