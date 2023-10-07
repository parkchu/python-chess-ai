import unittest
import sys
sys.path.append("./src/main")
from board.Board import Board

class BoardTest(unittest.TestCase):

    def test_init_board(self):
        board = Board()

        piece = board.getPiece((0, 7))
        self.assertEqual(piece.image, "R")

    def test_move_piece(self):
        board = Board()
        currentPositon = (0, 1)
        targetPosition = (0, 2)
        currentPiece = board.getPiece(currentPositon)

        board.move(currentPositon, targetPosition)

        targetPiece = board.getPiece(targetPosition)
        self.assertEqual(currentPiece, targetPiece)
    

if __name__ == '__main__':
    unittest.main()
