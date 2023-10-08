import unittest
import sys
sys.path.append("./src/main/chess/chess")
from pieces.King import King

class PieceTest(unittest.TestCase):

    def test_make_white_king(self):
        king = King("white")
        self.assertEqual(king.image, "K")


if __name__ == '__main__':
    unittest.main()
