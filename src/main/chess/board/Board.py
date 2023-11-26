import copy
from chess.pieces.Pawn import Pawn
from chess.pieces.Rook import Rook
from chess.pieces.Bishop import Bishop
from chess.pieces.Knight import Knight
from chess.pieces.King import King
from chess.pieces.Queen import Queen
from chess.pieces.NonePiece import NonePiece
from chess.pieces.Piece import Team
from chess.util.exceptions import IllegalMovementException
from chess.util.exceptions import PromotionPositionException
from chess.util.exceptions import PromotionSourceException
from chess.util.exceptions import PromotionTargetException
from .Position import Position
from .Positions import Positions

class Board:

    def __init__(self, shouldSetup=True):
        self.board = {}
        self.kingPosition = {}
        self.initBoard()
        if (shouldSetup):
            self.setPieces()


    def initBoard(self):
        files = [chr(file) for file in range(97, 105)]
        ranks = [str(rank) for rank in reversed(range(1, 9))]
        for rank in ranks:
            for file in files:
                self.setPiece(Position(file, rank))
        self.kingPosition[Team.WHITE] = Position.new("e1")
        self.kingPosition[Team.BLACK] = Position.new("e8")


    def setPieces(self):
        files = [chr(file) for file in range(97, 105)]
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(0,8):
            self.setPiece(Position(files[i], "8"), pieces[i](Team.BLACK))
            self.setPiece(Position(files[i], "7"), Pawn(Team.BLACK))
            self.setPiece(Position(files[i], "2"), Pawn(Team.WHITE))
            self.setPiece(Position(files[i], "1"), pieces[i](Team.WHITE))


    def setPiece(self, position, piece=NonePiece()):
        self.board[position.get()] = piece
        if (piece.isIt(King)):
            self.kingPosition[piece.team] = position


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
            raise IllegalMovementException()
        currentPiece = self.getPiece(currentPosition)
        self.setPiece(currentPosition)
        self.setPiece(targetPosition, currentPiece)
        if (currentPiece.isIt(King)):
            self.castling(targetPosition, currentPosition.getDistance(targetPosition))
            self.kingPosition[currentPiece.team] = targetPosition
        currentPiece.move()


    def canMove(self, currentPosition, targetPosition):
        movablePositions = self.getMovablePositions(currentPosition)
        return movablePositions.contains(targetPosition)


    def getMovablePositions(self, position):
        piece = self.getPiece(position)
        positions = Positions.empty()

        if (piece.isNone()):
            return positions

        for distance in piece.getDistances():
            positions.appendAll(self.getMovablePath(position, distance))

        for direction in piece.getDirections():
            positions.appendAll(self.getMovablePath(position, direction, True))

        return positions
    

    def getMovablePath(self, position, distance, isDirection = False):
        positions = Positions.empty()
        nextPosition = position.move(distance)

        while (self.isContinuousMovable(nextPosition) and isDirection):
            if (not self.isCheckAfterMove(position, nextPosition)):
                positions.append(nextPosition)
            nextPosition = nextPosition.move(distance)
        
        if (self.isMovable(position, nextPosition)):
            positions.append(nextPosition)

        return positions
    

    def isContinuousMovable(self, position):
        return position.isAvailable() and self.getPiece(position).isNone()
    

    def isMovable(self, currentPosition, targetPosition):
        if (not targetPosition.isAvailable() or self.isCheckAfterMove(currentPosition, targetPosition)):
            return False
        
        piece = self.getPiece(currentPosition)

        if (piece.isIt(Pawn)):
            return self.isMovablePawn(currentPosition, targetPosition)
        
        if (piece.isCastling(currentPosition.getDistance(targetPosition))):
            return self.canCastling(currentPosition, targetPosition)
        
        return self.isMovableBasic(currentPosition, targetPosition)


    def isMovablePawn(self, currentPosition, targetPosition):
        currentPiece = self.getPiece(currentPosition)
        targetPiece = self.getPiece(targetPosition)
        direction = currentPosition.getDirection(targetPosition)

        if (currentPiece.isFirstMove and direction[0] == 0):
            betweenPiece = self.getPiece(currentPosition.move(direction))
            return targetPiece.isNone() and betweenPiece.isNone()
        
        if (direction[0] == 0):
            return targetPiece.isNone()
        
        return targetPiece.isEnemy(currentPiece)
    

    def canCastling(self, kingPosition, targetPosition):
        king = self.getPiece(kingPosition)
        if (self.isCheck(king.team)):
            return False
        
        direction = kingPosition.getDirection(targetPosition)
        nextPosition = kingPosition
        while (nextPosition != targetPosition):
            nextPosition = nextPosition.move(direction)
            if (self.isCheckAfterMove(kingPosition, nextPosition)):
                return False

        rookPosition = targetPosition.getCastlingRookPosition()
        rook = self.getPiece(rookPosition)
        return rook.isFirstMove and self.canMoveExcludingCheck(rookPosition, kingPosition.move(direction))


    def isMovableBasic(self, currentPosition, targetPosition):
        currentPiece = self.getPiece(currentPosition)
        targetPiece = self.getPiece(targetPosition)
        return targetPiece.isNone() or targetPiece.isEnemy(currentPiece)


    def castling(self, kingPosition, distance):
        king = self.getPiece(kingPosition)

        if (king.isCastling(distance)):
            rookPosition = kingPosition.getCastlingRookPosition()
            position = kingPosition.move(rookPosition.getDirection(kingPosition))
            rook = self.getPiece(rookPosition)
            self.setPiece(rookPosition)
            self.setPiece(position, rook)
            rook.move()


    def isCheckmate(self, team):
        positions = self.getPositionsByTeam(team)
        movablePositons = Positions.empty()
        for position in positions.positions:
            movablePositons.appendAll(self.getMovablePositions(position))
        return movablePositons.isEmpty()


    def isCheckAfterMove(self, currentPosition, targetPosition):
        board = copy.deepcopy(self)
        currentPiece = board.getPiece(currentPosition)
        board.setPiece(currentPosition)
        board.setPiece(targetPosition, currentPiece)
        return board.isCheck(currentPiece.team)


    def isCheck(self, team):
        positions = self.getPositionsByTeam(team.getEnemy())
        kingPosition = self.kingPosition[team]
        
        return any(self.canMoveExcludingCheck(position, kingPosition) for position in positions.positions)
    

    def getPositionsByTeam(self, team):
        lambdaFunction = lambda item: item[1].isWhite()
        if (team.isBlack()):
            lambdaFunction = lambda item: item[1].isBlack()
        points = filter(lambdaFunction, self.board.items())
        return Positions(list(map(lambda point: Position.new(point[0]), points)))
    
    
    def canMoveExcludingCheck(self, currentPosition, targetPosition):
        piece = self.getPiece(currentPosition)
        distance = currentPosition.getDistance(targetPosition)
        direction = currentPosition.getDirection(targetPosition)

        if (not piece.containsDirection(direction)):
            return piece.containsDistance(distance)
        
        nextPosition = currentPosition.move(direction)
        while (nextPosition != targetPosition and self.isContinuousMovable(nextPosition)):
            nextPosition = nextPosition.move(direction)

        return piece.containsDistance(distance) or nextPosition == targetPosition
    

    def promote(self, position, pieceType):
        piece = self.getPiece(position)

        if (not position.isEnd(piece.team)):
            raise PromotionPositionException()

        if (not piece.isIt(Pawn)):
            raise PromotionSourceException()
        
        if (pieceType in [Pawn, King]):
            raise PromotionTargetException()
        
        self.setPiece(position, pieceType(piece.team))    
