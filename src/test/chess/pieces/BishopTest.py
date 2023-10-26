import unittest
from chess.pieces.Bishop import Bishop
from chess.board.Position import Position

class BishopTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        bishop = Bishop("white")
        position = Position.new("e4")

        positions = bishop.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["a8", 'h7', 'h1', 'b1'])


if __name__ == '__main__':
    unittest.main()
