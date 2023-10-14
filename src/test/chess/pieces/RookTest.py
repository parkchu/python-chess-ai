import unittest
from chess.pieces.Rook import Rook

class RookTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        rook = Rook("white")
        position = "e4"

        positions = rook.getMovablePositions(position)

        self.assertEqual(positions, [["e5", "e6", "e7", "e8"], ['f4', 'g4', 'h4'], ['e3', 'e2', 'e1'], ['d4', 'c4', 'b4', 'a4']])


if __name__ == '__main__':
    unittest.main()
