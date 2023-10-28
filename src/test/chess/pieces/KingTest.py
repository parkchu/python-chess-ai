import unittest
from chess.pieces.King import King
from chess.board.Position import Position

class KingTest(unittest.TestCase):

    def test_make_white_king(self):
        king = King("white")
        
        self.assertEqual(king.image, "k")

    
    def test_get_movable_positions(self):
        king = King("white")
        position = Position.new("e4")

        positions = king.getMovableEndPositions(position)

        self.assertEqual(positions.getToString(), ["d5", "e5", "f5", "f4", 'f3', 'e3', 'd3', 'd4'])


if __name__ == '__main__':
    unittest.main()
