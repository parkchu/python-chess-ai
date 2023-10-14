from chess.pieces.Pawn import Pawn
from chess.pieces.Rook import Rook
from chess.pieces.Bishop import Bishop
from chess.pieces.Knight import Knight
from chess.pieces.King import King
from chess.pieces.Queen import Queen
from chess.pieces.NonePiece import NonePiece

class Board:

    def __init__(self):
        self.board = {}
        self.initBoard()


    def initBoard(self):
        files = [chr(x) for x in range(97, 105)]
        for y in reversed(range(1, 9)):
            for x in files:
                self.board["{}{}".format(x, y)] = NonePiece()

        self.setPieces()


    def setPieces(self):
        files = [chr(x) for x in range(97, 105)]
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(0,8):
            self.board["{}8".format(files[i])] = pieces[i]("black")
            self.board["{}7".format(files[i])] = Pawn("black")
            self.board["{}2".format(files[i])] = Pawn("white")
            self.board["{}1".format(files[i])] = pieces[i]("white")


    def getBoard(self):
        board = list(map(self.getPieceImage, self.board))
        return self.listChunk(board, 8)


    def getPieceImage(self, position):
        piece = self.getPiece(position)
        return piece.image


    def getPiece(self, position):
        piece = self.board[position]
        return piece
    

    def listChunk(self, lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    

    def move(self, currentPosition, targetPosition):
        currentPiece = self.board[currentPosition]
        self.board[currentPosition] = NonePiece()
        self.board[targetPosition] = currentPiece
        currentPiece.move()


    def getMovablePositions(self, position):
        piece = self.board[position]
        if (piece.team == None):
            return []
        
        return piece.getMovablePositions(position)
