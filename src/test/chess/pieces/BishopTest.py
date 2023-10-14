import unittest
from chess.pieces.Bishop import Bishop

class BishopTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        bishop = Bishop("white")
        position = "e4"

        positions = bishop.getMovablePositions(position)

        self.assertEqual(positions, [["d5", "c6", "b7", "a8"], ["f5", 'g6', 'h7'], ['f3', 'g2', 'h1'], ['d3', 'c2', 'b1']])


if __name__ == '__main__':
    unittest.main()
