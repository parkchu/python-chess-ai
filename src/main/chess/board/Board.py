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
        if (not self.canMove(currentPosition, targetPosition)):
            raise Exception("움직일 수 없는 위치 입니다.")
        currentPiece = self.board[currentPosition]
        self.board[currentPosition] = NonePiece()
        self.board[targetPosition] = currentPiece
        currentPiece.move()


    def canMove(self, currentPosition, targetPosition):
        movablePositions = self.getMovablePositions(currentPosition)
        return targetPosition in movablePositions


    def getMovablePositions(self, position):
        positions = []
        piece = self.board[position]

        if (piece.isNone()):
            return positions
        
        for movablePositions in piece.getMovablePositions(position):
            for movablePosition in movablePositions:
                if (self.check(piece, position, movablePosition)):
                    positions.append(movablePosition)
                    if (self.board[movablePosition].isEnemy(piece)):
                        break
                else:
                    break
            
        return positions


    # def getMovablePositions(self, position):
    #     positions = []
    #     piece = self.board[position]

    #     if (piece.isNone()):
    #         return positions
        
    #     movablePositions = piece.getMovablePositions(position)
    #     for movablePosition in movablePositions:
    #         (positions.append(movablePosition) if self.check(piece, position, movablePosition) else None) 
    #     return positions


    def check(self, piece, currentPosition, targetPosition):
        if (piece.isIt(Pawn)):
            return self.checkMovablePawn(currentPosition, targetPosition)
        if (piece.isIt(Knight) or piece.isIt(King)):
            return self.checkMovableBasic(piece, targetPosition)
        return self.checkMovable(piece, currentPosition, targetPosition)


    def getDirection(self, currentPosition, targetPosition):
        x = self.toDirection(ord(targetPosition[0]) - ord(currentPosition[0]))
        y = self.toDirection(ord(targetPosition[1]) - ord(currentPosition[1]))
        return (x, y)
    

    def toDirection(self, value):
        if (value < 0):
            return -1
        if (value > 0):
            return 1
        return 0
    

    def checkMovablePawn(self, currentPosition, targetPosition):
        currentPiece = self.board[currentPosition]
        targetPiece = self.board[targetPosition]
        direction = self.getDirection(currentPosition, targetPosition)
        if (currentPiece.isFirstMove and direction[0] == 0):
            betweenPiece = self.board[self.moveDirection(currentPosition, direction)]
            return targetPiece.isNone() and betweenPiece.isNone()
        if (direction[0] == 0):
            return targetPiece.isNone()
        return targetPiece.isEnemy(currentPiece)
    

    def checkMovableBasic(self, currentPiece, targetPosition):
        targetPiece = self.board[targetPosition]
        return targetPiece.isNone() or targetPiece.isEnemy(currentPiece)
    

    def checkMovable(self, piece, currentPosition, targetPosition, direction=None):
        if (currentPosition == targetPosition):
            return True
        if (direction == None):
            direction = self.getDirection(currentPosition, targetPosition)
        nextPosition = self.moveDirection(currentPosition, direction)
        if (self.checkMovableBasic(piece, nextPosition)):
            return self.checkMovable(piece, nextPosition, targetPosition, direction)
        return False
    

    def moveDirection(self, position, direction):
        x = chr(ord(position[0]) + direction[0])
        y = chr(ord(position[1]) + direction[1])
        return x + y
