#import numpy
#import Coordinate

class Board:
    from Coordinate import Coordinate
    from Player import Player

    # Constructor that initializes the board to be a 2D-Array of type coordinates
    def __init__ (self):
        from Coordinate import Coordinate
        self.y = 10
        self.x = 12
        self.TheBoard = [0] * self.x
        for i in range(self.x):
            self.TheBoard[i] = [0] * self.y
        for a in range (0,self.x):
            for b in range (0,self.y):
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
    def updateBoardWithPlayer(self, x, y, player):
        self.TheBoard[x][y].setOwner(player)
        return self

    # Method that prints a certain field on a board
    def printCertainField(self, row, column):
        print(self.TheBoard[row][column])

    # Method that prints the colors on the board
    # NOTE: MIGHT NOT BE NEEDED
    def printBoardColors(self):
        for i in range(0,self.x):
            for j in range(0,self.y):
                value = self.TheBoard[i][j]
                if self.TheBoard[i][j].getColor() == "black":
                    print('{:^3}'.format('B'), end = '')
                elif self.TheBoard[i][j].getColor() == "white":
                    print('{:^3}'.format('W'), end = '')
                else:
                    temp = self.TheBoard[i][j].getColor()
                if j != 9:
                    print(" -> ", end = '')
            print()

    # NOTE: MIGHT NOT BE NEEDED
    def printBoardWithTokens(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                if self.TheBoard[i][j].getOwner().getName() != "null":
                    print('{:^3}'.format('*'), end='')
                elif self.TheBoard[i][j].getColor() == "black":
                    print('{:^3}'.format('B'), end = '')
                elif self.TheBoard[i][j].getColor() == "white":
                    print('{:^3}'.format('W'), end='')
                if j != 9:
                    print(" -> ", end='')
            print()

    # NOTE: MIGHT NOT BE NEEDED
    def printBoardOnlyTokens(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                if self.TheBoard[i][j].getOwner().getName() != "null": ## Should be fixed based off the player
                    print('{:^3}'.format('*'), end='')
                else:
                    print('{:^3}'.format('-'), end='')
                if j != 9:
                    print(" -> ", end='')
            print()
