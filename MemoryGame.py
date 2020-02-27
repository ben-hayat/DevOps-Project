import random
import time

class MemoryGame:
    def __init__(self, diff=1, debug=0):
        self.difficulty = diff
        self.debug = debug

    def get_difficulty(self):
        return self._difficulty

    def set_difficulty(self, value):
        if value < 1:
            raise ValueError("difficulty must be grater then 0 ")
        self._difficulty = value

    def generate_sequence(self):
        rand_list = []
        for i in range(self.difficulty):
            rand_list.append(random.randint(1, 101))
        print ("Please remember the following generated : {rand}".format(rand=rand_list),end="")
        time.sleep(0.7)
        print("\rNow let hope you remember :)")
        return rand_list

    def get_list_from_user(self):
        user_list = []
        for i in range(self.difficulty):
            _item_input = input("item [{diff}] : ".format(diff=i))
            if _item_input.isnumeric():
                user_list.append(int(_item_input))
        if (self.debug):
            print("Received : {recv}".format(recv=user_list))
        return user_list

    def is_list_equal(self,list1,list2):
        for i in range(self.difficulty):
            if list1[i] != list2[i]:
                if (self.debug):
                    print ("No, its was : {the_list}".format(the_list=list1))
                return False
        return True

    def play(self):
        return self.is_list_equal(self.generate_sequence(),self.get_list_from_user())

    difficulty = property(get_difficulty,set_difficulty)

def debug():
    game = MemoryGame(3,1)
    if game.play():
        print ("Wow, Correct !")
    else:
        print ("Nope, you are wrong !")

#debug()