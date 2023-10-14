import unittest
from chess.pieces.Knight import Knight

class KnightTest(unittest.TestCase):
    
    def test_get_movable_positions(self):
        knight = Knight("white")
        position = "e4"

        positions = knight.getMovablePositions(position)

        self.assertEqual(positions, [["d6"], ["f6"], ["g5"], ["g3"], ['f2'], ['d2'], ['c3'], ['c5']])


if __name__ == '__main__':
    unittest.main()
