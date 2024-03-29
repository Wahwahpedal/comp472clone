# This is the player class that contains all the methods that a player can do in the game
import copy

class Player:

    # Default Constructor
    def __init__ (self, name = None):
        self.isTurn = False
        self.firstMove = True
        self.numberOfTokens = 15
        if name is not None:
            self.name = name
        else:
            self.name = 'null'

    # Setter that returns a string
    def setName(self, name):
        self.name = name

    def clonePlayer(self):
        return copy.deepcopy(self)

    # Setter to return if it's the player's turn
    def setPlayerIsTurn(self, isTurn):
        self.isTurn = isTurn

    def setNumberOfTokens(self, value):
        self.numberOfTokens = value

    # Getter that returns a string
    def getName(self):
        return self.name

    # Getter that returns a boolean
    def getIsTurn(self):
        return self.isTurn

    #Method used once the player has moved in the game
    def toggleFirstMove(self):
        if self.firstMove:
            self.firstMove = False

    #Method to determine if the player has played yet
    def getFirstMove(self):
        return self.firstMove

    #Method to decrease the number of tokens. Used one the player has played a round
    def decreaseTokens(self):
        value = self.numberOfTokens - 1
        self.setNumberOfTokens(value)

    #Method to determine the number of tokens the player has left
    def getTokens(self):
        return self.numberOfTokens
