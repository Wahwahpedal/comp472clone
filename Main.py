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
startGame.chooseToken()
startGame.getBoard().printBoardOnlyTokens()
print("Player1 now has", newGame.getPlayer1().getTokens())