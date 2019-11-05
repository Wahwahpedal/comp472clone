# This class will be used for creating the boards to analyze the depths
from Board import Board
from Player import Player
from Game import Game
import numpy


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


    def generateChildren(self, depth):
        if depth <= 0:
            return
        minX = self.game.rectangleCoordinates[0]
        maxX = self.game.rectangleCoordinates[1]
        minY = self.game.rectangleCoordinates[2]
        maxY = self.game.rectangleCoordinates[3]
        print(self.game.rectangleCoordinates)

        if depth == 1:
            player = self.computerPlayer
        elif depth == 2:
            player = self.opponentPlayer
        for i in range(minX, maxX):
            for j in range(minY, maxY):
                if self.parentBoard.getCoordinate(i,j).getOwner().getName() == "null":
                    self.childrenBoards = Nodes(self.game, self.parentBoard.updateBoardWithPlayer(i, j, player), self.opponentPlayer, self.computerPlayer, i, j)

        #for i in len(self.childrenBoards)): #NOTE: Need to figure this out with another depth
            #self.GenerateChildren(depth - 1);

    def calculateScore(self, childBoard, index, player = Player()):  #Used to calculate the score of the board
        # xCoordinate = self.childrenBoards[index].getCoordinate()
        totalPoints = 0
        for i in range(0, 12):
            for j in range(0, 10):
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










