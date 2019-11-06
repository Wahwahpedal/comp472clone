# This is the board class that creates the board for the game
from colorama import Fore, Back, Style
import copy


class Board:

    # Constructor that initializes the board to be a 2D-Array of type coordinates
    def __init__(self):
        from Coordinate import Coordinate
        x = 12
        y = 10
        self.TheBoard = [0] * x
        for i in range(x):
            self.TheBoard[i] = [0] * y
        for a in range(0, 12):
            for b in range(0, 10):
                if ((a % 2) == 0 and (b % 2) == 0):
                    self.TheBoard[a][b] = Coordinate("black")
                elif ((a % 2) == 0 and (b % 2) == 1):
                    self.TheBoard[a][b] = Coordinate("white")
                elif ((a % 2) == 1 and (b % 2) == 1):
                    self.TheBoard[a][b] = Coordinate("black")
                elif ((a % 2) == 1 and (b % 2) == 0):
                    self.TheBoard[a][b] = Coordinate("white")

    def cloneBoard(self):
        return copy.deepcopy(self)

    # Getter that returns an object of type coordinate
    def getCoordinate(self, row, column):
        return self.TheBoard[row][column]

    # Method that updates the board
    def updateBoardWithPlayer(self, x, y, player):
        self.TheBoard[x][y].setOwner(player)
        return self

    # MTesting for the nodes
    def updateTempBoard(self, x, y, player):
        return self.cloneBoard().getCoordinate(x, y).setOwner(player)



    # Method that prints a certain field on a board
    def printCertainField(self, row, column):
        print(self.TheBoard[row][column])

    # Method that prints the colors on the board
    def printBoardColors(self):
        y_axis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        for i in range(0, 12):
            print(Fore.RED + '\033[1m' + y_axis[i], end=" ")
            for j in range(0, 10):
                value = self.TheBoard[i][j]
                if self.TheBoard[i][j].getColor() == "black":
                    print(Fore.BLUE + '{:^3}'.format('B'), end='')
                elif self.TheBoard[i][j].getColor() == "white":
                    print(Fore.GREEN + '{:^3}'.format('W'), end='')
                else:
                    temp = self.TheBoard[i][j].getColor()
                if j != 9:
                    print(Style.RESET_ALL + " -> ", end='')
            print()
        print(
            Fore.RED + '\033[1m' + '    1       2     3      4      5      6      7      8      9     10' + Style.RESET_ALL)

