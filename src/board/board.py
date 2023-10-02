class Board:

    def __init__(self):
        self.gameboard = {}
        self.mkbaord()

    def mkbaord(self):
        for i in range(0,8):
            self.gameboard[(i,1)] = 'w_pawn'
            self.gameboard[(i,6)] = 'b_pawn'
        w_placers = ['wRook','wKnight','wBishop','wKing','wQueen','wBishop','wKnight','wRook']
        b_placers = ['bRook','bKnight','bBishop','bKing','bQueen','bBishop','bKnight','bRook']
        for i in range(0,8):
            self.gameboard[(i,0)] = w_placers[i]
            self.gameboard[((7-i),7)] = b_placers[i]
       
    
        
        

    
