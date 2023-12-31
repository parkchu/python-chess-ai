class Ai:
    def __init__(self):
        pass

    
    def getMovePosition(self, board, team):
        if (board.isCheckmate(team)):
            raise Exception("체크메이트 당했습니다.")
        currentPosition = self.getCurrentPosition(board, team)
        targetPosition = self.getTargetPosition(board, currentPosition)
        notation = board.makeNotation(currentPosition, targetPosition)
        return notation
    

    def getCurrentPosition(self, board, team):
        dangerousPositions = board.getDangerousPositions(team)
        if dangerousPositions.isEmpty():
            return board.getPositionsByTeam(team).getRandomPosition()
        position = max(dangerousPositions.positions, key=lambda position:board.getPiece(position).point)
        return position


    def getTargetPosition(self, board, currentPosition):
        movablePositions = board.getMovablePositions(currentPosition)
        return movablePositions.getRandomPosition()
