class Position(object):

    def new(positionString):
        return Position(positionString[0], positionString[1])
    

    def __init__(self, file, rank):
        self.file = file
        self.rank = rank


    def __eq__(self, other):
        if isinstance(other, Position):
            return self.file == other.file and self.rank == other.rank
        return False


    def isAvailable(self):
        return 'a' <= self.file <= 'h' and '1' <= self.rank <= '8'


    def move(self, distance):
        return Position(chr(ord(self.file) + distance[0]), chr(ord(self.rank) + distance[1]))


    def get(self):
        return self.file + self.rank


    def getDistance(self, targetPosition):
        x = ord(targetPosition.file) - ord(self.file)
        y = ord(targetPosition.rank) - ord(self.rank)
        return (x, y)


    def getDirection(self, targetPosition):
        x = self.toDirection(ord(targetPosition.file) - ord(self.file))
        y = self.toDirection(ord(targetPosition.rank) - ord(self.rank))
        return (x, y)
    
    
    def toDirection(self, value):
        if (value < 0):
            return -1
        if (value > 0):
            return 1
        return 0
    

    def isEnd(self, team):
        return self.rank == team.getEndRank()
