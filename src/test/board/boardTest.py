import unittest
import sys
sys.path.append("./src/main")
from board.board import Board

class BoardTest(unittest.TestCase):

    def test_init_board(self):
        board = Board()
        piece = board.getPiece((0, 7))

        self.assertEqual(piece.image, "R")


if __name__ == '__main__':
    unittest.main()
