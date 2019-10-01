#from Board import Board
from Game import Game
#from Player import Player
startGame = Game("PlayerOne","PlayerTwo") #type game
board = startGame.getBoard()
firstPlayer = startGame.getPlayer1()
secondplayer = startGame.getPlayer2()


# This is for testing
startGame.getBoard().printBoardColors()
print("=====")

print("Round1")
#startGame.placeToken()
startGame.playGame()
newGame.getBoard().printBoardOnlyTokens()

print("=======")

print("Round 2")
newGame = newGame.placeToken(1)
newGame.getBoard().printBoardOnlyTokens()


