import unittest
from chess.pieces.Bishop import Bishop
from chess.pieces.Piece import Team

class BishopTest(unittest.TestCase):
    
    def test_make_white_bishop(self):
        piece = Bishop(Team.WHITE)
        
        self.assertEqual(piece.image, "b")


if __name__ == '__main__':
    unittest.main()
