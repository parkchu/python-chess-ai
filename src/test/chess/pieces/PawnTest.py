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

        self.assertEqual(positions, ["b3", "a3", "c3", "b4"])


    def test_get_out_of_range_position(self):
        pawn = Pawn("white")
        position = "a2"

        positions = pawn.getMovablePositions(position)

        self.assertEqual(positions, ["a3", "b3", "a4"])

    
    def test_get_movable_positions_black(self):
        pawn = Pawn("black")
        position = "b7"

        positions = pawn.getMovablePositions(position)

        self.assertEqual(positions, ["b6", "a6", "c6", "b5"])


    def test_already_move(self):
        pawn = Pawn("white")
        pawn.move()
        position = "b3"

        positions = pawn.getMovablePositions(position)

        self.assertEqual(positions, ["b4", "a4", "c4"])


if __name__ == '__main__':
    unittest.main()
