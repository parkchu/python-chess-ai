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


    def test_get_movable_positions(self):
        board = Board()
        pawnPosition = "a2"

        positions = board.getMovablePositions(pawnPosition)

        movablePositions = ["a3", "a4"]
        self.assertEqual(positions, movablePositions)


    def test_get_movable_positions_already_move_pawn(self):
        board = Board()
        currentPositon = "a2"
        targetPosition = "a3"
        board.move(currentPositon, targetPosition)

        positions = board.getMovablePositions(targetPosition)

        movablePositions = ["a4"]
        self.assertEqual(positions, movablePositions)

    
    def test_get_movable_positions_rook(self):
        board = Board()
        pawnPosition = "a2"
        rookPosition = "a1"
        board.move(pawnPosition, "a4")

        positions = board.getMovablePositions(rookPosition)

        movablePositions = ["a2", "a3"]
        self.assertEqual(positions, movablePositions)
    

if __name__ == '__main__':
    unittest.main()
