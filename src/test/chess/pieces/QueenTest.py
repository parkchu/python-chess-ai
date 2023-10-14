import unittest
from chess.pieces.Queen import Queen

class QueenTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        queen = Queen("white")
        position = "e4"

        positions = queen.getMovablePositions(position)

        self.assertEqual(positions, [["d5", "c6", "b7", "a8"], ["e5", "e6", "e7", "e8"], ["f5", 'g6', 'h7'], ['f4', 'g4', 'h4'], ['f3', 'g2', 'h1'], ['e3', 'e2', 'e1'], ['d3', 'c2', 'b1'], ['d4', 'c4', 'b4', 'a4']])


if __name__ == '__main__':
    unittest.main()