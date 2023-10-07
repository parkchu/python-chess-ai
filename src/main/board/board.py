from pieces.Pawn import Pawn
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.King import King
from pieces.Queen import Queen
from pieces.NonePiece import NonePiece

class Board:

    def __init__(self):
        self.gameboard = {}
        self.mkbaord()


    def mkbaord(self):    
        placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    

        for i in range(0,8):
            self.gameboard[(7,i)] = placers[i]("black")
            self.gameboard[(6,i)] = Pawn("black")
            for x in range(2, 6):
                self.gameboard[(x, i)] = NonePiece()
            self.gameboard[(1,i)] = Pawn("white")
            self.gameboard[(0,i)] = placers[i]("white")

        self.gameboard = dict(sorted(self.gameboard.items()))
            

    def getBoard(self):
        board = list(map(self.test, self.gameboard))
        return self.listChunk(board, 8)
    
    def test(self, coordinate):
        piece = self.gameboard[coordinate]
        return str(coordinate)
    
    def listChunk(self, lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]
