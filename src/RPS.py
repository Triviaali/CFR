import random

ROCK = 0
PAPER = 1
SCISSORS = 2

class RPS:
    def __init__(self, opp_strategy):

        self.ACTIONS = 3
        self.regret_sum = [0.0, 0.0, 0.0]
        self.strategy = [0.0, 0.0, 0.0]
        self.strategySum = [0.0, 0.0, 0.0]

        self.opponent_strategy = opp_strategy

    def get_strategy(self):
        normalizingSum = 0.0
        for i in range(self.ACTIONS):
            if self.regret_sum[i] > 0.0:
                self.strategy[i] = self.regret_sum[i]
            else:
                self.strategy[i] = 0.0
            normalizingSum += self.strategy[i]

        for j in range(self.ACTIONS):
            if normalizingSum > 0.0:
                self.strategy[j] /= normalizingSum
            else:
                self.strategy[j] = 1.0 / self.ACTIONS

            self.strategySum[j] += self.strategy[j]

        return self.strategy

    def get_action(self, strategy):
        random_float = random.random()
        action_to_be_chosen = 0
        cumul_probability = 0.0
        while (action_to_be_chosen < self.ACTIONS - 1 ):
            cumul_probability += strategy[action_to_be_chosen]
            if (random_float < cumul_probability):
                break
            action_to_be_chosen += 1

        return action_to_be_chosen

    def train(self, iterations):
        action_utility = [0.0, 0.0, 0.0]
        for i in range(iterations):
            strategy = self.get_strategy()
            my_action = self.get_action(strategy)
            opp_action = self.get_action(self.opponent_strategy)

            action_utility[opp_action] = 0
            action_utility[0 if opp_action == self.ACTIONS - 1 else opp_action + 1] = 1
            action_utility[self.ACTIONS - 1 if opp_action == 0 else opp_action - 1] = -1

            for j in range(self.ACTIONS):
                self.regret_sum[j] += action_utility[j] - action_utility[my_action]

    def get_average_strategy(self):
        avg_strategy = [0.0, 0.0, 0.0]
        normalizing_sum = 0.0
        for i in range(self.ACTIONS):
            normalizing_sum += self.strategySum[i]

        for j in range(self.ACTIONS):
            if normalizing_sum > 0.0:
                avg_strategy[j] = self.strategySum[j] / normalizing_sum
            else:
                avg_strategy[j] = 1 / self.ACTIONS

        return avg_strategy

traineri = RPS([0.33, 0.33, 0.34])
traineri.train(1000000)
print(traineri.get_average_strategy())

