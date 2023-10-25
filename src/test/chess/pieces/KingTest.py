import unittest
from chess.pieces.King import King

class KingTest(unittest.TestCase):

    def test_make_white_king(self):
        king = King("white")
        
        self.assertEqual(king.image, "k")

    
    def test_get_movable_positions(self):
        king = King("white")
        position = "e4"

        positions = king.getMovablePositions(position)

        self.assertEqual(positions, ["d5", "e5", "f5", "f4", 'f3', 'e3', 'd3', 'd4'])


if __name__ == '__main__':
    unittest.main()
