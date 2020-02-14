from .ArrayMethods import ArrayMethods

am = ArrayMethods()


class KuhnsPokerCFR:
    def run(self, iterations):
        game_tree = dict()
        expected_game_value = 0

        for x in range(iterations):
            expected_game_value += self.cfr(game_tree)
            information_set: InformationSet
            for _, information_set in game_tree.items():
                information_set.next_strategy()

        expected_game_value /= iterations
        value: InformationSet
        print(len(game_tree))
        self.display_results(expected_game_value, game_tree)

    def display_results(self, expected_value, game_tree):
        print(f"player 1 expected value: {expected_value}")
        print(f"player 2 expected value: {-1 * expected_value}")

        print()
        ## Strategies of both players are in the same map so gotta filter player 1 and player 2 based on actions.
        print('Player 1 Strategies:')
        player1_strats = []
        player2_strats = []
        sorted_tree = sorted(game_tree.items(), key=lambda x: x[0])
        for _, information_set in filter(lambda x: len(x[0]) % 2 == 0, sorted_tree):
            print(information_set, " Iterations: ", information_set.iterations)
            #player1_strats.append(information_set,)
        print()
        print('Player 2 Strategies:')
        for _, information_set in filter(lambda x: len(x[0]) % 2 == 1, sorted_tree):
            print(information_set, " Iterations: ", information_set.iterations)
            #player2_strats.append(information_set)


    def cfr(self, game_tree, prev_actions="", p1_card=-1.0, p2_card=-1.0, p1_reach_prob=1.0, p2_reach_prob=1.0,
            common_reach_prob=1.0):
        if prev_actions == "":
            return self.chance_util(game_tree)

        if self.is_terminal(prev_actions):
            return self.get_utility_at_terminal_node(prev_actions, p1_card, p2_card)

        actions = len(prev_actions)
        is_player_1 = actions % 2 == 0

        information_set: InformationSet
        information_set = self.get_information_set(game_tree, p1_card if is_player_1 else p2_card, prev_actions)

        ## Get the game tree node.
        strategy = information_set.strategy

        ## Update reach probability
        if is_player_1:
            information_set.reach_prob += p1_reach_prob
        else:
            information_set.reach_prob += p2_reach_prob

        ## CFR action utility for each action.

        action_utilities = am.zeros(2)

        for i, action in enumerate(["c", "b"]):
            next_action = prev_actions + action
            if is_player_1:

                action_utilities[i] = -1.0 * self.cfr(game_tree, next_action, p1_card, p2_card,
                                                      p1_reach_prob * strategy[i], p2_reach_prob, common_reach_prob)
            else:
                action_utilities[i] = -1.0 * self.cfr(game_tree, next_action, p1_card, p2_card, p1_reach_prob,
                                                      p2_reach_prob * strategy[i], common_reach_prob)

        util = am.sum(am.arrayMultiply(action_utilities, strategy))

        regrets = am.substractAll(action_utilities, util)
        if is_player_1:
            information_set.regret_sum = am.arrayAdd(information_set.regret_sum,
                                                     am.multiplyAll(regrets, p2_reach_prob * common_reach_prob))
        else:
            information_set.regret_sum = am.arrayAdd(information_set.regret_sum,
                                                     am.multiplyAll(regrets, p1_reach_prob * common_reach_prob))

        return util

    def chance_util(self, game_tree):
        expected_value = 0
        combinations_of_cards = 6  # JQ JK QJ QK KJ KQ
        for i in range(3):
            for j in range(3):
                if i != j:
                    expected_value += self.cfr(game_tree, "rr", i, j, 1, 1, (1 / 6))
        return expected_value / combinations_of_cards

    def is_terminal(self, prev_actions):
        ## Nodes that end with showdown
        terminal_nodes = ["rrcc", "rrcbc", "rrcbb", "rrbc", "rrbb"]
        return prev_actions in terminal_nodes

    def get_utility_at_terminal_node(self, prev_actions, p1_card, p2_card):
        actions = len(prev_actions)

        player_card = p1_card if actions % 2 == 0 else p2_card
        opponent_card = p2_card if actions % 2 == 0 else p1_card

        ## check and fold are the same so
        if prev_actions == "rrcbc" or prev_actions == "rrbc":
            ## last player folded. the current player wins.
            return 1
        elif prev_actions == "rrcc":
            ## Checked down so player with higher cards wins.
            if player_card > opponent_card:
                return 1
            else:
                return -1

        # Paths with check bet call or bet and a call.
        if prev_actions == "rrcbb" or prev_actions == "rrbb":

            if player_card > opponent_card:
                return 2
            else:
                return -2

    def get_information_set(self, game_tree, card, prev_actions):
        key = self.card_str(card) + " " + prev_actions

        information_set: InformationSet
        if key not in game_tree:
            information_set = InformationSet(key)
            game_tree[key] = information_set
            return information_set

        return game_tree[key]

    def card_str(self, card):
        if card == 0:
            return "J"
        elif card == 1:
            return "Q"
        return "K"


class InformationSet:
    def __init__(self, key):
        self.key = key
        self.regret_sum = am.zeros(2)
        self.strategy_sum = am.zeros(2)
        self.strategy = am.repeat((1 / 2), 2)
        self.reach_prob = 0
        self.reach_prob_sum = 0
        self.iterations = 0

    def __str__(self):
        strategies = ['{:03.2f}'.format(x)
                      for x in self.get_average_strategy()]
        return '{} {}'.format(self.key.ljust(6), strategies)

    def next_strategy(self):
        self.strategy_sum = am.arrayAdd(self.strategy_sum, am.multiplyAll(self.strategy, self.reach_prob))
        self.strategy = self.get_strategy()
        self.reach_prob_sum += self.reach_prob
        self.reach_prob = 0
        self.iterations += 1

    def get_strategy(self):
        strategy = am.clip(self.regret_sum, 0.0)
        normalizing_sum = am.sum(strategy)
        if normalizing_sum > 0.0:
            # Normalize
            strategy = am.divideAll(strategy, normalizing_sum)
        else:
            # uniform strategy distribution
            strategy = am.repeat((1 / 2), 2)
        self.iterations += 1
        return strategy

    def get_average_strategy(self):
        strategy = am.divideAll(self.strategy_sum, self.reach_prob_sum)

        normalizing_sum = am.sum(strategy)
        strategy = am.divideAll(strategy, normalizing_sum)

        return strategy
