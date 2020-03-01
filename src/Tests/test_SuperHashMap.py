from ..Models.DataStructures import SuperHashMap, SuperArray, SuperNode


class TestSuperHashMap:
    def test_init(self):
        testi = SuperHashMap()

        assert isinstance(testi, type(SuperHashMap()))
        assert isinstance(testi.slots, type(SuperArray(0)))

    def test_set_and_get(self):
        key = 'rrbc'
        value = 55

        testi = SuperHashMap()
        testi[key] = value

        should_be_55 = testi[key]

        assert should_be_55 == 55

    def test_items(self):
        hashimappi = SuperHashMap()

        keys = ['rr', 'rrb', 'rrc', 'rrbc']
        values = [1, 2, 3, 4]

        hashimappi['rr'] = 1
        hashimappi['rrb'] = 2
        hashimappi['rrc'] = 3
        hashimappi['rrbc'] = 4

        assert all([k in keys and v in values for k, v in hashimappi.items()])

    def test_keys(self):
        hashimappi = SuperHashMap()

        keys = ['rr', 'rrb', 'rrc', 'rrbc']

        hashimappi['rr'] = 1
        hashimappi['rrb'] = 2
        hashimappi['rrc'] = 3
        hashimappi['rrbc'] = 4

        assert all([k in keys for k in hashimappi.keys()])

    def test_values(self):
        hashimappi = SuperHashMap()

        values = [1, 2, 3, 4]

        hashimappi['rr'] = 1
        hashimappi['rrb'] = 2
        hashimappi['rrc'] = 3
        hashimappi['rrbc'] = 4

        assert all([v in values for v in hashimappi.values()])