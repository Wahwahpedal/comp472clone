# This class will be used for creating the boards to analyze the depths
from Board import Board
from Player import Player
import numpy as np


class Nodes:
    def __init__(self, game, board = Board(), oponentPlayer = Player(), computerPlayer = Player(),  x= 0, y = 0):
        self.parentBoard = board.cloneBoard()
        self.childrenBoards = "null"
        self.opponentPlayer = oponentPlayer
        self.computerPlayer = computerPlayer
        self.value = 0
        self.xvalue = x
        self.yvalue = y
        self.game = game

    def limitSearchSpace(self, buffer=1):
        if (self.game.rectangleCoordinates[0] - buffer) < 0:
            minX = 0
        else:
            minX = self.game.rectangleCoordinates[0] - buffer

        if (self.game.rectangleCoordinates[1] + buffer) > 11:
            maxX = 12
        else:
           maxX = self.game.rectangleCoordinates[1] + buffer + 1

        if (self.game.rectangleCoordinates[2] - buffer) < 0:
            minY = 0
        else:
            minY = self.game.rectangleCoordinates[2] - buffer

        if (self.game.rectangleCoordinates[3] + buffer) > 9:
            maxY = 10
        else:
            maxY = self.game.rectangleCoordinates[3] + buffer + 1

        print("Rectangle")
        print(self.game.rectangleCoordinates)

        arr = [minX, maxX, minY, maxY]
        return arr

    def generateChildren(self, depth):
        if depth <= 0:
            return
        arr = self.limitSearchSpace(depth)  # MAY WANT TO CHANGE BUFFER
        print("THIS IS THE RECTANGLE BOUNDARIES")   # Testing
        print(arr)  # Testing
        if depth == 1:
            player = self.computerPlayer
        elif depth == 2:
            player = self.opponentPlayer
        for i in range(arr[0],arr[1]):
            for j in range(arr[2], arr[3]):
                if self.parentBoard.getCoordinate(i,j).getOwner().getName() == "null":
                    self.childrenBoards = Nodes(self.game, self.parentBoard.updateBoardWithPlayer(i, j, player), self.opponentPlayer, self.computerPlayer, i, j)


        #for i in len(self.childrenBoards)): #NOTE: Need to figure this out with another depth
            #self.GenerateChildren(depth - 1);

    def calculateScore(self, childBoard, index, depth, player = Player()):  #Used to calculate the score of the board
        arr = self.limitSearchSpace(depth)  # MAY WANT TO CHANGE BUFFER
        # xCoordinate = self.childrenBoards[index].getCoordinate()
        totalPoints = 0
        for i in range(arr[0], arr[1]):
            for j in range(arr[2], arr[3]):
                if childBoard[index].getCoordinate(i,j).getOwner().getName() == player.getName():
                    totalPoints = totalPoints + 5 #This is used just for testing at the moment
        return totalPoints

    def isPieceTouching(self, x, y, player=Player()):
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


        #check topLeft, #check topRight, #checkBottomLeft, #checkBottomRight










