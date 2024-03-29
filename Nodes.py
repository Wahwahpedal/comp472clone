# This class will be used for creating the boards to analyze the depths
from Board import Board
from Player import Player
import numpy as np

class Nodes:

    def __init__(self, thegame, board, oponentPlayer, computerPlayer, x=0, y=0):
        self.parentBoard = board.cloneBoard()
        self.childrenBoards = "null"
        self.opponentPlayer = oponentPlayer
        self.computerPlayer = computerPlayer
        self.value = 0
        self.xvalue = x
        self.yvalue = y
        global game
        game = thegame
        self.counterForChildrenBoards = 0 #Not sure if this will be needed
        self.openList = np.array([])
        self.closedList = np.array([])

    def getGame(self):
        return game

    def getParentBoard(self):
        return self.parentBoard

    def getChildrenBoards(self):
        return self.childrenBoards

    def getValue(self):
        return self.value

    def limitSearchSpace(self, buffer=1):
        if (game.rectangleCoordinates[0] - buffer) < 0:
            minX = 0
        else:
            minX = game.rectangleCoordinates[0] - buffer

        if (game.rectangleCoordinates[1] + buffer) > 11:
            maxX = 12
        else:
            maxX = game.rectangleCoordinates[1] + buffer + 1

        if (game.rectangleCoordinates[2] - buffer) < 0:
            minY = 0
        else:
            minY = game.rectangleCoordinates[2] - buffer

        if (game.rectangleCoordinates[3] + buffer) > 9:
            maxY = 10
        else:
            maxY = game.rectangleCoordinates[3] + buffer + 1

        print("Rectangle")  # informative/debug
        print(game.rectangleCoordinates)  # informative/debug

        arr = [minX, maxX, minY, maxY]
        return arr

    def generateChildren(self, depth):
        if depth <= 0:
            return
        arr = self.limitSearchSpace(depth)  # MAY WANT TO CHANGE BUFFER
        print("THIS IS THE RECTANGLE BOUNDARIES")  # informative/debug
        print(arr)  # informative/debug
        if depth == 1:
            player = self.computerPlayer
        elif depth == 2:
            player = self.opponentPlayer
        #for i in range(0, 12):  # Used for testing until lines 66 and 67 are corrected
            # for j in range(0, 10): # Used for testing until lines 66 and 67 are corrected
        for i in range(arr[0],arr[1]):
            for j in range(arr[2], arr[3]):
                self.parentBoard = game.theBoard
                self.childrenBoards = "null"
                if self.parentBoard.getCoordinate(i, j).getOwner().getName() == "null":
                    tempBoard = game.theBoard.cloneBoard()
                    updatedBoard = tempBoard.updateBoardWithPlayer(i, j, player)
                    # print(game.printGameForBoard(updatedBoard)) Used for testing
                    self.childrenBoards = Nodes(game, updatedBoard, self.opponentPlayer, self.computerPlayer, i, j)
                    print(game.printGameForBoard(self.childrenBoards.getParentBoard()))  #Used for testing
                    self.counterForChildrenBoards = self.counterForChildrenBoards + 1 #Don't think this is needed but keeping it for testing at the moment
                    self.openList = (np.append(self.openList, self.childrenBoards)) # Creates an open list with the children
                    # self.game.updateGame(i, j, 1, False) # Testing purposes
                    # self.game.printGame() # Testing purposes

        print("======")
        #print(self.openList[1].getGame().printGame())
        self.calculateChildrenScores(1, self.computerPlayer) #Used for testing
        print("Maximum child is", self.getMaxOfChildren()) #Used for testing
        print("======")

        # for i in len(self.childrenBoards)): #NOTE: Need to figure this out with another depth
        # self.GenerateChildren(depth - 1);

    def calculateChildrenScores(self, depth, player):  # Used to calculate the score of the board, NOT determining min or max right now but need to
        arr = self.limitSearchSpace(depth)  # MAY WANT TO CHANGE BUFFER
        # xCoordinate = self.childrenBoards[index].getCoordinate()
        for index in self.openList: #Used to generate the heuristic value for each child
            totalPoints = 0
            # for i in range(0, 12):  # Used for testing until lines 66 and 67 are corrected
                # for j in range(0, 10):  # Used for testing until lines 66 and 67 are corrected
            for i in range(arr[0], arr[1]):
                for j in range(arr[2], arr[3]):
                    if index.getParentBoard().getCoordinate(i, j).getOwner().getName() == player.getName():
                        totalPoints = totalPoints + 5  # This is used just for testing at the moment
            # print("The total points are", totalPoints) Used for testing
            index.value = totalPoints

    def getMaxOfChildren(self):  # Function to be used to determine which child should be used when Max is playing
        maxChild = "null"
        maxValue = 0;
        for i in self.openList:
            if i.value > maxValue:
                maxChild = i
                maxValue = i.getValue()
        return maxChild

    # TO DO:
    # def updateGameWithChildChosen(self, maxChild): #Neds a method to update the game with the value chosen
        # return game.updateGame()

    def isPieceTouching(self, x, y, player):
        corner1x = x - 1
        corner1y = y - 1

        corner2x = x - 1
        corner2y = y + 1

        corner3x = x + 1
        corner3y = y - 1

        corner4x = x + 1
        corner4y = y + 1

        topLeftOwner = self.parentBoard.getCoordinate(corner1x, corner1y).getOwner().getName()
        topRightOwner = self.parentBoard.getCoordinate(corner2x, corner2y).getOwner().getName()
        bottomLeftOwner = self.parentBoard.getCoordinate(corner3x, corner3y).getOwner().getName()
        bottomRightOwner = self.parentBoard.getCoordinate(corner4x, corner4y).getOwner().getName()

        # check topLeft, #check topRight, #checkBottomLeft, #checkBottomRight
