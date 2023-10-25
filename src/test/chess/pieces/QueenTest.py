import unittest
from chess.pieces.Queen import Queen

class QueenTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        queen = Queen("white")
        position = "e4"

        positions = queen.getMovablePositions(position)

        self.assertEqual(positions, ["a8", "e8", 'h7', 'h4', 'h1', 'e1', 'b1', 'a4'])


if __name__ == '__main__':
    unittest.main()