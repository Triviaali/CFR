import pytest

from ..Models.KUHNS_CFR import KuhnsPokerCFR, InformationSet
#
# kuhn = KuhnsPokerCFR()
# game_tree = kuhn.run(1000)
#
# class TestKuhns:
#     def test_right_amount_of_iterations(self):
#         iterations = 0
#         for _, info_set in game_tree.items():
#             iterations += info_set.iterations
#         assert iterations == 24000
#
#     def test_right_amount_of_nodes(self):
#         assert len(game_tree) == 12


class Test_InformationSet:
    @pytest.fixture
    def clean_info_set(self):
        info_set = InformationSet('rr')
        return info_set

    def test_init(self, clean_info_set):
        assert clean_info_set.key == 'rr'
        assert clean_info_set.strategy[0] == 0.5 and clean_info_set.strategy[1] == 0.5


    def test_next_strategy(self, clean_info_set):
        clean_info_set.reach_prob = 1
        clean_info_set.next_strategy()

        assert clean_info_set.strategy_sum[0] == 0.5 and clean_info_set.strategy_sum[1] == 0.5

    def test_get_strategy(self,clean_info_set):
        clean_info_set.regret_sum[0] = 1
        clean_info_set.regret_sum[1] = -0.5

        strategy = clean_info_set.get_strategy()
        assert strategy[0] == 1 and strategy[1] == 0

    def test_get_average_strategy(self, clean_info_set):
        clean_info_set.strategy_sum[0] = 1
        clean_info_set.strategy_sum[1] = 1
        clean_info_set.reach_prob_sum = 2

        strat = clean_info_set.get_average_strategy()

        assert strat[0] == 0.5 and strat[1] == 0.5