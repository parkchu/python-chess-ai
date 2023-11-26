import unittest
from chess.board.Board import Board
from chess.board.Position import Position
from chess.pieces.Pawn import Pawn
from chess.pieces.King import King
from chess.pieces.Queen import Queen
from chess.pieces.Piece import Team
from chess.pieces.Rook import Rook
from chess.util.exceptions import PromotionPositionException
from chess.util.exceptions import PromotionSourceException
from chess.util.exceptions import PromotionTargetException
from chess.util.exceptions import IllegalMovementException

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
        whiteQueenPosition = Position.new("a1")
        whiteQueen = Queen(Team.WHITE)
        board.setPiece(blackKingPosition, blackKing)
        board.setPiece(whiteQueenPosition, whiteQueen)

        result = board.isCheck(Team.BLACK)

        self.assertEqual(result, True)

    
    def test_is_not_check(self):
        board = Board()

        result = board.isCheck(Team.BLACK)
        
        self.assertEqual(result, False)


    def test_is_not_check_by_pawn(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        whitePawnPosition = Position.new("a7")
        whitePawn = Pawn(Team.WHITE)
        board.setPiece(blackKingPosition, blackKing)
        board.setPiece(whitePawnPosition, whitePawn)

        result = board.isCheck(Team.BLACK)

        self.assertEqual(result, False)

    
    def test_is_check_after_move(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        whiteQueenPosition = Position.new("b1")
        whiteQueen = Queen(Team.WHITE)
        board.setPiece(blackKingPosition, blackKing)
        board.setPiece(whiteQueenPosition, whiteQueen)

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


    def test_get_movable_positions_when_is_check_after_move(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        whiteQueenPosition = Position.new("b1")
        whiteQueen = Queen(Team.WHITE)
        board.setPiece(blackKingPosition, blackKing)
        board.setPiece(whiteQueenPosition, whiteQueen)

        positions = board.getMovablePositions(blackKingPosition)

        movablePositions = ["a7"]
        self.assertEqual(positions.getToString(), movablePositions)

    
    def test_checkmate(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        whiteQueenPosition = Position.new("a7")
        whiteQueen = Queen(Team.WHITE)
        whitePawnPosition = Position.new("b6")
        whitePawn = Pawn(Team.WHITE)
        board.setPiece(blackKingPosition, blackKing)
        board.setPiece(whiteQueenPosition, whiteQueen)
        board.setPiece(whitePawnPosition, whitePawn)

        result = board.isCheckmate(Team.BLACK)

        self.assertEqual(result, True)


    def test_is_not_checkmate(self):
        board = Board(False)
        blackKingPosition = Position.new("a8")
        blackKing = King(Team.BLACK)
        whiteQueenPosition = Position.new("a7")
        whiteQueen = Queen(Team.WHITE)
        board.setPiece(blackKingPosition, blackKing)
        board.setPiece(whiteQueenPosition, whiteQueen)

        result = board.isCheckmate(Team.BLACK)

        self.assertEqual(result, False)

    
    def test_pawn_promotion(self):
        board = Board(False)
        whitePawnPosition = Position.new("a8")
        whitePawn = Pawn(Team.WHITE)
        board.setPiece(whitePawnPosition, whitePawn)

        board.promote(whitePawnPosition, Queen)

        whiteQueen = board.getPiece(whitePawnPosition)
        self.assertEqual(type(whiteQueen), Queen)


    def test_pawn_promotion_is_not_positon(self):
        board = Board(False)
        whiteQueenPosition = Position.new("a7")
        whiteQueen = Queen(Team.WHITE)
        board.setPiece(whiteQueenPosition, whiteQueen)

        try:
            board.promote(whiteQueenPosition, Queen)
        except Exception as exception:
            self.assertEqual(type(exception), PromotionPositionException)

    
    def test_pawn_promotion_is_not_pawn(self):
        board = Board(False)
        whiteQueenPosition = Position.new("a8")
        whiteQueen = Queen(Team.WHITE)
        board.setPiece(whiteQueenPosition, whiteQueen)

        try:
            board.promote(whiteQueenPosition, Queen)
        except Exception as exception:
            self.assertEqual(type(exception), PromotionSourceException)


    def test_pawn_promotion_is_not_pawn(self):
        board = Board(False)
        whitePawnPosition = Position.new("a8")
        whitePawn = Pawn(Team.WHITE)
        board.setPiece(whitePawnPosition, whitePawn)

        try:
            board.promote(whitePawnPosition, King)
        except Exception as exception:
            self.assertEqual(type(exception), PromotionTargetException)


    def test_castling(self):
        board = Board(False)
        whiteKingPosition = Position.new("e1")
        whiteKing = King(Team.WHITE)
        whiteRookPosition = Position.new("h1")
        whiteRook = Rook(Team.WHITE)
        board.setPiece(whiteKingPosition, whiteKing)
        board.setPiece(whiteRookPosition, whiteRook)

        board.move(whiteKingPosition, whiteKingPosition.move((2, 0)))

        afterKingPosition = Position.new("g1")
        afterRookPosition = Position.new("f1")
        self.assertEqual(board.getPiece(afterKingPosition), whiteKing)
        self.assertEqual(board.getPiece(afterRookPosition), whiteRook)

    
    def test_can_not_castling(self):
        board = Board(False)
        whiteKingPosition = Position.new("e1")
        whiteKing = King(Team.WHITE)
        whiteRookPosition = Position.new("h1")
        whiteRook = Rook(Team.WHITE)
        blackQueenPosition = Position.new("f3")
        blackQueen = Queen(Team.BLACK)
        board.setPiece(whiteKingPosition, whiteKing)
        board.setPiece(whiteRookPosition, whiteRook)
        board.setPiece(blackQueenPosition, blackQueen)

        try:
            board.move(whiteKingPosition, whiteKingPosition.move((2, 0)))
        except Exception as exception:
            self.assertEqual(type(exception), IllegalMovementException)


if __name__ == '__main__':
    unittest.main()
