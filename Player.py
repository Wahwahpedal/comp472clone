class Player:

    # Default Constructor
    def __init__ (self, name = None):
        self.isTurn = False
        self.firstMove = True
        self.numberOfTokens = 30
        if name is not None:
            self.name = name
        else:
            self.name = 'null'

    # Setter that returns a string
    def setName(name):
        self.name = name

    # Setter to return if it's the player's turn?
    def setPlayerIsTurn(isTurn):
        this.isTurn = isTurn

    def setNumberOfTokens(self, value):
        self.numberOfTokens = value

    # Getter that returns a string
    def getName(self):
        return self.name

    # Getter that returns a boolean
    def getIsTurn(self):
        return this.isTurn

    #Method used once the player has moved in the game
    def toggleFirstMove(self):
        if self.firstMove == False:
            self.firstMove = True
        else:
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

