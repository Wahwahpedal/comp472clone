#import numpy
#import Coordinate

class Board:
    from Coordinate import Coordinate
    from Player import Player

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

    def printFullBoard(self):
        print(self.TheBoard)

    def printCertainField(self, row, column):
        print(self.TheBoard[row][column])

    def returnCoordinate(self,row, column):
        return self.TheBoard[row][column]

    def updateBoard(self, x, y, player):
        self.TheBoard[x][y].setOwner(player)
        return self

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
