# This is the coordinate class that contains all the information pertaining to the coordinates on a board
class Coordinate:
    from Player import Player

    # Default constructor
    def __init__(self, color=None, owner=Player()):
        if color is not None:
            self.color = color
        self.owner = owner

    # Setter that sets the owner of the coordinate
    def setOwner(self, owner):
        self.owner = owner

    # Method used when moving token to another place
    def releaseCoordinate(self):
        from Player import Player
        self.owner = Player()

    # Setter that sets the color of the coordinate
    def setColor(self, color):
        self.color = color

    # Getter that returns the owner of the coordinate
    def getOwner(self):
        return self.owner

    # Getter that returns the color of the coordinate
    def getColor(self):
        return self.color
