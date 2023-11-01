import unittest
from chess.pieces.Bishop import Bishop

class BishopTest(unittest.TestCase):
    
    def test_make_white_bishop(self):
        piece = Bishop("white")
        
        self.assertEqual(piece.image, "b")


if __name__ == '__main__':
    unittest.main()
