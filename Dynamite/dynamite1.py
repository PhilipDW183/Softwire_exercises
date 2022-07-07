import random
import math

class ChaosBot:
    def __init__(self):
        self.choices = ["R", "P", "S", "W", "D"]
        self.base_choices = ["R", "P", "S"]
        self.dynamites_used = 0
        self.win = {"R":"P",
                    "S":"R",
                    "P":"S",
                    "W":"R",
                    "D":"W"}

    def use_dynamite(self):
        self.dynamites_used += 1

    def check_for_duplicates(self, list_to_check):

        empty_set = set()
        for pattern in list_to_check:
            if pattern in empty_set:
                return pattern
            else:
                empty_set.add(pattern)

        return None

    def opponents_pattern_response(self, last_10_moves):

        opponents_pattern_2 = set(last_10_moves[-2:])
        if len(opponents_pattern_2) == 1:
            opponents_tactic = opponents_pattern_2.pop()
            return self.win[opponents_tactic]

        patterns = []

        for pattern_length in range(3, 6):
            start = 0
            end = pattern_length - 1
            while end < 10:
                patterns.append(last_10_moves[start, end+1])
                start += 1
                end += 1

        pattern = self.check_for_duplicates(patterns)

        if not pattern:
            return None
        else:
            return self.win[pattern[0]]


    def make_move(self, gamestate):
        rounds = len(gamestate["rounds"])

        if rounds > 10:
            last_10_moves = gamestate["rounds"][-10:]
            opponents_last_10_moves = [move["p2"] for move in last_10_moves]

        if len(gamestate["rounds"]) <= 10:
            self.use_dynamite()
            return "D"
        else:

            opponents_pattern = set(opponents_last_10_moves[-2])
            if len(opponents_pattern) == 1:
                opponents_tactic = opponents_pattern.pop()
                return self.win[opponents_tactic]

            else:

                if self.dynamites_used < 100:
                    self.use_dynamite()
                    return "D"
                else:
                    return random.choice(self.base_choices)



