from src.RPS import RPS

ROCK = 0
PAPER = 1
SCISSORS = 2

RPStrainer = RPS([0.5, 0.5, 0])


class TestRPS:
    def test_get_action(self):
        strategy = [0.5, 0.5, 0]
        frequencies = {}
        iterations = 10000
        for i in range(iterations):
            res = RPStrainer.get_action(strategy)
            if res not in frequencies:
                frequencies[res] = 1
            else:
                frequencies[res] += 1

        assert 2 not in frequencies
        suhde = frequencies[0]/frequencies[1]
        assert suhde > 0.96 and suhde < 1.04

    def test_get_action_two(self):
        strategy = [0.33, 0.33, 0.34]
        frequencies = {}
        iterations = 100000
        for i in range(iterations):
            res = RPStrainer.get_action(strategy)
            if res not in frequencies:
                frequencies[res] = 1
            else:
                frequencies[res] += 1

        marginaalinSisalla = True
        for freq in frequencies:
            suhde = frequencies[freq]/100000
            if suhde < 0.32 or suhde > 0.35:
                marginaalinSisalla = False
                print(suhde)

        assert marginaalinSisalla

    def test_end_result(self):
        strat = [0.5, 0.25, 0.25]
        RPStrainer = RPS(strat)
        RPStrainer.train(10000)
        end_result = RPStrainer.get_average_strategy()
        assert end_result[0] < 0.015 and end_result[1] > 0.97 and end_result[2] < 0.015

    def test_end_result_two(self):
        strat = [0.2, 0.6, 0.2]
        RPStrainer = RPS(strat)
        RPStrainer.train(10000)
        end_result = RPStrainer.get_average_strategy()
        assert end_result[0] < 0.015 and end_result[1] < 0.015 and end_result[2] > 0.97