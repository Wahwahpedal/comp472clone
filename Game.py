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
        self.lastMoveXCoordinate = "null"
        self.lastMoveYCoordinate = "null"
        self.wasLastRoundAMove = False
        self.winner = "null"

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
        while self.moveCount < 31 :
            value = 0
            if self.currentPlayer is self.Player1:
                value = 1
            if self.currentPlayer is self.Player2:
                value = 2
            print("It is", self.currentPlayer.getName(), "'s turn.")
            if(self.currentPlayer.getTokens() > 0):
                self.chooseTokenMove(value, count)
            else:
                self.move(value)
            count = count + 1
            if self.isWinner(int(self.lastPieceXCoordinate), int(self.lastPieceYCoordinate), self.currentPlayer):
                self.winner = self.currentPlayer
                break

            if self.wasLastRoundAMove and 0 < int(self.lastMoveYCoordinate) < 11 and self.isWinner((int(self.lastMoveXCoordinate) + 1), int(self.lastMoveYCoordinate), self.getOpponent()):
                self.winner = self.currentPlayer
                break
                
            self.printGame()
            self.switchPlayers()

        self.printGame()
        if (self.winner !="null"):
            print("The winner is", self.currentPlayer.getName())
        else:
            print("The game resulted in a tie")

    # Method to determine if there is a winner
    def isWinner(self, x, y, player = Player()):

         if self.checkCenterPiece(x, y, player):
             return True

         corner1x = x - 1
         corner1y = y - 1

         if self.checkCenterPiece(corner1x, corner1y, player):
             return True

         corner2x = x - 1
         corner2y = y + 1

         if self.checkCenterPiece(corner2x, corner2y, player):
             return True

         corner3x = x + 1
         corner3y = y - 1

         if self.checkCenterPiece(corner3x, corner3y, player):
             return True

         corner4x = x + 1
         corner4y = y + 1

         if self.checkCenterPiece(corner4x, corner4y, player):
             return True
         return False


    def checkCenterPiece(self, x, y, player = Player()):
        corner1x = x - 1
        corner1y = y - 1

        corner2x = x - 1
        corner2y = y + 1

        corner3x = x + 1
        corner3y = y - 1

        corner4x = x + 1
        corner4y = y + 1

        if corner1x < 0 or corner1x > 11 or 0 > corner1y > 9 or corner2x < 0 or corner2x > 11 or corner2y < 0 or corner2y > 9 or corner3x < 0 or corner3x > 11 or corner3y < 0 or corner3y > 9 or corner4x < 0 or corner4x > 11 or corner4y < 0 or corner4y > 9:
            return False

        corner1Owner = self.getBoard().getCoordinate(corner1x, corner1y).getOwner()
        if corner1Owner != player:
            return False

        corner2Owner = self.getBoard().getCoordinate(corner2x, corner2y).getOwner()
        if corner2Owner != player:
            return False


        corner3Owner = self.getBoard().getCoordinate(corner3x, corner3y).getOwner()
        if corner3Owner != player:
            return False

        corner4Owner = self.getBoard().getCoordinate(corner4x, corner4y).getOwner()
        if corner4Owner != player:
            return False

        leftPiece = y-1
        rightpiece = y + 1

        opponent = "null"

        if player is self.Player1:
            opponent = self.Player2
        elif player is self.Player2:
            opponent = self.Player1
        xValue = x

        leftOpponent = self.getBoard().getCoordinate(xValue, leftPiece).getOwner()
        rightOpponent = self.getBoard().getCoordinate(xValue, rightpiece).getOwner()

        if leftOpponent == opponent and rightOpponent == opponent:
            return False

        return True



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
        accepted_direction = []
        printed_direction = []

        while True:
            x, y = self.chooseCoordinates()
            theCoordinates = board.getCoordinate(x, y)
            owner = theCoordinates.getOwner()
            if owner.getName() == self.currentPlayer.getName():
                if x > 0 and board.getCoordinate(x - 1, y).getOwner().getName() =='null':
                    accepted_direction.append('N')
                    accepted_direction.append('n')
                    printed_direction.append('N')
                    if y > 0 and board.getCoordinate(x - 1, y - 1).getOwner().getName() =='null':
                        accepted_direction.append('NW')
                        accepted_direction.append('nw')
                        accepted_direction.append('nW')
                        accepted_direction.append('Nw')
                        printed_direction.append('NW')
                    if y < 9 and board.getCoordinate(x - 1, y + 1).getOwner().getName() =='null':
                        accepted_direction.append('NE')
                        accepted_direction.append('ne')
                        accepted_direction.append('nE')
                        accepted_direction.append('Ne')
                        printed_direction.append('NE')

                if x < 11 and board.getCoordinate(x + 1, y).getOwner().getName() =='null':
                    accepted_direction.append('S')
                    accepted_direction.append('s')
                    printed_direction.append('S')
                    if y > 0 and board.getCoordinate(x + 1, y - 1).getOwner().getName() =='null':
                        accepted_direction.append('SW')
                        accepted_direction.append('sw')
                        accepted_direction.append('sW')
                        accepted_direction.append('Sw')
                        printed_direction.append('SW')
                    if y < 9 and board.getCoordinate(x + 1, y + 1).getOwner().getName() =='null':
                        accepted_direction.append('SE')
                        accepted_direction.append('se')
                        accepted_direction.append('sE')
                        accepted_direction.append('Se')
                        printed_direction.append('SE')

                if y > 0 and board.getCoordinate(x, y - 1).getOwner().getName() =='null':
                    accepted_direction.append('W')
                    accepted_direction.append('w')
                    printed_direction.append('W')

                if y < 9 and board.getCoordinate(x, y + 1).getOwner().getName() =='null':
                    accepted_direction.append('E')
                    accepted_direction.append('e')
                    printed_direction.append('E')

                if len(accepted_direction) > 0:
                    break
                else:
                    print("No free coordinates are adjacent to this token. Please pick another token to move.")

            else:
                print("The token does not belong to you. Please enter another token coordinate")
                printed_direction.clear()
                accepted_direction.clear()



        while True:
            print("You may chose the following cardinal directions: " + ', '.join(printed_direction))
            direction = input("Please enter a cardinal direction to move the token:")
            if direction in accepted_direction:
                break
            else:
                print("Please enter a valid direction")

        if direction == 'N' or direction == 'n':
            theGame =self.updateGame(x-1,y,value)
            self.lastPieceXCoordinate = int(x-1)
            self.lastPieceYCoordinate = int(y)
        elif direction == 'S' or direction == 's':
            theGame = self.updateGame(x + 1, y, value)
            self.lastPieceXCoordinate = int(x+1)
            self.lastPieceYCoordinate = int(y)
        elif direction == 'E' or direction == 'e':
            theGame = self.updateGame(x, y + 1, value)
            self.lastPieceXCoordinate = int(x)
            self.lastPieceYCoordinate = int(y+1)
        elif direction == 'W' or direction == 'w':
            theGame = self.updateGame(x, y - 1, value)
            self.lastPieceXCoordinate = int(x)
            self.lastPieceYCoordinate = int(y-1)
        elif direction == 'NE' or direction == 'ne' or direction == 'nE' or direction == 'Ne':
            theGame = self.updateGame(x - 1, y + 1, value)
            self.lastPieceXCoordinate = int(x-1)
            self.lastPieceYCoordinate = int(y+1)
        elif direction == 'NW' or direction == 'nw' or direction == 'nW' or direction == 'Nw':
            theGame = self.updateGame(x - 1, y - 1, value)
            self.lastPieceXCoordinate = int(x-1)
            self.lastPieceYCoordinate = int(y-1)
        elif direction == 'SE' or direction == 'se' or direction == 'sE' or direction == 'Se':
            theGame = self.updateGame(x + 1, y + 1, value)
            self.lastPieceXCoordinate = int(x+1)
            self.lastPieceYCoordinate = int(y+1)
        elif direction == 'SW' or direction == 'sw' or direction == 'sw' or direction == 'sw':
            theGame = self.updateGame(x + 1, y - 1, value)
            self.lastPieceXCoordinate = int(x+1)
            self.lastPieceYCoordinate = int(y-1)

        self.theBoard = theGame.getBoard()
        theCoordinates.releaseCoordinate()

        self.moveCount = moveCount + 1
        self.wasLastRoundAMove = True
        self.lastMoveXCoordinate = int(x)
        self.lastMoveYCoordinate = int(y)

        return theGame



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

            if (owner.getName() =='null'):
                theGame =self.updateGame(x,y,value)

            else:
                print("Invalid Move. Please try again")
                continue

        self.lastPieceXCoordinate = int(x)
        self.lastPieceYCoordinate = int(y)
        self.wasLastRoundAMove = False
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
                if theCoordinate.getOwner().getName() == 'null':
                    print('{:^3}'.format('-'), end='')
                elif theCoordinate.getOwner().getName() != "null": ## Should be fixed based off the player
                    if theCoordinate.getOwner() == self.Player1:
                        print('{:^3}'.format('P1'), end='')
                    elif theCoordinate.getOwner() == self.Player2:
                        print('{:^3}'.format('P2'), end='')
                #elif theCoordinate.getOwner() == 'null':
                #    print('{:^1}'.format('-'), end='')
                if j != 9:
                    print(" -> ", end='')
            print()
