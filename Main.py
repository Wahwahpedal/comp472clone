# This is the main class where the game is played

from Game import Game
playerOneName = input("Enter player one's name: ")
playerTwoName = input("Enter player two's name: ")
startGame = Game(playerOneName,playerTwoName) #Creating an object of type Game

# Intro Message
print("Welcome to the X-Rudder Game! Here's the initial board:")
startGame.getBoard().printBoardColors()
print("=====")
print("Let's get started!")

# Plays the game
startGame.playGame()

# Closing Message
print("Hope you had fun playing, goodbye!")




