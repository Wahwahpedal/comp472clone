# This is the Game class that contains the methods used in creating the game
import random
from random import randrange

import numpy as np

from colorama import Fore, Style


class Game:
    from Player import Player

    # Default Constructor
    def __init__(self, name1, name2, playWithComputer):
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
        self.computerMoves = np.array([])
        self.player1Moves = np.array([])
        self.computerOpponent = playWithComputer

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
    def getOpponent(self, player=Player()):
        if player == self.Player1:
            return self.Player2
        return self.Player1

    # Method used for testing if the coordinate of a board was updated
    def printTheField(self, row, column):
        print(self.theBoard.printCertainField(row, column))

    # Method that randomly chooses the play who should start
    def chooseFirstPlayer(self):
        value = random.randint(1, 2)
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
        while self.moveCount < 31:
            value = 0
            if self.currentPlayer is self.Player1:
                value = 1
                print("It is Player 1 (P1)'s turn, ", self.currentPlayer.getName(), ":")
            if self.currentPlayer is self.Player2:
                value = 2
                print("It is Player 2 (P2)'s turn, ", self.currentPlayer.getName(), ":")
            if (self.currentPlayer.getTokens() > 0):  # If player has tokens, they can either place token or move tokens
                print("You have", self.currentPlayer.getTokens(), "tokens remaining.")
                self.chooseTokenMove(value, count)
            else:  # Once the player has used all their tokens, they can only move tokens around
                print("You have used up all your tokens. Now, you can only move tokens. There are ", self.moveCount,
                      "moves left in the game.")
                self.move(value)
            count = count + 1
            if self.isWinner(int(self.lastPieceXCoordinate), int(self.lastPieceYCoordinate), self.currentPlayer):
                self.winner = self.currentPlayer
                break

            if self.wasLastRoundAMove and 0 < int(self.lastMoveYCoordinate) < 11 and self.isWinner((self.lastMoveXCoordinate + 1), self.lastMoveYCoordinate, self.getOpponent()):
                self.winner = self.getOpponent()
                break

            self.printGame()
            self.switchPlayers()

        self.printGame()
        if (self.winner != "null"):
            print("The winner is", self.winner.getName())
        else:
            print("The game resulted in a tie")

    # Method to determine if there is a winner
    def isWinner(self, x, y, player=Player()):

        if self.checkCorners(x, y, player):
            return True

        corner1x = x - 1
        corner1y = y - 1

        if self.checkCorners(corner1x, corner1y, player):
            return True

        corner2x = x - 1
        corner2y = y + 1

        if self.checkCorners(corner2x, corner2y, player):
            return True

        corner3x = x + 1
        corner3y = y - 1

        if self.checkCorners(corner3x, corner3y, player):
            return True

        corner4x = x + 1
        corner4y = y + 1

        if self.checkCorners(corner4x, corner4y, player):
            return True
        return False

    # The Player chooses if they want to place a new token or move a token they own
    def chooseTokenMove(self, value, count):
        if self.moveCount < 31 and (self.currentPlayer.getTokens() != 0):
            if count < 3:
                self.placeToken(value)
            else:
                while True:
                    TokenMoveValue = input("Do you want to place new token(N) or move an existing token(M)?: ")
                    if TokenMoveValue == "N" or TokenMoveValue == "n":
                        self.placeToken(value)
                        break
                    elif TokenMoveValue == 'M' or TokenMoveValue == "m":
                        if self.moveCount < 31:  # number of moves must be equal to or less than 30
                            self.move(value)
                            break
                        else:
                            print("Game reached its number of moves ... ")
                            break

                    else:
                        print('The input is not correct. Please follow instructions below.')

        elif self.moveCount < 31 and (self.currentPlayer.getTokens() == 0):
            print("You do not have any more tokens to place  but can move existing tokens.")
            if self.moveCount < 31:  # number of moves must be 30
                print("You have ", self.moveCount, "moves left.")
                self.move(value)
            else:
                print("Game reached its number of moves ... ")

    # The Method gets the coordinates of the token from player, verifies it, and move it
    def move(self, value):
        board = self.getBoard()
        accepted_direction = []
        printed_direction = []
        direction = 0

        while True:
            if value == 1 or self.computerOpponent == False:
                x, y = self.chooseCoordinates()
            elif value == 2 and self.computerOpponent == True:
                position = self.chooseMove()
                thePosition = position
                position.split()
                x = int(self.getValue(position[0]))
                if len(position) == 2:
                    y = (int(position[1])) - 1
                elif len(position) == 3:
                    y = int(str((position[1])) + str(position[2])) - 1
            theCoordinates = board.getCoordinate(x, y)
            owner = theCoordinates.getOwner()
            if owner.getName() == self.currentPlayer.getName():
                if x > 0:
                    if board.getCoordinate(x - 1, y).getOwner().getName() == 'null':
                        accepted_direction.append('N')
                        if value == 1 or self.computerOpponent == False:  # Allows for user to enter lower or capitals but is not needed for the computer
                            accepted_direction.append('n')
                            printed_direction.append('N')
                    if y > 0 and board.getCoordinate(x - 1, y - 1).getOwner().getName() == 'null':
                        accepted_direction.append('NW')
                        if value == 1 or self.computerOpponent == False:  # Allows for user to enter lower or capitals but is not needed for the computer
                            accepted_direction.append('nw')
                            accepted_direction.append('nW')
                            accepted_direction.append('Nw')
                            printed_direction.append('NW')
                    if y < 9 and board.getCoordinate(x - 1, y + 1).getOwner().getName() == 'null':
                        accepted_direction.append('NE')
                        if value == 1 or self.computerOpponent == False:  # Allows for user to enter lower or capitals but is not needed for the computer
                            accepted_direction.append('ne')
                            accepted_direction.append('nE')
                            accepted_direction.append('Ne')
                            printed_direction.append('NE')

                if x < 11:
                    if board.getCoordinate(x + 1, y).getOwner().getName() == 'null':
                        accepted_direction.append('S')
                        if value == 1 or self.computerOpponent == False:  # Allows for user to enter lower or capitals but is not needed for the computer
                            accepted_direction.append('s')
                            printed_direction.append('S')
                    if y > 0 and board.getCoordinate(x + 1, y - 1).getOwner().getName() == 'null':
                        accepted_direction.append('SW')
                        if value == 1 or self.computerOpponent == False:  # Allows for user to enter lower or capitals but is not needed for the computer
                            accepted_direction.append('sw')
                            accepted_direction.append('sW')
                            accepted_direction.append('Sw')
                            printed_direction.append('SW')
                    if y < 9 and board.getCoordinate(x + 1, y + 1).getOwner().getName() == 'null':
                        accepted_direction.append('SE')
                        if value == 1 or self.computerOpponent == False:  # Allows for user to enter lower or capitals but is not needed for the computer
                            accepted_direction.append('se')
                            accepted_direction.append('sE')
                            accepted_direction.append('Se')
                            printed_direction.append('SE')

                if y > 0 and board.getCoordinate(x, y - 1).getOwner().getName() == 'null':
                    accepted_direction.append('W')
                    if value == 1 or self.computerOpponent == False:  # Allows for user to enter lower or capitals but is not needed for the computer
                        accepted_direction.append('w')
                        printed_direction.append('W')

                if y < 9 and board.getCoordinate(x, y + 1).getOwner().getName() == 'null':
                    accepted_direction.append('E')
                    if value == 1 or self.computerOpponent == False:  # Allows for user to enter lower or capitals but is not needed for the computer
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
            if value == 1 or self.computerOpponent == False:
                print("You may chose the following cardinal directions: " + ', '.join(printed_direction))
                direction = input("Please enter a cardinal direction to move the token:")
                if direction in accepted_direction:
                    break
                else:
                    print("Please enter a valid direction")
            elif value == 2 and self.computerOpponent == True:
                s = " "
                s = s.join(accepted_direction)
                s = s.split()
                direction = self.chooseDirection(s)
                print("The direction chosen was: ", direction)
                break

        decrease = False
        if direction == 'N' or direction == 'n':
            theGame = self.updateGame(x - 1, y, value, decrease)
            self.lastPieceXCoordinate = int(x - 1)
            self.lastPieceYCoordinate = int(y)
        elif direction == 'S' or direction == 's':
            theGame = self.updateGame(x + 1, y, value, decrease)
            self.lastPieceXCoordinate = int(x + 1)
            self.lastPieceYCoordinate = int(y)
        elif direction == 'E' or direction == 'e':
            theGame = self.updateGame(x, y + 1, value, decrease)
            self.lastPieceXCoordinate = int(x)
            self.lastPieceYCoordinate = int(y + 1)
        elif direction == 'W' or direction == 'w':
            theGame = self.updateGame(x, y - 1, value, decrease)
            self.lastPieceXCoordinate = int(x)
            self.lastPieceYCoordinate = int(y - 1)
        elif direction == 'NE' or direction == 'ne' or direction == 'nE' or direction == 'Ne':
            theGame = self.updateGame(x - 1, y + 1, value, decrease)
            self.lastPieceXCoordinate = int(x - 1)
            self.lastPieceYCoordinate = int(y + 1)
        elif direction == 'NW' or direction == 'nw' or direction == 'nW' or direction == 'Nw':
            theGame = self.updateGame(x - 1, y - 1, value, decrease)
            self.lastPieceXCoordinate = int(x - 1)
            self.lastPieceYCoordinate = int(y - 1)
        elif direction == 'SE' or direction == 'se' or direction == 'sE' or direction == 'Se':
            theGame = self.updateGame(x + 1, y + 1, value, decrease)
            self.lastPieceXCoordinate = int(x + 1)
            self.lastPieceYCoordinate = int(y + 1)
        elif direction == 'SW' or direction == 'sw' or direction == 'sw' or direction == 'sw':
            theGame = self.updateGame(x + 1, y - 1, value, decrease)
            self.lastPieceXCoordinate = int(x + 1)
            self.lastPieceYCoordinate = int(y - 1)
        elif value ==1 and self.computerOpponent == True:
            newCoordinate = str(self.getCharacter(self.lastPieceXCoordinate)) + str(self.lastPieceYCoordinate +1)
            xCoordinate = self.getCharacter(x)
            yCoordinate = y+1
            thePosition = str(xCoordinate) + str(yCoordinate)
            self.player1Moves = np.where(self.player1Moves == thePosition, newCoordinate, self.player1Moves)
        if value == 2 and self.computerOpponent == True:
            newCoordinate = str(self.getCharacter(self.lastPieceXCoordinate)) + str(self.lastPieceYCoordinate + 1)
            self.computerMoves = np.where(self.computerMoves == thePosition, newCoordinate, self.computerMoves)
            print("The computer has moved from", thePosition, " to ", newCoordinate)
            print(self.computerMoves)  # NOTE: USED FOR TESTING

        self.theBoard = theGame.getBoard()
        theCoordinates.releaseCoordinate()

        self.moveCount = self.moveCount + 1
        self.wasLastRoundAMove = True
        self.lastMoveXCoordinate = int(x)
        self.lastMoveYCoordinate = int(y)

        return theGame

    # Helper method that asks the user for the position where they want to place the token
    def chooseCoordinates(self):
        length3 = False
        while True:
            value = input("Enter the position where you want to place/move your token: ")
            value = value.lower()
            length = len(value)
            if length != 2 and length != 3:
                print("Incorrect value entered, try again.\n")
            else:
                value.split()
                if length == 3 and int(value[1]) == 1 and int(value[2]) == 0:
                    length3 = True
                    break
                elif length == 3 and (not(int(value[1]) == 1 and int(value[2]) == 0)):
                    print("Incorrect value entered, try again.\n")
                elif value[1].isdigit() and 0 < int(value[1]) < 11 and 96 < ord(value[0]) < 109 or 64 < ord(
                        value[0]) < 77:
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

        if length3:
            y = 9
        else:
            y = value[1]
            y = int(y) - 1
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

            # thePlayer
            if value == 1:
                thePlayer = self.Player1
            if value == 2:
                thePlayer = self.Player2

            decrease = True
            if (owner.getName() == 'null'):
                theGame = self.updateGame(x, y, value, decrease)
            if self.computerOpponent and value == 1:
                thePosition = str(self.getCharacter(x)) + str(y+1)
                self.player1Moves = (np.append(self.player1Moves, thePosition))

            else:
                print("Invalid Move. Please try again")
                continue

        self.lastPieceXCoordinate = int(x)
        self.lastPieceYCoordinate = int(y)
        self.wasLastRoundAMove = False
        return theGame

    # Helper method to check if there's a winner
    def checkCorners(self, x, y, player=Player()):
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

        leftPiece = y - 1
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

    # Helper method that updates the game
    def updateGame(self, x, y, value, shouldDecrease):
        self.theBoard = self.getBoard()
        coordinate = self.theBoard.getCoordinate(x, y)
        if value == 1:
            self.theBoard = self.theBoard.updateBoardWithPlayer(x, y, self.Player1)
            if self.Player1.getTokens() > 0 and shouldDecrease == True:
                self.Player1.decreaseTokens()
            if self.Player1.getFirstMove():
                self.Player1.toggleFirstMove()
        elif value == 2:
            self.theBoard = self.theBoard.updateBoardWithPlayer(x, y, self.Player2)
            if self.Player2.getTokens() > 0 and shouldDecrease == True:
                self.Player2.decreaseTokens()
            if self.Player2.getFirstMove():
                self.Player2.toggleFirstMove()
        self.lastPieceXCoordinate = x
        self.lastPieceYCoordinate = y
        return self

    # Method that prints the board game
    def printGame(self):
        y_axis = ['A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ', 'J ', 'K ', 'L ']
        x_axis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        theBoard = self.getBoard()
        for i in range(0, 12):
            print(Fore.RED + '\033[1m' + y_axis[i], end=" ")
            for j in range(0, 10):
                theCoordinate = theBoard.getCoordinate(i, j)
                if theCoordinate.getOwner().getName() == 'null':
                    print(Style.RESET_ALL + '{:^3}'.format('--'), end='')
                elif theCoordinate.getOwner().getName() != "null":  ## Should be fixed based off the player
                    if theCoordinate.getOwner() == self.Player1:
                        print(Fore.BLUE + '{:^3}'.format('P1'), end='')
                    elif theCoordinate.getOwner() == self.Player2:
                        print(Fore.GREEN + '{:^3}'.format('P2'), end='')
                # elif theCoordinate.getOwner() == 'null':
                #    print('{:^1}'.format('-'), end='')
                if j != 9:
                    print(Style.RESET_ALL + " -> ", end='')
            print()
        print(
            Fore.RED + '\033[1m' + '    1       2     3      4      5      6      7      8      9     10' + Style.RESET_ALL)
        print("=====")

        # Method that runs the game until at least one player has used up all their tokens

    def playGameWithComputer(self):
        count = 1
        while self.moveCount < 31:
            print("The human's moves have been", self.player1Moves) #For testing
            print("Computer moves", self.computerMoves)
            value = 0
            if self.currentPlayer is self.Player2:
                value = 2
                print("It is the computer's turn:")
                TokenMoveValue = self.computerPlaceOrMove()
                if (TokenMoveValue == "N" or TokenMoveValue == "n" or (count < 3)) and (self.currentPlayer.getTokens() > 0):
                    if (not(count < 3)) and self.currentPlayer.getTokens() > 0:
                        print("The computer has chosen to place a new token")
                    self.computerPlaceToken()
                    print(self.computerMoves)  # NOTE: USED FOR TESTING
                    print("The computer has ", self.currentPlayer.getTokens(), " tokens remaining.")
                elif TokenMoveValue == 'M' or TokenMoveValue == "m" or self.currentPlayer.getTokens() <= 0:
                    if self.currentPlayer.getTokens() > 0:
                        print("The computer has chosen to move a token")
                    elif self.currentPlayer.getTokens() <= 0:
                        print("The computer has used up all their tokens and can only move tokens now. "
                              "There are ", self.moveCount, "moves left in the game.")
                    if self.moveCount < 31:  # number of moves must be 30
                        self.move(value)
                    else:
                        print("Game reached its number of moves ... ")
            elif self.currentPlayer is self.Player1:
                value = 1
                print("It is Player 1 (P1)'s turn, ", self.currentPlayer.getName(), ":")
                if (
                        self.currentPlayer.getTokens() > 0):  # If player has tokens, they can either place token or move tokens
                    print("You have", self.currentPlayer.getTokens(), "tokens remaining.")
                    self.chooseTokenMove(value, count)
                elif self.currentPlayer.getTokens() < 0:  # Once the player has used all their tokens, they can only move tokens around
                    print("You have used up all your tokens. Now, you can only move tokens. There are ", self.moveCount,
                          "moves left in the game.")
                    self.move(value)

            count = count + 1
            if self.isWinner(int(self.lastPieceXCoordinate), int(self.lastPieceYCoordinate), self.currentPlayer):
                self.winner = self.currentPlayer
                break

            if self.wasLastRoundAMove and 0 < int(self.lastMoveYCoordinate) < 11 and self.isWinner((self.lastMoveXCoordinate + 1), self.lastMoveYCoordinate, self.getOpponent()):
                self.winner = self.getOpponent()
                break

            self.printGame()
            self.switchPlayers()

        if self.moveCount <= 0:  # number of moves must be 30
            print("Game reached its number of moves ... ")

        self.printGame()
        if (self.winner != "null"):
            print("The winner is", self.winner.getName())
        else:
            print("The game resulted in a tie")

    # This function randomly generates a computers choice to place new token or move existing token
    def computerPlaceOrMove(self):
        options = ["N", "M"]
        return random.choice(options)

    # This function randomly generates where to place the token
    def computerPlaceToken(self):
        board = self.getBoard()
        theGame = "null"
        while theGame == "null":
            x = (randrange(11))
            y = (randrange(10))
            charOfX = self.getCharacter(x)
            theCoordinates = board.getCoordinate(x, y)
            owner = theCoordinates.getOwner()

            decrease = True
            if (owner.getName() == 'null'):
                thePosition = str(charOfX) + str(y + 1)
                print("The computer has placed a token on", thePosition, ".")
                theGame = self.updateGame(x, y, 2, decrease)
                self.computerMoves = (np.append(self.computerMoves, thePosition))
            else:
                continue

        self.lastPieceXCoordinate = int(x)
        self.lastPieceYCoordinate = int(y)
        self.wasLastRoundAMove = False
        return theGame

    def getValue(self, value):
        switcher = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            'K': 10,
            'L': 11
        }
        return switcher.get(value, "Invalid information")

    def getCharacter(self, value):
        switcher = {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F',
            6: 'G',
            7: 'H',
            8: 'I',
            9: 'J',
            10: 'K',
            11: 'L'
        }
        return switcher.get(value, "Invalid information")

    def chooseMove(self):
        return random.choice(self.computerMoves)

    def chooseDirection(self, availablepositions):
        return random.choice(availablepositions)
