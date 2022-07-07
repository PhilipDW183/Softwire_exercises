import random

class RandomBot:

    def __init__(self):
        self.possible_moves = ["R", "P", "S"]
        self.dynamite_used = 0

    def make_move(self, gamestate):

        if len(gamestate["rounds"]) % 50 == 0 & self.dynamite_used < 100:
            self.dynamite_used += 1
            return "D"

        return random.choice(self.possible_moves)