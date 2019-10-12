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
        self.lastPieceXCoordinate = "null"
        self.lastPieceYCoordinate = "null"

    # Getter that returns an object of type board
    def getBoard(self):
        return self.theBoard

    # Getter that returns an object of type player
    def getPlayer1(self):
        return self.Player1

    # Getter that returns an object of type player
    def getPlayer2(self):
        return self.Player1

    # Setter that sets player1
    def setPlayer1(self, player=Player()):
        self.Player1 = player

    # Setter that sets player2
    def setPlayer2(self, player=Player()):
        self.Player2 = player

    # Helper Method to get the opposite player
    def getOppoent(self, player = Player()):
        if player == self.Player1:
            return self.Player2
        return self.Player1

    # Method used for testing if the coordinate of a board was updated
    def printTheField(self, row, column):
        print(self.theBoard.printCertainField(row, column))

    # Method to update the board of the game
    def updateBoard(self, board = Board()):
        self.theBoard = board

    # Method that randomly chooses the play who should start
    def chooseFirstPlayer(self):
        value = random.randint(1,2)
        if value == 1:
            return self.Player1
        else:
            return self.Player1

    # Method that changes the turn of the player
    def switchPlayers(self):
        if self.currentPlayer == self.Player1:
            self.currentPlayer = self.Player2
        else:
            self.currentPlayer = self.Player1

    # Method that runs the game until at least one player has used up all their tokens
    def playGame(self):
        while (self.Player1.getTokens() != 0 or self.Player2.getTokens() != 0):
            value = 0
            if self.currentPlayer is self.Player1:
                value = 1
            if self.currentPlayer is self.Player2:
                value = 2
            print("It is", self.currentPlayer.getName(), "'s turn.")
            self.placeToken(value)
            if self.isWinner(self.currentPlayer):
                break
            self.printGame()
            self.switchPlayers()
        print("The winner is", self.currentPlayer)

    # Method to determine if there is a winner
    def isWinner(self, player = Player()):
        #NOTE: This is not calculating correctly, it needs to do it around all adjacent ones
        x = int(self.lastPieceXCoordinate)
        y = int(self.lastPieceYCoordinate)
        corner1x = x - 1
        corner1y = y - 1
        corner1Owner = self.getBoard().getCoordinate(corner1x, corner1y).getOwner()
        corner2x = x - 1
        corner2y = y + 1
        corner2Owner = self.getBoard().getCoordinate(corner2x, corner2y).getOwner()
        corner3x = x + 1
        corner3y = y - 1
        corner3Owner = self.getBoard().getCoordinate(corner3x, corner3y).getOwner()
        corner4x = x + 1
        corner4y = y + 1
        corner4Owner = self.getBoard().getCoordinate(corner4x, corner4y).getOwner()
        crossOneX = x
        crossOneY = y-1
        crossOneOwner = self.getBoard().getCoordinate(crossOneX, crossOneY).getOwner()
        crossTwoX = x
        crossOneY = y+1
        crossTwoOwner = self.getBoard().getCoordinate(crossTwoX, crossOneY).getOwner()
        playerToVerify = player
        if playerToVerify == corner1Owner and playerToVerify == corner2Owner and playerToVerify == corner3Owner and playerToVerify == corner4Owner:
            # Verifies if the other player has crossed out the X
            opponent = self.getOppoent(player)
            if crossOneOwner!= opponent and crossTwoOwner != opponent:
                return True
        return False

    # Helper method that asks the user for the position where they want to place the token
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

    # Helper method to place a token on the board
    def placeToken(self, value):
        board = self.getBoard()
        theGame = "null"
        while theGame == "null":
            x, y = self.chooseToken()
            theCoordinates = board.getCoordinate(x, y)
            owner = theCoordinates.getOwner()
            #thePlayer
            if value == 1:
                thePlayer = self.Player1
            if value == 2:
                thePlayer = self.Player2
            if (thePlayer.getFirstMove() == True) and (owner.getName() == 'null'):
                theGame =self.updateGame(x,y,value)
                board = theGame.getBoard()
                theCoordinates = board.getCoordinate(x, y)
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
                    coordinateToVerify = board.getCoordinate(corner1x, corner1y)
                    owner = coordinateToVerify.getOwner().getName()
                    print(owner)
                    print(self.Player1.getName())
                    if owner == thePlayer.getName():
                        theGame = self.updateGame(x,y,value)
                if corner2x <= 9 and corner2y <= 9:
                    coordinateToVerify = board.getCoordinate(corner2x, corner2y)
                    owner = coordinateToVerify.getOwner()
                    if owner == thePlayer:
                        theGame = self.updateGame(x,y,value)
                if corner3x >= 0 and corner3y >= 0:
                    coordinateToVerify = board.getCoordinate(corner3x, corner3y)
                    owner = coordinateToVerify.getOwner()
                    if owner == thePlayer:
                        theGame = self.updateGame(x,y,value)
                if corner4x <= 9 and corner4y <= 9:
                    coordinateToVerify = board.getCoordinate(corner4x, corner4y)
                    owner = coordinateToVerify.getOwner()
                    if owner == thePlayer:
                        theGame = self.updateGame(x,y,value)
            if theGame == "null":
                print("Invalid Move. Please try again")
        self.lastPieceXCoordinate = int(x)
        self.lastPieceYCoordinate = int(y)
        return theGame

    # Helper method that updates the game
    def updateGame(self, x, y, value):
        self.theBoard = self.getBoard()
        coordinate = self.theBoard.getCoordinate(x, y)
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
        self.lastPieceXCoordinate = x
        self.lastPieceYCoordinate = y
        return self

    # Method that prints the board game
    def printGame(self):
        theBoard = self.getBoard()
        for i in range(0, 10):
            for j in range(0, 10):
                theCoordinate = theBoard.getCoordinate(i, j)
                if theCoordinate.getOwner().getName() != "null": ## Should be fixed based off the player
                    if theCoordinate.getOwner() == self.Player1:
                        print('{:^1}'.format('P1'), end='')
                    elif theCoordinate.getOwner() == self.Player2:
                        print('{:^1}'.format('P2'), end='')
                else:
                    print('{:^1}'.format('-'), end='')
                if j != 9:
                    print(" -> ", end='')
            print()