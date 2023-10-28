import unittest
from chess.pieces.Pawn import Pawn
from chess.board.Position import Position

class PawnTest(unittest.TestCase):

    def test_make_white_pawn(self):
        pawn = Pawn("white")
        
        self.assertEqual(pawn.image, "p")


    def test_get_movable_positions(self):
        pawn = Pawn("white")
        position = Position.new("b2")

        positions = pawn.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["b3", "a3", "c3", "b4"])


    def test_get_out_of_range_position(self):
        pawn = Pawn("white")
        position = Position.new("a2")

        positions = pawn.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["a3", "b3", "a4"])

    
    def test_get_movable_positions_black(self):
        pawn = Pawn("black")
        position = Position.new("b7")

        positions = pawn.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["b6", "a6", "c6", "b5"])


    def test_already_move(self):
        pawn = Pawn("white")
        pawn.move()
        position = Position.new("b3")

        positions = pawn.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["b4", "a4", "c4"])


if __name__ == '__main__':
    unittest.main()
