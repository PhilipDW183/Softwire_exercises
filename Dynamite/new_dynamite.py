import random
import math

class DaBomb:

    def __init__(self):
        self.choices = ["R", "P", "S", "W", "D"]
        self.base_choices = ["R", "P", "S"]
        self.win = {"R":"P",
                    "S":"R",
                    "P":"S",
                    "W":"R",
                    "D":"W"}
        self.lose = {"R":"P",
                     "S":"R",
                     "P":"S",
                     "D":"W",
                     "W":"R"}
        self.dynamite_used = 0
        self.opponent_dynamite_used = 0
        self.draws = 0

    def check_opponent_play_to_lose(self, oponents_moves, my_moves):

        if oponents_moves[1] == self.lose[my_moves[0]] and oponents_moves[2] == self.lose[my_moves[1]]:
            return self.win[self.lose[my_moves[2]]]

        return None

    def check_opponent_play_to_win(self, oponents_moves, my_moves):

        if oponents_moves[1] == self.win[my_moves[0]] and oponents_moves[2] == self.win[my_moves[1]]:
            return self.win[self.win[my_moves[2]]]

        return None

    def check_opponent_playing_against_self(self, oponents_moves):

        if oponents_moves[1] == self.win[oponents_moves[0]] and oponents_moves[2] == self.win[oponents_moves[1]]:
            return self.win[self.win[oponents_moves[2]]]

        return None

    def check_opponent_losing_against_self(self, oponents_moves):
        if oponents_moves[1] == self.lose[oponents_moves[0]] and oponents_moves[2] == self.lose[oponents_moves[1]]:
            return self.win[self.lose[oponents_moves[2]]]

        return None


    def make_move(self, gamestate):

        rounds = len(gamestate["rounds"])

        if gamestate["rounds"]:
            if gamestate["rounds"][-1]["p2"] == "D":
                self.opponent_dynamite_used += 1

        if rounds <= 1:
            return random.choice(self.base_choices)

        if rounds > 2:
            last_3_moves = gamestate["rounds"][-3:]
            opponents_last_3_moves = [move["p2"] for move in last_3_moves]
            my_last_3_moves = [move["p1"] for move in last_3_moves]
            opponents_strategy = set(opponents_last_3_moves)

            if len(opponents_strategy) == 1:
                opponents_move = opponents_strategy.pop()
                return self.win[opponents_move]

            opponent_strat_1 = self.check_opponent_play_to_win(opponents_last_3_moves,
                                                             my_last_3_moves)
            opponent_strat_2 = self.check_opponent_play_to_lose(opponents_last_3_moves,
                                                              my_last_3_moves)
            opponent_strat_3 = self.check_opponent_losing_against_self(opponents_last_3_moves)
            opponent_strat_4 = self.check_opponent_playing_against_self(opponents_last_3_moves)

            opponent_strats = [opponent_strat_1, opponent_strat_2,
                               opponent_strat_3, opponent_strat_4]

            for strat in opponent_strats:
                if strat:
                    return strat

        if len(gamestate["rounds"]) > 1:

            if gamestate["rounds"][-1]["p2"] == gamestate["rounds"][-1]["p1"]:
                self.draws += 1
            else:
                self.draws = 0

        if self.draws >= 1:

            if self.opponent_dynamite_used < 100:
                prob = random.randint(1, 4)
                if prob == 4 and self.dynamite_used < 100:
                    self.dynamite_used += 1
                    return "D"
                else:
                    return random.choice(self.base_choices)

            elif self.dynamite_used < 100:
                self.dynamite_used += 1
                return "D"

        return random.choice(self.base_choices)