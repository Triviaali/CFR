from ..Models.ArrayMethods import ArrayMethods
import random

am = ArrayMethods()

class TestArrayMethods:
    def test_clip(self):
        test_list = []
        for x in range(150):
            test_list.append(-(random.random()))

        clipped_list = am.clip(test_list, 0.0)
        onlyZeroes = all(num == 0.0 for num in clipped_list)

        assert onlyZeroes == True

    def test_zeros(self):
        onlyZeroes = all(num == 0.0 for num in am.zeros(100))
        assert onlyZeroes

    def test_sum(self):
        sumTest = [1 for x in range(10)]
        assert am.sum(sumTest) == 10

    def test_repeat(self):
        element = 5
        lista = am.repeat(element, 5)
        assert all(num == 5 for num in lista) and len(lista) == 5

    def test_arrayAdd(self):
        array_one = [1, 1, 1]
        array_two = [2, 2, 2]
        assert all(num == 3 for num in am.arrayAdd(array_one, array_two))

    def test_divideAll(self):
        array_one = [4, 4, 4]
        assert all(num == 2 for num in am.divideAll(array_one, 2))

    def test_arrayMultiply(self):
        array1 = array2 = [2, 2, 2]
        assert all(num == 4 for num in am.arrayMultiply(array1, array2))

    def test_multiplyAll(self):
        array2 = [2, 2, 2]
        assert all(num == 10 for num in am.multiplyAll(array2, 5))


    def test_substractAll(self):
        array_one = [4, 4, 4]
        assert all(num == 1 for num in am.substractAll(array_one, 3))

    def test_columnAsList(self):
        payoffMatrix = [[0, -1, 1],
                        [1, 0, -1],
                        [-1, 1, 0]]
        column_one = am.getColumnAsList(payoffMatrix, 0)
        column_two = am.getColumnAsList(payoffMatrix, 1)
        column_three = am.getColumnAsList(payoffMatrix, 2)
        assert column_one == [0, 1, -1] and column_two == [-1, 0, 1] and column_three == [1, -1, 0]
