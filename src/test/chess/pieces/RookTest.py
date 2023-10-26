import unittest
from chess.pieces.Rook import Rook
from chess.board.Position import Position

class RookTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        rook = Rook("white")
        position = Position.new("e4")

        positions = rook.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["e8", 'h4', 'e1', 'a4'])


if __name__ == '__main__':
    unittest.main()
