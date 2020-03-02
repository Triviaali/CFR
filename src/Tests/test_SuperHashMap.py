from ..Models.DataStructures import SuperHashMap, SuperArray


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

        print(hashimappi.values())
        assert all([v in values for v in hashimappi.values()])

    def test_contains(self):
        hashimappi = SuperHashMap()

        hashimappi['rr'] = 1

        assert 'rr' in hashimappi
        assert 'abc' not in hashimappi

    def test_hash(self):
        hashimappi = SuperHashMap()
        hashes = []
        hashi = hashimappi.hash('J rr') % 16
        for x in range(10000):
            hashes.append(hashimappi.hash('J rr') % 16)

        assert all([hashi == x for x in hashes])

    def test_different_hashes(self):
        hashimappi = SuperHashMap()
        keys = ['J rr',
        'J rrcb',
        'K rr',
        'K rrcb',
        'Q rr',
        'Q rrcb',
        'J rrb',
        'J rrc',
        'K rrb',
        'K rrc',
        'Q rrb',
        'Q rrc']

        hashvalues = [hashimappi.hash(key) for key in keys]
        uniqueValues = list(set(list(hashvalues)))
        assert len(uniqueValues) == 12

    def test_different_hashes_different_indexes(self):
        hashimappi = SuperHashMap()
        keys = ['J rr',
        'J rrcb',
        'K rr',
        'K rrcb',
        'Q rr',
        'Q rrcb',
        'J rrb',
        'J rrc',
        'K rrb',
        'K rrc',
        'Q rrb',
        'Q rrc']

        hashvalues = [hashimappi.hash(key) % 47 for key in keys]
        uniqueValues = list(set(list(hashvalues)))
        assert len(uniqueValues) == 12

    def test_contains_in_map(self):
        hashimappi = SuperHashMap()
        keys = ['J rr',
        'J rrcb',
        'K rr',
        'K rrcb',
        'Q rr',
        'Q rrcb',
        'J rrb',
        'J rrc',
        'K rrb',
        'K rrc',
        'Q rrb',
        'Q rrc']

        for i, key in enumerate(keys):
            hashimappi[key] = i

        assert 'J rr' in hashimappi
        assert 'J rrcb' in hashimappi