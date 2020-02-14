from ..Models.KUHNS_CFR import KuhnsPokerCFR

kuhn = KuhnsPokerCFR()
game_tree = kuhn.run(1000)

class TestKuhns:
    def test_right_amount_of_iterations(self):
        iterations = 0
        for _, info_set in game_tree.items():
            iterations += info_set.iterations
        assert iterations == 24000

    def test_right_amount_of_nodes(self):
        assert len(game_tree) == 12