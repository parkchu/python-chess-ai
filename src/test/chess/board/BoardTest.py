import unittest
from chess.board.Board import Board

class BoardTest(unittest.TestCase):

    def test_init_board(self):
        board = Board()

        piece = board.getPiece("a8")
        self.assertEqual(piece.image, "R")

    def test_move_piece(self):
        board = Board()
        currentPositon = "a2"
        targetPosition = "a3"
        currentPiece = board.getPiece(currentPositon)

        board.move(currentPositon, targetPosition)

        targetPiece = board.getPiece(targetPosition)
        self.assertEqual(currentPiece, targetPiece)
    

if __name__ == '__main__':
    unittest.main()
