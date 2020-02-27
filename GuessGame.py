import random

class GuessGame:
    def __init__(self, diff=1, debug=0):
        self.difficulty = diff
        self.secret_number = 1
        self.debug = debug

    def get_difficulty(self):
        return self._difficulty

    def set_difficulty(self, value):
        if value < 1:
            raise ValueError("difficulty must be grater then 0 ")
        self._difficulty = value

    def get_secret_number(self):
        return self._secret_number

    def set_secret_number(self, value):
        if value < 1:
            raise ValueError("Number must be grater then 0 ")
        self._secret_number = value

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)
        if (self.debug):
            print ("Generated : {rand}".format(rand=self.secret_number))

    def get_guess_from_user(self):
        guess = 0
        while (guess < 1 or guess > self.difficulty):
            _guess_input = input("Random number in range (1-{diff}) was selected, try guess it: ".format(diff=self.difficulty))
            if _guess_input.isnumeric():
                guess = int(_guess_input)
        return guess

    def compare_results(self,to_compare):
        return to_compare == self.secret_number

    def play(self):
        self.generate_number()
        return self.compare_results(self.get_guess_from_user())

    difficulty = property(get_difficulty,set_difficulty)
    secret_number = property(get_secret_number,set_secret_number)

def debug():
    game = GuessGame(4,1)
    if game.play():
        print ("Correct !")
    else:
        print ("Wrong guess !")

#debug()