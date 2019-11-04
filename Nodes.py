# This class will be used for creating the boards to analyze the depths
from Board import Board
from Player import Player
import numpy


class TreeNodes:
    def __init__(self, board=Board(), oponentPlayer = Player(), computerPlayer = Player()):
        self.parentBoard = board.cloneBoard()
        self.childrenBoards = []
        self.opponentPlayer = oponentPlayer
        self.computerPlayer = computerPlayer


    def generateChildren(self, depth):
        if depth <= 0:
            return
        if depth == 1:
            player = self.computerPlayer
        elif depth == 2:
            player = self.opponentPlayer
        for i in range(0, 12):
            for j in range(0, 10):
                if self.parentBoard.getCoordinate(i,j).getOwner().getName() == "null":
                    tempBoard = self.parentBoard
                    self.childrenBoards.append(tempBoard.updateBoardWithPlayer(i, j, player))
        print(len(self.childrenBoards)) #NOTE: USED FOR TESTING
        #for i in len(self.childrenBoards)): #NOTE: Need to figure this out with another depth
            #self.GenerateChildren(depth - 1);

    def calculateScore(self, childBoard, index, player = Player()):  #Used to calculate the score of the board but store it in the children's trees
        xCoordinate = self.childrenBoards[index].getCoordinate()
        totalPoints = 0
        for i in range(0, 12):
            for j in range(0, 10):
                if childBoard[index].getCoordinate(i,j).getOwner().getName() == player.getName():
                    totalPoints = totalPoints + 5 #This is used just for testing at the moment
        return totalPoints










