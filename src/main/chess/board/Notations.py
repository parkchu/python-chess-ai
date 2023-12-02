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
            return self.undoByWhite()
        self.checkUndo(self.black)
        return self.undoByBlack()
    

    def checkUndo(self, notations):
        if (not notations):
            raise IndexError("움직인 기물이 없으면 Undo 할 수 없습니다.")


    def undoByWhite(self):
        if (self.isLastMovementWhite()):
            return [self.white.pop()]
        return [self.black.pop(), self.white.pop()]
    

    def isLastMovementWhite(self):
        return len(self.white) > len(self.black)


    def undoByBlack(self):
        if (self.isLastMovementWhite()):
            return [self.white.pop(), self.black.pop()]
        return [self.black.pop()]
