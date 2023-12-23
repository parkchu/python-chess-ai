class Ai:
    def __init__(self):
        self.history = []

    
    def getMovePosition(self, board, team):
        try:
            currentPosition = self.getCurrentPosition(board, team)
            targetPosition = self.getTargetPosition(board, currentPosition)
            movePosition = {
            "currentPosition": currentPosition,
            "targetPosition": targetPosition
            }
            return movePosition
        except:
            return self.getMovePosition(board, team)
    

    def getCurrentPosition(self, board, team):
        positions = board.getPositionsByTeam(team)
        return positions.getRandomPosition()
    

    def getTargetPosition(self, board, currentPosition):
        movablePositions = board.getMovablePositions(currentPosition)
        return movablePositions.getRandomPosition()
