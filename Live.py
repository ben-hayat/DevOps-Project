from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame

def welcome(name):
    return "Hello {print_name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play\n".format(print_name=name)

def load_game():
    game = 0
    while (game < 1 or game > 3):
        _game_input = input("Please choose a game to play:\n\t"
           "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\t"
           "2. Guess Game - guess a number and see if you chose like the computer\n\t"
           "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        if _game_input.isnumeric():
            game = int(_game_input)

    difficulty = 0
    while (difficulty < 1 or difficulty > 5):
        _difficulty_input = input("Please choose game difficulty from 1 to 5:")
        if _difficulty_input.isnumeric():
            difficulty = int(_difficulty_input)

    if game == 1:
        game = MemoryGame(difficulty)
    elif game == 2:
        game = GuessGame(difficulty)
    elif game == 3:
        game = CurrencyRouletteGame(difficulty)

    if game.play():
        print("Wow, Correct !")
    else:
        print("Nope, you are wrong !")

def debug ():
    n = input("Please insert name:")
    print(welcome(n))
    load_game()