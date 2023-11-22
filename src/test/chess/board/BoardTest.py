import unittest
from chess.board.Board import Board
from chess.board.Position import Position
from chess.pieces.Pawn import Pawn
from chess.pieces.King import King
from chess.pieces.Queen import Queen
from chess.pieces.Piece import Team

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
        board.setPiece(blackPawnPosition, Pawn(Team.BLACK))

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
        board.setPiece(blackPawnPosition, Pawn(Team.BLACK))

        positions = board.getMovablePositions(whitePawnPosition)

        movablePositions = []
        self.assertEqual(positions.getToString(), movablePositions)


    def test_not_movable_positions_rook(self):
        board = Board()
        blackPawnPosition = Position.new("a2")
        whiteRookPosition = Position.new("a1")
        board.setPiece(blackPawnPosition, Pawn(Team.BLACK))

        positions = board.getMovablePositions(whiteRookPosition)

        movablePositions = ["a2"]
        self.assertEqual(positions.getToString(), movablePositions)

    
    def test_get_movable_positions_knight(self):
        board = Board()
        position = Position.new("b1")

        positions = board.getMovablePositions(position)

        movablePositions = ["a3", "c3"]
        self.assertEqual(positions.getToString(), movablePositions)

    
    def test_set_king(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        board.setPiece(blackKingPosition, blackKing)

        self.assertEqual(board.kingPosition[Team.BLACK], blackKingPosition)


    def test_set_king(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        board.setPiece(blackKingPosition, blackKing)
        movablePositon = Position.new("a7")
        
        board.move(blackKingPosition, movablePositon)

        self.assertEqual(board.kingPosition[Team.BLACK], movablePositon)


    def test_is_check(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        whiteQueenPositoin = Position.new("a1")
        whiteQueen = Queen(Team.WHITE)
        board.setPiece(blackKingPosition, blackKing)
        board.setPiece(whiteQueenPositoin, whiteQueen)

        result = board.isCheck(Team.BLACK)

        self.assertEqual(result, True)

    
    def test_is_not_check(self):
        board = Board()

        result = board.isCheck(Team.BLACK)
        
        self.assertEqual(result, False)

    
    def test_is_check_after_move(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        whiteQueenPositoin = Position.new("b1")
        whiteQueen = Queen(Team.WHITE)
        board.setPiece(blackKingPosition, blackKing)
        board.setPiece(whiteQueenPositoin, whiteQueen)

        result = board.isCheckAfterMove(blackKingPosition, blackKingPosition.move((1,0)))

        self.assertEqual(result, True)

    
    def test_is_not_check_after_move(self):
        board = Board()
        blackPawnPosition = Position.new("a7")
        movablePositon = Position.new("a6")

        result = board.isCheckAfterMove(blackPawnPosition, movablePositon)
        
        self.assertEqual(result, False)


    def test_is_check_after_move_not_moving(self):
        board = Board()
        blackPawnPosition = Position.new("a7")
        movablePositon = Position.new("a6")
        board.isCheckAfterMove(blackPawnPosition, movablePositon)

        piece = board.getPiece(movablePositon)
        
        self.assertEqual(piece.isNone(), True)


if __name__ == '__main__':
    unittest.main()
