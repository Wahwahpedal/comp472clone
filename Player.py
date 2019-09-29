class Player:
    #from Board import Board
    #from Coordinate import Coordinate
    #isTurn = ""
    #firstMove
    #Board theBoard = ""

    def __init__ (self, name = None):
        self.isTurn = False
        self.firstMove = True
        if name is not None:
            self.name = name
        else:
            self.name='null'

    def setName(name):
        self.name = name

    def getName(self):
        return self.name

    def getIsTurn(self):
        return this.isTurn

    def toggleFirstMove(self):
        if self.firstMove == False:
            self.firstMove = True
        else:
            self.firstMove = False

    def getFirstMove(self):
        return self.firstMove

    def setPlayerIsTurn(isTurn):
        this.isTurn = isTurn
    #def placeToken(position):
        #Need to update board when a token is placed
