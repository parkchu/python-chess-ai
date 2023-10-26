import unittest
from chess.pieces.Queen import Queen
from chess.board.Position import Position

class QueenTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        queen = Queen("white")
        position = Position.new("e4")

        positions = queen.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["a8", "e8", 'h7', 'h4', 'h1', 'e1', 'b1', 'a4'])


if __name__ == '__main__':
    unittest.main()