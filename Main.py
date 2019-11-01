# This is the main class where the game is played
from colorama import Fore, Back, Style
from Game import Game


# Intro Message
print("Welcome to the X-Rudder Game!")


while True:
    version = input("Do you want to play with another person or a computer?. Type \"P\" for player or \"C\" for computer: ")
    if (version == "C") or (version == "c") or (version == "P") or (version == "p"):
        break
    else:
        print("Incorrect value entered, try again.")

if (version == "C") or (version == "c"):
    playerOneName = input("Enter your name: ")
    playerTwoName = "Computer"
    startGame = Game(playerOneName,playerTwoName) #Creating an object of type Game
    # Plays the game with the computer
    print("Here's the initial board:")
    startGame.getBoard().printBoardColors()
    print(Style.RESET_ALL + "=====")
    print("Let's get started!")
    #print(startGame.computerPlaceToken()) For testing
    startGame.playGameWithComputer() #Note: THIS METHOD NEEDS TO BE CHANGED FOR A COMPUTER

if (version == "P") or (version == "p"):
    playerOneName = input("Enter player one's name: ")
    playerTwoName = input("Enter player two's name: ")
    startGame = Game(playerOneName,playerTwoName) #Creating an object of type Game
    # Plays the game
    print("Here's the initial board:")
    startGame.getBoard().printBoardColors()
    print(Style.RESET_ALL + "=====")
    print("Let's get started!")
    startGame.playGame()

# Closing Message
print("Hope you had fun playing, goodbye!")
