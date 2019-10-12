import random
moveCount = 0
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
        self.moveCount = 0
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
        return self.Player2

    # Setter that sets player1
    def setPlayer1(self, player=Player()):
        self.Player1 = player

    # Setter that sets player2
    def setPlayer2(self, player=Player()):
        self.Player2 = player

    # Helper Method to get the opposite player
    def getOpponent(self, player = Player()):
        if player == self.Player1:
            return self.Player2
        return self.Player1

    # Method used for testing if the coordinate of a board was updated
    def printTheField(self, row, column):
        print(self.theBoard.printCertainField(row, column))

    # Method to update the board of the game
    def updateBoard(self, board = Board()):   #Do we even use this? Method similar to Board class
        self.theBoard = board

    # Method that randomly chooses the play who should start
    def chooseFirstPlayer(self):
        value = random.randint(1,2)
        if value == 1:
            return self.Player1
        else:
            return self.Player2

    # Method that changes the turn of the player
    def switchPlayers(self):
        if self.currentPlayer == self.Player1:
            self.currentPlayer = self.Player2
        else:
            self.currentPlayer = self.Player1

    # Method that runs the game until at least one player has used up all their tokens
    def playGame(self):
        count = 1
        while self.Player1.getTokens() != 0 or self.Player2.getTokens() != 0 or self.moveCount < 31 :
            value = 0
            if self.currentPlayer is self.Player1:
                value = 1
            if self.currentPlayer is self.Player2:
                value = 2
            print("It is", self.currentPlayer.getName(), "'s turn.")
            self.chooseTokenMove(value, count)
            count = count + 1
            if self.isWinner(self.currentPlayer):
                break
            self.printGame()
            self.switchPlayers()

        print("The winner is", self.currentPlayer)  #Must check there is actually a winner and the game is not tied especially after 30 moves

    # Method to determine if there is a winner
    def isWinner(self, player = Player()):
         #NOTE: This is not calculating correctly, it needs to do it around all adjacent ones
         x = int(self.lastPieceXCoordinate)
         y = int(self.lastPieceYCoordinate)
        # corner1x = x - 1
        # corner1y = y - 1
        # corner1Owner = self.getBoard().getCoordinate(corner1x, corner1y).getOwner()
        # corner2x = x - 1
        # corner2y = y + 1
        # corner2Owner = self.getBoard().getCoordinate(corner2x, corner2y).getOwner()
        # corner3x = x + 1
        # corner3y = y - 1
        # corner3Owner = self.getBoard().getCoordinate(corner3x, corner3y).getOwner()
        # corner4x = x + 1
        # corner4y = y + 1
        # corner4Owner = self.getBoard().getCoordinate(corner4x, corner4y).getOwner()
        # crossOneX = x
        # crossOneY = y-1
        # crossOneOwner = self.getBoard().getCoordinate(crossOneX, crossOneY).getOwner()
        # crossTwoX = x
        # crossOneY = y+1
        # crossTwoOwner = self.getBoard().getCoordinate(crossTwoX, crossOneY).getOwner()
        # playerToVerify = player
        # if playerToVerify == corner1Owner and playerToVerify == corner2Owner and playerToVerify == corner3Owner and playerToVerify == corner4Owner:
        #     # Verifies if the other player has crossed out the X
        #     opponent = self.getOpponent(player)
        #     if crossOneOwner!= opponent and crossTwoOwner != opponent:
        #         return True
        # return False

    # The Player chooses if they want to place a new token or move a token they own
    def chooseTokenMove(self, value, count):
        if count < 3:
            self.placeToken(value)
        else:
            while True:
                TokenMoveValue = input ("Do you want to place new token(N) or move an existing token(M)?: ")
                if TokenMoveValue == "N" or TokenMoveValue == "n":
                    self.placeToken(value)
                    break
                elif TokenMoveValue == 'M' or TokenMoveValue == "m":
                     if moveCount < 31: # number of moves must be 30
                        self.move(value)
                        break
                     else:
                        print("Game reached its number of moves ... ")
                        break

                else:
                    print('The input is not correct. Please follow instructions below.')

    # The Method gets the coordinates of the token from player, verifies it, and move it
    def move(self, value):
        board = self.getBoard()
        while True:
            x, y = self.chooseCoordinates()
            theCoordinates = board.getCoordinate(x, y)
            owner = theCoordinates.getOwner()
            if owner.getName() == self.currentPlayer.getName():
                break
            else:
                print("The token does not belong to you. Please enter another token coordinate")

        accepted_direction = {'N', 'n', 'S', 's', 'E', 'e', 'W', 'w', 'NE', 'ne', 'Ne', 'nE', 'NW', 'nw', 'Nw', 'nW', 'SE', 'se', 'Se', 'sE', 'sW', 'Sw', 'SW', 'sw'}

        while True:
            direction = input("Please enter a cardinal direction to move the token (N, S, E, W, NE, NW, SE, SW: ")
            if direction in accepted_direction:
                break
            else:
                print("The direction is not correct. Please enter another direction")

        if direction == 'N' or direction == 'n':
            if x > 0:
                newCoordinate = board.getCoordinate(x-1, y)
                if newCoordinate.getOwner().getName() == 'null':
                    theCoordinates.releaseCoordinate()
                    theGame =self.updateGame(x-1,y,value)
                    self.moveCount = moveCount+1
                    return theGame
            else:
                print("You can not have this move on this token. Please try again.")
                self.move(value)

        elif direction == 'S' or direction == 's':
            if x < 11:
                newCoordinate = board.getCoordinate(x+1, y)
                if newCoordinate.getOwner().getName() == 'null':
                    theCoordinates.releaseCoordinate()
                    theGame =self.updateGame(x+1,y,value)
                    self.moveCount = moveCount+1
                    return theGame
            else:
                print("You can not have this move on this token. Please try again.")
                self.move(value)

        elif direction == 'E' or direction == 'e':
            if y < 9:
                newCoordinate = board.getCoordinate(x, y+1)
                if newCoordinate.getOwner().getName() == 'null':
                    theCoordinates.releaseCoordinate()
                    theGame =self.updateGame(x,y+1,value)
                    board = theGame.getBoard()
                    self.moveCount = moveCount+1
                    return theGame
            else:
                print("You can not have this move on this token. Please try again.")
                self.move(value)

        elif direction == 'W' or direction == 'w':
            if y > 0:
                newCoordinate = board.getCoordinate(x, y-1)
                if newCoordinate.getOwner().getName() == 'null':
                    theCoordinates.releaseCoordinate()
                    theGame =self.updateGame(x,y-1,value)
                    self.moveCount = moveCount+1
                    return theGame
            else:
                print("You can not have this move on this token. Please try again.")
                self.move(value)

        elif direction == 'NE' or direction == 'ne' or direction == 'nE' or direction == 'Ne':
            if x > 0 and y < 9:
                newCoordinate = board.getCoordinate(x-1, y+1)
                if newCoordinate.getOwner().getName() == 'null':
                    theCoordinates.releaseCoordinate()
                    theGame =self.updateGame(x-1,y+1,value)
                    self.moveCount = moveCount+1
                    return theGame
            else:
                print("You can not have this move on this token. Please try again.")
                self.move(value)

        elif direction == 'NW' or direction == 'nw' or direction == 'nW' or direction == 'Nw':
            if x > 0 and y > 0:
                newCoordinate = board.getCoordinate(x-1, y-1)
                if newCoordinate.getOwner().getName() == 'null':
                    theCoordinates.releaseCoordinate()
                    theGame =self.updateGame(x-1,y-1,value)
                    self.moveCount = moveCount+1
                    return theGame
            else:
                print("You can not have this move on this token. Please try again.")
                self.move(value)

        elif direction == 'SE' or direction == 'se' or direction == 'sE' or direction == 'Se':
            if x < 11 and y < 9:
                newCoordinate = board.getCoordinate(x+1, y+1)
                if newCoordinate.getOwner().getName() == 'null':
                    theCoordinates.releaseCoordinate()
                    theGame =self.updateGame(x+1,y+1,value)
                    self.moveCount = moveCount+1
                    return theGame
            else:
                print("You can not have this move on this token. Please try again.")
                self.move(value)

        elif direction == 'SW' or direction == 'sw' or direction == 'sw' or direction == 'sw':
            if x < 11 and  y > 0:
                newCoordinate = board.getCoordinate(x+1, y-1)
                if newCoordinate.getOwner().getName() == 'null':
                    theCoordinates.releaseCoordinate()
                    theGame =self.updateGame(x+1,y-1,value)
                    self.moveCount = moveCount+1
                    return theGame
        else:
            print("You can not have this move on this token. Please try again.")
            self.move(value)


    # Helper method that asks the user for the position where they want to place the token
    def chooseCoordinates(self):
        while True:
            value = input("Enter the position where you want to place/move your token: ")
            length = len(value)
            if length != 2:
                print("Incorrect value entered, try again.\n")
            else:
                value.split()
                if -1 < int(value[1]) < 10 and 96 < ord(value[0]) < 109 or 64 < ord(value[0]) < 77:
                    break
                else:
                    print("Incorrect value entered, try again.\n")
        if value[0] == 'A' or value[0] == 'a':
            x = 0
        elif value[0] == 'B' or value[0] == 'b':
            x = 1
        elif value[0] == 'C' or value[0] == 'c':
            x = 2
        elif value[0] == 'D' or value[0] == 'd':
            x = 3
        elif value[0] == 'E' or value[0] == 'e':
            x = 4
        elif value[0] == 'F' or value[0] == 'f':
            x = 5
        elif value[0] == 'G' or value[0] == 'g':
            x = 6
        elif value[0] == 'H' or value[0] == 'h':
            x = 7
        elif value[0] == 'I' or value[0] == 'i':
            x = 8
        elif value[0] == 'J' or value[0] == 'j':
            x = 9
        elif value[0] == 'K' or value[0] == 'k':
            x = 10
        elif value[0] == 'L' or value[0] == 'l':
            x = 11
        y = value[1]
        y = int(y)
        x = int(x)
        return x, y

    # Helper method to place a token on the board
    def placeToken(self, value):
        board = self.getBoard()
        theGame = "null"
        while theGame == "null":
            x, y = self.chooseCoordinates()
            theCoordinates = board.getCoordinate(x, y)
            owner = theCoordinates.getOwner()

            #thePlayer
            if value == 1:
                thePlayer = self.Player1
            if value == 2:
                thePlayer = self.Player2

            if (owner.getName() == 'null'):
                theGame =self.updateGame(x,y,value)

            else:
                print("Invalid Move. Please try again")
                continue

        self.lastPieceXCoordinate = int(x)
        self.lastPieceYCoordinate = int(y)
        return theGame


    # Helper method that updates the game
    def updateGame(self, x, y, value):
        self.theBoard = self.getBoard()
        coordinate = self.theBoard.getCoordinate(x, y)
        if value == 1:
            self.theBoard = self.theBoard.updateBoardWithPlayer(x,y,self.Player1)
            self.Player1.decreaseTokens()
            if self.Player1.getFirstMove():
                self.Player1.toggleFirstMove()
        elif value == 2:
            self.Player2.decreaseTokens()
            self.theBoard  = self.theBoard.updateBoardWithPlayer(x,y,self.Player2)
            if self.Player2.getFirstMove():
                self.Player2.toggleFirstMove()
        self.lastPieceXCoordinate = x
        self.lastPieceYCoordinate = y
        return self

    # Method that prints the board game
    def printGame(self):
        theBoard = self.getBoard()
        for i in range(0, 12):
            for j in range(0, 10):
                theCoordinate = theBoard.getCoordinate(i, j)
                if theCoordinate.getOwner() == 'null':
                    print('{:^1}'.format('-'), end='')
                elif theCoordinate.getOwner().getName() != "null": ## Should be fixed based off the player
                    if theCoordinate.getOwner() == self.Player1:
                        print('{:^1}'.format('P1'), end='')
                    elif theCoordinate.getOwner() == self.Player2:
                        print('{:^1}'.format('P2'), end='')
                #elif theCoordinate.getOwner() == 'null':
                #    print('{:^1}'.format('-'), end='')
                if j != 9:
                    print(" -> ", end='')
            print()
