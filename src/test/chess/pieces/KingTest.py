import unittest
from chess.pieces.King import King
from chess.pieces.Piece import Team

class KingTest(unittest.TestCase):

    def test_make_white_king(self):
        piece = King(Team.WHITE)
        
        self.assertEqual(piece.image, "k")


if __name__ == '__main__':
    unittest.main()
