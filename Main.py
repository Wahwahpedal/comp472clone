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
#newGame = startGame.placeToken(1,2,1)
# newBoard = newGame.getBoard()
#newCoordinate = newBoard.returnCoordinate(1,2)
# owner = newcoordinate.getowner()
# print(owner.getname(), "testing to see if correct owner prints")
# print("new owner is", newcoordinate.getowner().getname())
# print(firstplayer.getfirstmove(), "shoud be no")
# nextround = newgame.placetoken(0,4,1)
# newboard = nextround.getboard()
# coordinatex = board.returncoordinate(0,1)
# print(type(coordinatex.getowner()))
# ownerx = coordinatex.getowner()
# print("new owner is", coordinatex.getowner().getname())
# startgame.getboard().printboardonlytokens()
# print("player1 now has", newgame.getplayer1().gettokens())

print("Round1")
newGame = startGame.placeToken(1)
newGame.getBoard().printBoardOnlyTokens()

print("=======")

print("Round 2")
newGame = newGame.placeToken(1)
newGame.getBoard().printBoardOnlyTokens()


