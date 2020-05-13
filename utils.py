from os import system, name

SCORES_FILE_NAME = "Scores.txt"
# A number representing a bad return code for a function.
BAD_RETURN_CODE = 99
# A function to clear the screen (useful when playing memory game or before a new game starts).
def Screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def debug ():
    n = input("Please insert name:")
    print("Hello {print_name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play\n".format(print_name=n))
    Screen_cleaner()
    n = input("did you see the Welcome message ?")

#debug()