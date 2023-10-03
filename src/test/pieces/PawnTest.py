import unittest
import sys
sys.path.append("./src/main")
from pieces.Pawn import Pawn

class PieceTest(unittest.TestCase):

    def test_make_white_pawn(self):
        pawn = Pawn("white")
        self.assertEqual(pawn.image, "P")


if __name__ == '__main__':
    unittest.main()
