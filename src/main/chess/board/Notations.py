class Notations:

    def __init__(self):
        self.white = []
        self.black = []

    
    def save(self, notation):
        notations = self.black
        if (notation.isWhite()):
            notations = self.white
        notations.append(notation)

    
    def undo(self, team):
        if (team.isWhite()):
            self.checkUndo(self.white)
            return self.getUndoNotations(self.white, self.black, self.isLastMovementBlack())
        self.checkUndo(self.black)
        return self.getUndoNotations(self.black, self.white, self.isLastMovementWhite())
    

    def checkUndo(self, notations):
        if (not notations):
            raise IndexError("움직인 기물이 없으면 Undo 할 수 없습니다.")


    def getUndoNotations(self, ourNotations, enemyNotations, islastMovementEnemy):
        notations = []
        if (islastMovementEnemy):
            notations += self.getLastNotation(enemyNotations)
        notations += self.getLastNotation(ourNotations)
        return notations
    

    def getLastNotation(self, notations):
        notation = notations.pop()
        lastNotations = [notation]
        if (notation.isCastling()):
            lastNotations.append(notation.getCastlingNotation())
        return lastNotations
    

    def isLastMovementBlack(self):
        return len(self.black) == len(self.white)


    def isLastMovementWhite(self):
        return len(self.white) > len(self.black)
