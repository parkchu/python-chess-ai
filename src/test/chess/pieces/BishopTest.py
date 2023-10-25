import unittest
from chess.pieces.Bishop import Bishop

class BishopTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        bishop = Bishop("white")
        position = "e4"

        positions = bishop.getMovablePositions(position)

        self.assertEqual(positions, ["a8", 'h7', 'h1', 'b1'])


if __name__ == '__main__':
    unittest.main()
