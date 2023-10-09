import unittest
from chess.pieces.King import King

class KingTest(unittest.TestCase):

    def test_make_white_king(self):
        king = King("white")
        
        self.assertEqual(king.image, "k")


if __name__ == '__main__':
    unittest.main()
