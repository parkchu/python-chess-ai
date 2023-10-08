import unittest
import sys
sys.path.append("./src/main/chess")
from pieces.Pawn import Pawn

class PieceTest(unittest.TestCase):

    def test_make_white_piece(self):
        pawn = Pawn("white")
        
        self.assertEqual(pawn.team, "white")


if __name__ == '__main__':
    unittest.main()
