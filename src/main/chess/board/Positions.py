class Positions:

    def __init__(self, positions=[]):
        self.positions = positions

    
    def append(self, position):
        if (position.isAvailable() and not self.contains(position)):
            self.positions.append(position)

    
    def getByIndex(self, index):
        return self.positions[index]
    
    
    def filter(self, condition, value):
        positions = []

        for position in self.positions:
            if (condition(value, position)):
                positions.append(position)

        return Positions(positions)
        
    
    def contains(self, position):
        return position in self.positions
