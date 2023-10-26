from chess.pieces.Pawn import Pawn
from chess.pieces.Rook import Rook
from chess.pieces.Bishop import Bishop
from chess.pieces.Knight import Knight
from chess.pieces.King import King
from chess.pieces.Queen import Queen
from chess.pieces.NonePiece import NonePiece
from .Position import Position
from .Positions import Positions

class Board:

    def __init__(self):
        self.board = {}
        self.initBoard()


    def initBoard(self):
        files = [chr(file) for file in range(97, 105)]
        ranks = [str(rank) for rank in reversed(range(1, 9))]
        for rank in ranks:
            for file in files:
                self.setPiece(Position(file, rank))

        self.setPieces()


    def setPieces(self):
        files = [chr(file) for file in range(97, 105)]
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(0,8):
            self.setPiece(Position(files[i], "8"), pieces[i]("black"))
            self.setPiece(Position(files[i], "7"), Pawn("black"))
            self.setPiece(Position(files[i], "2"), Pawn("white"))
            self.setPiece(Position(files[i], "1"), pieces[i]("white"))


    def setPiece(self, position, piece=NonePiece()):
        self.board[position.get()] = piece


    def getBoard(self):
        board = list(map(self.getPieceImage, self.board))
        return self.listChunk(board, 8)


    def getPieceImage(self, positionString):
        position = Position.new(positionString)
        piece = self.getPiece(position)
        return piece.image


    def getPiece(self, position):
        piece = self.board[position.get()]
        return piece
    

    def listChunk(self, lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
    

    def move(self, currentPosition, targetPosition):
        if (not self.canMove(currentPosition, targetPosition)):
            raise Exception("움직일 수 없는 위치 입니다.")
        currentPiece = self.getPiece(currentPosition)
        self.setPiece(currentPosition)
        self.setPiece(targetPosition, currentPiece)
        currentPiece.move()


    def canMove(self, currentPosition, targetPosition):
        movablePositions = self.getMovablePositions(currentPosition)
        return movablePositions.contains(targetPosition)


    def getMovablePositions(self, position):
        piece = self.getPiece(position)

        if (piece.isNone()):
            return Positions.empty()
        
        movablePositions = piece.getMovablePositions(position)
        if (piece.isIt(Pawn)):
            return movablePositions.filter(self.canMovablePawn, position)
        
        if (piece.isIt(King) or piece.isIt(Knight)):
            return movablePositions.filter(self.canMovableBasic, position)
            
        movableEndPositions = piece.getMovableEndPositions(position)
        positions = Positions.empty()
        for movableEndPosition in movableEndPositions.positions:
            positions = self.getPositions(piece, position, movableEndPosition, positions)
        return positions


    def canMovablePawn(self, currentPosition, targetPosition):
        currentPiece = self.getPiece(currentPosition)
        targetPiece = self.getPiece(targetPosition)
        direction = currentPosition.getDirection(targetPosition)

        if (currentPiece.isFirstMove and direction[0] == 0):
            betweenPiece = self.getPiece(currentPosition.move(direction))
            return targetPiece.isNone() and betweenPiece.isNone()
        
        if (direction[0] == 0):
            return targetPiece.isNone()
        
        return targetPiece.isEnemy(currentPiece)    
    

    def canMovableBasic(self, currentPosition, targetPosition):
        currentPiece = self.getPiece(currentPosition)
        targetPiece = self.getPiece(targetPosition)
        return targetPiece.isNone() or targetPiece.isEnemy(currentPiece)
    

    def getPositions(self, piece, currentPosition, targetPosition, positions, direction=None):
        if (currentPosition == targetPosition):
            return positions
        
        if (direction == None):
            direction = currentPosition.getDirection(targetPosition)

        nextPosition = currentPosition.move(direction)
        if (not nextPosition.isAvailable()):
            return positions
        nextPiece = self.getPiece(nextPosition)
        if (nextPiece.isNone()):
            positions.append(nextPosition)
            return self.getPositions(piece, nextPosition, targetPosition, positions, direction)
        if (nextPiece.isEnemy(piece)):
            positions.append(nextPosition)
        return positions
