class Coordinate:
    from Player import Player
    #
    # def __init__ (self):
    #     self.color = 'null'
    #     self.owner = 'null'

    def __init__(self, color=None, owner = Player()):
        if color is not None:
            self.color = color
        self.owner = owner
        #self.owner = 'null'


    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setOwner(self, owner):
        self.owner = owner

    def getOwner(self):
        return self.owner
