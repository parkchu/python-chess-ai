class Board:

    def __init__(self):
        self.gameboard = {}
        self.mkbaord()

    def mkbaord(self):
        for i in range(0,8):
            self.gameboard[(1,i)] = 'w_pawn'
            self.gameboard[(6,i)] = 'b_pawn'
        w_placers = ['wRook','wKnight','wBishop','wKing','wQueen','wBishop','wKnight','wRook']
        b_placers = ['bRook','bKnight','bBishop','bKing','bQueen','bBishop','bKnight','bRook']
        for i in range(0,8):
            self.gameboard[(0,i)] = w_placers[i]
            self.gameboard[(7,(7-i))] = b_placers[i]
            
       
    
        
        

    
