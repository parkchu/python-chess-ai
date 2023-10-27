import unittest
from chess.board.Board import Board
from chess.board.Position import Position
from chess.pieces.Pawn import Pawn

class BoardTest(unittest.TestCase):

    def test_init_board(self):
        board = Board()

        piece = board.getPiece(Position.new("a8"))
        self.assertEqual(piece.image, "R")


    def test_move_piece(self):
        board = Board()
        currentPositon = Position.new("a2")
        targetPosition = Position.new("a3")
        currentPiece = board.getPiece(currentPositon)

        board.move(currentPositon, targetPosition)

        targetPiece = board.getPiece(targetPosition)
        self.assertEqual(currentPiece, targetPiece)


    def test_get_movable_positions(self):
        board = Board()
        pawnPosition = Position.new("a2")

        positions = board.getMovablePositions(pawnPosition)

        movablePositions = ["a3", "a4"]
        self.assertEqual(positions.getToString(), movablePositions)


    def test_get_movable_positions_already_move_pawn(self):
        board = Board()
        currentPositon = Position.new("a2")
        targetPosition = Position.new("a3")
        board.move(currentPositon, targetPosition)

        positions = board.getMovablePositions(targetPosition)

        movablePositions = ["a4"]
        self.assertEqual(positions.getToString(), movablePositions)

    
    def test_take_piece_pawn(self):
        board = Board()
        blackPawnPosition = Position.new("a3")
        whitePawnPosition = Position.new("b2")
        board.setPiece(blackPawnPosition, Pawn("black"))

        positions = board.getMovablePositions(whitePawnPosition)

        movablePositions = ["b3", "a3", "b4"]
        self.assertEqual(positions.getToString(), movablePositions)

    
    def test_get_movable_positions_rook(self):
        board = Board()
        pawnPosition = Position.new("a2")
        rookPosition = Position.new("a1")
        board.move(pawnPosition, Position.new("a4"))

        positions = board.getMovablePositions(rookPosition)

        movablePositions = ["a2", "a3"]
        self.assertEqual(positions.getToString(), movablePositions)


    def test_not_movable_positions_pawn(self):
        board = Board()
        blackPawnPosition = Position.new("a3")
        whitePawnPosition = Position.new("a2")
        board.setPiece(blackPawnPosition, Pawn("black"))

        positions = board.getMovablePositions(whitePawnPosition)

        movablePositions = []
        self.assertEqual(positions.getToString(), movablePositions)


    def test_not_movable_positions_rook(self):
        board = Board()
        blackPawnPosition = Position.new("a2")
        whiteRookPosition = Position.new("a1")
        board.setPiece(blackPawnPosition, Pawn("black"))

        positions = board.getMovablePositions(whiteRookPosition)

        movablePositions = ["a2"]
        self.assertEqual(positions.getToString(), movablePositions)
    

if __name__ == '__main__':
    unittest.main()
