import unittest
from chess.pieces.Rook import Rook

class RookTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        rook = Rook("white")
        position = "e4"

        positions = rook.getMovablePositions(position)

        self.assertEqual(positions, ["e8", 'h4', 'e1', 'a4'])


if __name__ == '__main__':
    unittest.main()
