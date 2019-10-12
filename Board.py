#import numpy
#import Coordinate

class Board:
    from Coordinate import Coordinate
    from Player import Player

    # Constructor that initializes the board to be a 2D-Array of type coordinates
    def __init__ (self):
        from Coordinate import Coordinate
        rows = 10
        cols = 10
        x = 10
        y = 10
        self.TheBoard = [0] * x
        for i in range(x):
            self.TheBoard[i] = [0] * y
        for a in range (0,10):
            for b in range (0,10):
                if ((a%2) == 0 and (b%2) == 0):
                    self.TheBoard[a][b] = Coordinate("black")
                elif ((a%2) == 0 and (b%2) == 1):
                    self.TheBoard[a][b] = Coordinate("white")
                elif ((a%2) == 1 and (b%2) == 1):
                    self.TheBoard[a][b] = Coordinate("black")
                elif ((a%2) == 1 and (b%2) == 0):
                    self.TheBoard[a][b] = Coordinate("white")

    # Getter that returns an object of type coordinate
    def getCoordinate(self, row, column):
        return self.TheBoard[row][column]

    # Method that updates the board
    def updateBoard(self, x, y, player):
        self.TheBoard[x][y].setOwner(player)
        return self



    # Method that prints a certain field on a board
    def printCertainField(self, row, column):
        print(self.TheBoard[row][column])

    # Method that prints the colors on the board
    # NOTE: MIGHT NOT BE NEEDED
    def printBoardColors(self):
        for i in range(0,10):
            for j in range(0,10):
                value = self.TheBoard[i][j]
                if self.TheBoard[i][j].getColor() == "black":
                    print('{:^1}'.format('B'), end = '')
                elif self.TheBoard[i][j].getColor() == "white":
                    print('{:^1}'.format('W'), end = '')
                else:
                    temp = self.TheBoard[i][j].getColor()
                if j != 9:
                    print(" -> ", end = '')
            print()

    # NOTE: MIGHT NOT BE NEEDED
    def printBoardWithTokens(self):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.TheBoard[i][j].getOwner().getName() != "null":
                    print('{:^1}'.format('*'), end='')
                elif self.TheBoard[i][j].getColor() == "black":
                    print('{:^1}'.format('B'), end = '')
                elif self.TheBoard[i][j].getColor() == "white":
                    print('{:^1}'.format('W'), end='')
                if j != 9:
                    print(" -> ", end='')
            print()

    # NOTE: MIGHT NOT BE NEEDED
    def printBoardOnlyTokens(self):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.TheBoard[i][j].getOwner().getName() != "null": ## Should be fixed based off the player
                    print('{:^1}'.format('*'), end='')
                else:
                    print('{:^1}'.format('-'), end='')
                if j != 9:
                    print(" -> ", end='')
            print()
