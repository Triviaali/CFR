from ..Models.DataStructures import SuperArray


class TestSuperArray:
    def test_init(self):
        array = SuperArray(3)

        assert all([val == 0.0 for val in array])

    def test_set(self):
        array = SuperArray(4)
        array[0] = 1
        array[2] = 34234
        array[3] = 555

        assert array[0] == 1 and array[2] == 34234 and array[3] == 555 and array[1] == 0.0

    def test_add(self):
        array = SuperArray(3)
        array[0] = 1
        array[1] = 3
        array[2] = 5

        array += 5
        assert array[0] == 6 and array[1] == 8 and array[2] == 10

    def test_super_array_add(self):
        array = SuperArray(3)
        array[0] = 1
        array[1] = 3
        array[2] = 5

        array2 = SuperArray(3)
        array2[0] = 3
        array2[1] = 5
        array2[2] = 5

        array += array2
        assert array[0] == 4 and array[1] == 8 and array[2] == 10

    def test_mul(self):
        array = SuperArray(3)
        array[0] = 1
        array[1] = 3
        array[2] = 5

        array *= 5

        assert array[0] == 5 and array[1] == 15 and array[2] == 25

    def test_super_array_mul(self):
        array = SuperArray(3)
        array[0] = 1
        array[1] = 3
        array[2] = 5

        array2 = SuperArray(3)
        array2[0] = 3
        array2[1] = 5
        array2[2] = 5

        array *= array2
        assert array[0] == 3 and array[1] == 15 and array[2] == 25

    def test_sub(self):
        array = SuperArray(3)
        array[0] = 1
        array[1] = 3
        array[2] = 5

        array -= 1

        assert array[0] == 0 and array[1] == 2 and array[2] == 4

    def test_super_array_sub(self):
        array = SuperArray(3)
        array[0] = 1
        array[1] = 3
        array[2] = 5

        array2 = SuperArray(3)
        array2[0] = 3
        array2[1] = 5
        array2[2] = 5

        array -= array2
        assert array[0] == -2 and array[1] == -2 and array[2] == 0

    def test_div(self):
        array = SuperArray(3)
        array[0] = 5
        array[1] = 10
        array[2] = 15

        array /= 5

        assert array[0] == 1 and array[1] == 2 and array[2] == 3

    def test_super_array_div(self):
        array = SuperArray(3)
        array[0] = 55
        array[1] = 100
        array[2] = 15

        array2 = SuperArray(3)
        array2[0] = 5
        array2[1] = 10
        array2[2] = 1

        array /= array2

        assert array[0] == 11 and array[1] == 10 and array[2] == 15

    def test_clip(self):
        array = SuperArray(3)
        array[0] = -55
        array[1] = 100
        array[2] = -20

        array.clip(0)
        assert array[0] == 0 and array[1] == 100 and array[2] == 0

    def test_sum(self):
        array = SuperArray(3)
        array[0] = 55
        array[1] = 100
        array[2] = 15

        array.sum()

        assert array.sum() == 170

    def test_repeat(self):
        array = SuperArray(3)
        array.repeat(4 / 2, 3)

        assert all([value == 2 for value in array])
