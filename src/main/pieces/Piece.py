class Piece:
    def __init__(self, team, image):
        self.team = team
        self.image = self.setImage(image)

    def isWhite(self):
        return self.team == "white"
    
    def setImage(self, image):
        if (self.isWhite):
            return image
        return image.upper()
