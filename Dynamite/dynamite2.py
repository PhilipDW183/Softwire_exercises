import random
import math

class ReverseLogicBot:
    def __init__(self):
        self.choices = ["R", "P", "S", "W", "D"]
        self.base_choices = ["R", "P", "S"]
        self.dynamites_used = 0
        self.win = {"R":"P",
                    "S":"R",
                    "P":"S",
                    "W":"R",
                    "D":"W"}
        self.lose = {"R":"P",
                     "P":"S",
                     "S":"R"}

    def use_dynamite(self):
        self.dynamites_used += 1

    def make_move(self, gamestate):
        rounds = len(gamestate["rounds"])

        if rounds < 5:
            return "D"

        opponents_last_move = gamestate["rounds"][-1]["p2"]

        last_2_moves = gamestate["rounds"][-2:]
        opponents_last_2_moves = [move["p2"] for move in last_2_moves]

        opponents_pattern = set(opponents_last_2_moves)

        if len(opponents_pattern) == 1:
            opponents_move = opponents_pattern.pop()
            return self.win[opponents_move]

        if opponents_last_move == "D" and self.dynamites_used < 100:
            self.use_dynamite()
            return "D"

        return self.win[self.lose[opponents_last_move]]



