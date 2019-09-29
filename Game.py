class Game:
    from Board import Board
    from Player import Player

    def __init__ (self, name1=None, name2 = None):
        from Board import Board
        from Player import Player
        self.theBoard = Board()
        self.Player1 = Player(name1)
        self.Player2 = Player(name2)

    def printTheBoard(self):
        print(self.theBoard.printFullBoard())

    def printTheField(self, row, column):
        print(self.theBoard.printCertainField(row, column))

    def getBoard(self):
        return self.theBoard

    def updateBoard(board = Board()):
        self.theBoard = board

    def updateGame(self, x, y, value):
        self.theBoard = self.getBoard()
        templPlayer = self.returnPlayer1()
        self.Player1 = templPlayer
        if value == 1:
            self.theBoard  = self.theBoard.updateBoard(x,y,self.Player1)
        elif value == 2:
            templPlayer = game.returnPlayer2()
            self.Player2 = templPlayer
            self.theBoard  = updateBoard(x,y,self.Player2)
        if templPlayer.getFirstMove() == True:
            templPlayer.toggleFirstMove()
        return self

    def returnPlayer1(self):
        return self.Player1

    def returnPlayer2(self):
        return self.Player2

    def setPlayer1(self, player=Player()):
        self.Player1 = player

    def setPlayer2(self, player=Player()):
        self.Player2 = player

    def chooseToken(self):
        value = input("Enter the position where you want to place your token: ")
        length = len(value)
        while (length != 2):
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

    def placeToken(self, x, y, value):
        board = self.getBoard()
        theCoordinates = board.returnCoordinate(x,y)
        owner = theCoordinates.getOwner()
        print(theCoordinates.getOwner().getName())
        if value == 0:
            thePlayer = self.Player1
        else:
            thePlayer = self.Player2
        if (thePlayer.getFirstMove() == True) and (owner.getName() == 'null'):
            theGame =self.updateGame(x,y,value)
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
            if (corner1x >= 0 and corner1y >= 0):
                coordinateToVerify = board.returnCoordinate(corner1x,corner1y)
                owner = coordinateToVerify.getOwner()
                if owner == thePlayer:
                    theGame = self.updateGame(x,y,value)
            if (corner2x >= 0 and corner2y >= 0):
                coordinateToVerify = board.returnCoordinate(corner2x,corner2y)
                owner = coordinateToVerify.getOwner()
                if owner == thePlayer:
                    theGame = self.updateGame(x,y,value)
            if (corner3x >= 0 and corner3y >= 0):
                coordinateToVerify = board.returnCoordinate(corner3x,corner3y)
                owner = coordinateToVerify.getOwner()
                if owner == thePlayer:
                    theGame = self.updateGame(x,y,value)
            if (corner4x >= 0 and corner4y >= 0):
                print("TESTING")
                coordinateToVerify = board.returnCoordinate(corner4x,corner4y)
                owner = coordinateToVerify.getOwner()
                if owner == thePlayer:
                    theGame = self.updateGame(x,y,value)
            return theGame


#from Board import Board
from Game import Game
#from Player import Player
startGame = Game("PlayerOne","PlayerTwo") #type game
board = startGame.getBoard()
firstPlayer = startGame.returnPlayer1()
secondplayer = startGame.returnPlayer2()
startGame.getBoard().printBoardColors()

print("=====")

# #This is for testing
newGame = startGame.placeToken(1,2,1)
newBoard = newGame.getBoard()
newCoordinate = newBoard.returnCoordinate(1,2)
owner = newCoordinate.getOwner()
print(owner.getName(), "testing to see if correct owner prints")
print("New owner is", newCoordinate.getOwner().getName())
print(firstPlayer.getFirstMove(), "shoud be no")
nextRound = newGame.placeToken(0,4,1)
newBoard = nextRound.getBoard()
coordinateX = board.returnCoordinate(0,1)
print(type(coordinateX.getOwner()))
ownerX = coordinateX.getOwner()
print("New owner is", coordinateX.getOwner().getName())
value = input("Enter the position where you want to place your token: ")
startGame.chooseToken()
