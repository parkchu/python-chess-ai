class Piece:
    def __init__(self, team, image):
        self.team = team
        self.image = self.setImage(image)

    def isWhite(self):
        return self.team == "white"
    
    def isBlack(self):
        return self.team == "black"
    
    def setImage(self, image):
        if (self.isBlack()):
            return image.upper()
        return image
    
    def getMovablePositions(self, position):
        return []
