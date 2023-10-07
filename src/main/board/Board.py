from pieces.Pawn import Pawn
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.King import King
from pieces.Queen import Queen
from pieces.NonePiece import NonePiece

class Board:

    def __init__(self):
        self.board = {}
        self.initBoard()


    def initBoard(self):
        for y in reversed(range(0, 8)):
            for x in range(0, 8):
                self.board[(x, y)] = NonePiece()

        self.setPieces()
            
    def setPieces(self):
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(0,8):
            self.board[(i,7)] = pieces[i]("black")
            self.board[(i,6)] = Pawn("black")
            self.board[(i,1)] = Pawn("white")
            self.board[(i,0)] = pieces[i]("white")

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
    
    def move(self, currentPosition, targetPositon):
        currentPiece = self.board[currentPosition]
        self.board[currentPosition] = NonePiece()
        self.board[targetPositon] = currentPiece
