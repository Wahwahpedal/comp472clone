import random


class Game:
    from Board import Board
    from Player import Player

    # Default Constructor
    def __init__ (self, name1, name2):
        from Board import Board
        from Player import Player
        self.theBoard = Board()
        self.Player1 = Player(name1)
        self.Player2 = Player(name2)
        self.currentPlayer = self.chooseFirstPlayer()

    #Getter that returns an object of type board
    def getBoard(self):
        return self.theBoard

    #Getter that returns an object of type player
    def getPlayer1(self):
        return self.Player1

    #Getter that returns an object of type player
    def getPlayer2(self):
        return self.Player1

    #Setter that sets player1
    def setPlayer1(self, player=Player()):
        self.Player1 = player

    #Setter that sets player2
    def setPlayer2(self, player=Player()):
        self.Player2 = player

    #Method that prints the board
    def printTheBoard(self):
        print(self.theBoard.printFullBoard())

    #Method used for testing if the coordinate of a board was updated
    def printTheField(self, row, column):
        print(self.theBoard.printCertainField(row, column))

    #Method to update the board of the game
    def updateBoard(board = Board()):
        self.theBoard = board

    def chooseFirstPlayer(self):
        value = random.randint(1,2)
        if value == 1:
            return self.Player1
        else:
            return self.Player1

    def switchPlayers(self):
        if self.currentPlayer == self.Player1:
            self.currentPlayer = self.Player2
        else:
            self.currentPlayer = self.Player1

    #Method that runs the game until at least one player has used up all their tokens
    #NOTE: Need to modify to include that the game should be stopped if there's an X
    def playGame(self):
        while (self.Player1.getTokens() != 0 or self.Player2.getTokens() != 0):
            value = 0
            if self.currentPlayer is self.Player1:
                value = 1
            if self.currentPlayer is self.Player2:
                value = 2
            print("It is", self.currentPlayer.getName(), "'s turn.")
            self.placeToken(value)
            self.getBoard().printBoardOnlyTokens()
            self.switchPlayers()

    #Helper method that asks the user for the position where they want to place the token
    def chooseToken(self):
        value = input("Enter the position where you want to place your token: ")
        length = len(value)
        while length != 2:
            value = raw_input("Incorrect value entered, try again: ")
            length = len(value)
        value.split()
        x = 90
        if value[0] == 'A' or value[0] == 'a':
            x = 0
        if value[0] == 'B' or value[0] == 'b':
            x = 1
        if value[0] == 'C' or value[0] == 'c':
            x = 2
        if value[0] == 'D' or value[0] == 'd':
            x = 3
        if value[0] == 'E' or value[0] == 'e':
            x = 4
        if value[0] == 'F' or value[0] == 'f':
            x = 5
        if value[0] == 'G' or value[0] == 'g':
            x = 6
        if value[0] == 'H' or value[0] == 'h':
            x = 7
        if value[0] == 'I' or value[0] == 'i':
            x = 8
        if value[0] == 'J' or value[0] == 'j':
            x = 9
        y = value[1]
        y = int(y)
        x = int(x)
        return x, y

    #Helper method to place a token on the board
    def placeToken(self, value):
        board = self.getBoard()
        theGame = "null"
        while theGame == "null":
            x, y = self.chooseToken()
            theCoordinates = board.returnCoordinate(x, y)
            owner = theCoordinates.getOwner()
            #thePlayer
            if value == 1:
                thePlayer = self.Player1
            if value == 2:
                thePlayer = self.Player2
            if (thePlayer.getFirstMove() == True) and (owner.getName() == 'null'):
                theGame =self.updateGame(x,y,value)
                board = theGame.getBoard()
                theCoordinates = board.returnCoordinate(x, y)
                return theGame
            # #Need to try again if opponent has place one already
            else:
                corner1x = x-1
                corner1y = y-1
                corner2x = x-1
                corner2y = y+1
                corner3x = x+1
                corner3y = y-1
                corner4x = x+1
                corner4y = y+1
                if corner1x >= 0 and corner1y >= 0:
                    coordinateToVerify = board.returnCoordinate(corner1x,corner1y)
                    owner = coordinateToVerify.getOwner().getName()
                    print(owner)
                    print(self.Player1.getName())
                    if owner == thePlayer.getName():
                        theGame = self.updateGame(x,y,value)
                if corner2x <= 9 and corner2y <= 9:
                    coordinateToVerify = board.returnCoordinate(corner2x,corner2y)
                    owner = coordinateToVerify.getOwner()
                    if owner == thePlayer:
                        theGame = self.updateGame(x,y,value)
                if corner3x >= 0 and corner3y >= 0:
                    coordinateToVerify = board.returnCoordinate(corner3x,corner3y)
                    owner = coordinateToVerify.getOwner()
                    if owner == thePlayer:
                        theGame = self.updateGame(x,y,value)
                if corner4x <= 9 and corner4y <= 9:
                    coordinateToVerify = board.returnCoordinate(corner4x,corner4y)
                    owner = coordinateToVerify.getOwner()
                    if owner == thePlayer:
                        theGame = self.updateGame(x,y,value)
            if theGame == "null":
                print("Invalid Move. Please try again")
        return theGame

    #Helper method that updates the game
    def updateGame(self, x, y, value):
        self.theBoard = self.getBoard()
        coordinate = self.theBoard.returnCoordinate(x,y)
        if value == 1:
            self.theBoard = self.theBoard.updateBoard(x,y,self.Player1)
            self.Player1.decreaseTokens()
            if self.Player1.getFirstMove():
                self.Player1.toggleFirstMove()
        elif value == 2:
            self.Player2.decreaseTokens()
            self.theBoard  = self.theBoard.updateBoard(x,y,self.Player2)
            if self.Player2.getFirstMove():
                self.Player2.toggleFirstMove()
        return self