class Piece:
    def __init__(self, team):
        self.team = team

    def isWhite(self):
        return self.team == "white"