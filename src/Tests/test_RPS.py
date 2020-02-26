from ..Models.RPS_CFR import Trainer

trainer = Trainer()

class TestRPS:
    def test_good_nash_equilibrium_approximation(self):
        ## Equilibrium for both players is to play exactly 1/3 of rock paper and scissors
        p1, p2 = trainer.play(100000)
        assert all(num > (1/3 -0.02) and num < (1/3 + 0.02) for num in p1)
        assert all(num > (1 / 3 - 0.02) and num < (1 / 3 + 0.02) for num in p2)

