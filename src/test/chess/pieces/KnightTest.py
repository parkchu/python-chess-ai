import unittest
from chess.pieces.Knight import Knight
from chess.board.Position import Position

class KnightTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        knight = Knight("white")
        position = Position.new("e4")

        positions = knight.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["d6", "f6", "g5", "g3", 'f2', 'd2', 'c3', 'c5'])


if __name__ == '__main__':
    unittest.main()
