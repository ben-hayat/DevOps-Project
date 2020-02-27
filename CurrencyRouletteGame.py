import random
import requests

class CurrencyRouletteGame:
    def __init__(self, diff=1, debug=0):
        self.difficulty = diff
        self.debug = debug

    def get_difficulty(self):
        return self._difficulty

    def set_difficulty(self, value):
        if value < 1:
            raise ValueError("difficulty must be grater then 0 ")
        self._difficulty = value

    def get_money_interval(self,sum):
        # Get Exchange rate
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        # Making our request
        response = requests.get(url)
        _usd_exchange = response.json()

        if self.debug:
            print("The current exchange USD2ILS is: {rate}".format(rate=_usd_exchange.get('rates').get('ILS')))
        sum = sum * _usd_exchange.get('rates').get('ILS')
        return [sum-(5-self.difficulty),sum+(5-self.difficulty)]

    def get_guess_from_user (self,sum):
        _guess_input = input("Please guess the value (in ILS) of {_sum}) :".format(_sum=sum))
        try:
            return float(_guess_input)
        except:
            return 0

    def play(self):
        money = random.randint(1, 100)
        interval = self.get_money_interval(money)
        u_guess = self.get_guess_from_user(money)
        if self.debug:
            print("Guess is:{u_g}, Interval is:{p_int}".format(u_g=u_guess,p_int=interval))
        if u_guess > interval[0] and u_guess < interval[1]:
            return True
        else:
            return False

    difficulty = property(get_difficulty,set_difficulty)

def debug():
    game = CurrencyRouletteGame(3)
    if game.play():
        print ("Wow, Correct !")
    else:
        print ("Nope, you are wrong !")

#debug()