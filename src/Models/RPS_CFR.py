import random
from .DataStructures import SuperArray, RPSInfo


class Player:
    def __init__(self, name):
        self.name = name
        self.ACTIONS = 3

        self.regret_sum: SuperArray
        self.regret_sum = SuperArray(3)

        self.strategy: SuperArray
        self.strategy = SuperArray(3)

        self.strategy_sum: SuperArray
        self.strategy_sum = SuperArray(3)

    def __repr__(self):
        return self.name

    def get_strategy(self):
        # Gives a strategy profile for one iteration.

        # Remove negatives since we dont want to choose those as action.
        self.strategy.clip(0.0)

        normalizing_sum = self.strategy.sum()

        if normalizing_sum > 0.0:
            # Normalize
            self.strategy /= normalizing_sum
        else:
            # If normalizing sum negative play uniform distribution strategy.
            self.strategy.repeat(1 / 3, self.ACTIONS)

        # Add strategy profile to cumulative strategy sum.
        self.strategy_sum += self.strategy

    def regret(self, my_action, opp_action):
        # Count the regret sums for each action based on regret matching.
        result = RPSInfo.utilityFunc[my_action][opp_action]

        # Get a column from RPSInfo.utilityFunc
        array = RPSInfo.return_column(opp_action)
        # Substract result from all indexes of actual
        array -= result
        # Add calculated regret to total regret_sum
        self.regret_sum += array

    def get_action(self, strategy):
        # Get action from strategy profile
        random_float = random.random()
        action_to_be_chosen = 0
        cumul_probability = 0.0
        while (action_to_be_chosen < self.ACTIONS - 1):
            cumul_probability += strategy[action_to_be_chosen]
            if (random_float < cumul_probability):
                break
            action_to_be_chosen += 1

        return action_to_be_chosen

    def get_average_strategy(self):
        # Get average mixed strategy across all training iterations
        normalizing_sum = self.strategy_sum.sum()
        if normalizing_sum > 0.0:
            self.strategy_sum /= normalizing_sum
        else:
            self.strategy_sum.repeat(1 / 3, self.ACTIONS)

        return self.strategy_sum


class Trainer:
    def __init__(self):
        self.p1 = Player('Nash')
        self.p2 = Player('Equilibrium')
        self.num_wins = {
            self.p1: 0,
            self.p2: 0,
            'Draw': 0
        }

    def winner(self, a1, a2):
        result = RPSInfo.utilityFunc[a1][a2]
        if result == 1:
            return self.p1
        elif result == -1:
            return self.p2
        else:
            return 'Draw'

    def play(self, iterations):
        for i in range(iterations):
            self.p1.get_strategy()
            self.p2.get_strategy()
            a1 = self.p1.get_action(self.p1.strategy)
            a2 = self.p2.get_action(self.p2.strategy)
            self.p1.regret(a1, a2)
            self.p2.regret(a2, a1)

            winner = self.winner(a1, a2)
            self.num_wins[winner] += 1

        print('= Number of wins for each player = ')
        print(self.num_wins)
        print('= Strategy from average regret-matching = ')
        return self.conclude()

    def conclude(self):
        avg_strat_p1 = self.p1.get_average_strategy()
        avg_strat_p2 = self.p2.get_average_strategy()
        print("Player 1 strategy: ", avg_strat_p1)
        print("Player 2 strategy: ", avg_strat_p2)
        return [avg_strat_p1, avg_strat_p2]
