import unittest
from chess.pieces.Pawn import Pawn
from chess.pieces.Piece import Team

class PawnTest(unittest.TestCase):

    def test_make_white_pawn(self):
        piece = Pawn(Team.WHITE)
        
        self.assertEqual(piece.image, "p")


    def test_get_distances_white(self):
        pawn = Pawn(Team.WHITE)

        distances = pawn.getDistances()

        self.assertEqual(distances, [(0, 1), (-1, 1), (1, 1), (0, 2)])


    def test_get_distances_black(self):
        pawn = Pawn(Team.BLACK)

        distances = pawn.getDistances()

        self.assertEqual(distances, [(0, -1), (-1, -1), (1, -1), (0, -2)])


    def test_already_move(self):
        pawn = Pawn(Team.WHITE)
        pawn.move()

        distances = pawn.getDistances()

        self.assertEqual(distances, [(0, 1), (-1, 1), (1, 1)])


if __name__ == '__main__':
    unittest.main()
