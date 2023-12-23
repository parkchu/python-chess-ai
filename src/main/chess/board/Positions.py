import random

class Positions:

    def empty():
        return Positions([])


    def __init__(self, positions):
        self.positions = positions

    
    def append(self, position):
        if (position.isAvailable() and not self.contains(position)):
            self.positions.append(position)

    
    def appendAll(self, positions):
        for position in positions.positions:
            self.append(position)

    
    def getByIndex(self, index):
        return self.positions[index]
    
    
    def filter(self, condition, value):
        positions = Positions.empty()

        for position in self.positions:
            if (condition(value, position)):
                positions.append(position)

        return positions
        
    
    def contains(self, position):
        return position in self.positions
    

    def getToString(self):
        return list(map(lambda position: position.get(), self.positions))
    

    def isEmpty(self):
        return not self.positions
    

    def getRandomPosition(self):
        positions = self.positions.copy()
        random.shuffle(positions)
        return positions[0]
