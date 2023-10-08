import unittest
import sys
sys.path.append("./src/main/chess")
from pieces.Pawn import Pawn

class PawnTest(unittest.TestCase):

    def test_make_white_pawn(self):
        pawn = Pawn("white")
        
        self.assertEqual(pawn.image, "p")


if __name__ == '__main__':
    unittest.main()
