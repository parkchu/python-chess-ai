import unittest
from chess.pieces.Pawn import Pawn

class PawnTest(unittest.TestCase):

    def test_make_white_pawn(self):
        pawn = Pawn("white")
        
        self.assertEqual(pawn.image, "p")

    def test_get_movable_positions(self):
        pawn = Pawn("white")
        position = "b2"

        positions = pawn.getMovablePositions(position)

        self.assertEqual(positions, ["b3", "b4", "a3", "c3"])

    def test_get_out_of_range_position(self):
        pawn = Pawn("white")
        position = "a2"

        positions = pawn.getMovablePositions(position)

        self.assertEqual(positions, ["a3", "a4", "b3"])


if __name__ == '__main__':
    unittest.main()
