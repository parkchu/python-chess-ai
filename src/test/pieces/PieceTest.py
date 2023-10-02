import unittest
import sys
print(sys.path)
from pieces.Pawn import Pawn

class PieceTest(unittest.TestCase):

    def test_make_piece(self):
        pawn = Pawn("white")
        self.assertEqual(pawn.team, "white")


if __name__ == '__main__':
    unittest.main()
