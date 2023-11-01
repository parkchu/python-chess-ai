import unittest
from chess.pieces.Pawn import Pawn

class PawnTest(unittest.TestCase):

    def test_make_white_pawn(self):
        piece = Pawn("white")
        
        self.assertEqual(piece.image, "p")


    def test_get_distances_white(self):
        pawn = Pawn("white")

        distances = pawn.getDistances()

        self.assertEqual(distances, [(0, 1), (-1, 1), (1, 1), (0, 2)])


    def test_get_distances_black(self):
        pawn = Pawn("black")

        distances = pawn.getDistances()

        self.assertEqual(distances, [(0, -1), (-1, -1), (1, -1), (0, -2)])


    def test_already_move(self):
        pawn = Pawn("white")
        pawn.move()

        distances = pawn.getDistances()

        self.assertEqual(distances, [(0, 1), (-1, 1), (1, 1)])


if __name__ == '__main__':
    unittest.main()
