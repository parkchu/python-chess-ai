import unittest
from chess.pieces.King import King

class KingTest(unittest.TestCase):

    def test_make_white_king(self):
        piece = King("white")
        
        self.assertEqual(piece.image, "k")


if __name__ == '__main__':
    unittest.main()
