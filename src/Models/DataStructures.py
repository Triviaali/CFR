
class SuperArray:
    def __init__(self, length):
        self.inner_list = []
        self.length = length
        self.index = 0
        for x in range(length):
            self.inner_list.append(0.0)

    def __repr__(self):
        return str(self.inner_list)

    def __getitem__(self, index):
        return self.inner_list[index]

    def __setitem__(self, index, value):
        self.inner_list[index] = value

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_to_return = self[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return next_to_return

    def __add__(self, other):
        temp = self.inner_list
        if isinstance(other, float) or isinstance(other, int):
            for x in range(self.length):
                temp[x] = temp[x] + other
        elif isinstance(other, type(self)):
            if self.length != other.length:
                raise IndexError
            for x in range(self.length):
                temp[x] = temp[x] + other[x]
        else:
            raise ValueError

        self.inner_list = temp
        return self

    def __sub__(self, other):
        temp = self.inner_list
        if isinstance(other, float) or isinstance(other, int):
            for x in range(self.length):
                temp[x] = temp[x] - other
        elif isinstance(other, type(self)):
            if self.length != other.length:
                raise IndexError
            for x in range(self.length):
                temp[x] = temp[x] - other[x]
        else:
            raise ValueError

        self.inner_list = temp
        return self

    def __mul__(self, other):
        temp = self.inner_list
        if isinstance(other, float) or isinstance(other, int):
            for x in range(self.length):
                temp[x] = temp[x] * other
        elif isinstance(other, type(self)):
            if self.length != other.length:
                raise IndexError
            for x in range(self.length):
                temp[x] = temp[x] * other[x]
        else:
            raise ValueError

        self.inner_list = temp
        return self

    def __truediv__(self, other):
        temp = self.inner_list
        if isinstance(other, float) or isinstance(other, int):
            for x in range(self.length):
                temp[x] = temp[x] / other
        elif isinstance(other, type(self)):
            if self.length != other.length:
                raise IndexError
            for x in range(self.length):
                temp[x] = temp[x] / other[x]
        else:
            raise ValueError

        self.inner_list = temp
        return self

    def clip(self, minimium):
        temp = self.inner_list
        for x in range(self.length):
            if temp[x] < minimium:
                temp[x] = minimium

        self.inner_list = temp
        return self

    def sum(self):
        summa = 0
        for x in range(self.length):
            summa += self[x]

        return summa

    def repeat(self, value, times):
        self.inner_list = []
        for x in range(times):
            self.inner_list.append(value)
        return self

    def return_copy(self):
        copy = SuperArray(self.length)
        for x in range(self.length):
            copy[x] = self.inner_list[x]

        return copy

    def append(self, item):
        self.inner_list.append(item)
        self.length += 1


class SuperHashMap:
    def __init__(self):
        self.slots = SuperArray(17)
        self.length = 16
        self.PRIME = 31
        self.index = 0

    def __getitem__(self, key):
        hash_value_of_key = self.hash(key)
        index = hash_value_of_key % self.length
        if type(self.slots[index]) is not type(0.0) and self.slots[index].key == key:
            return self.slots[index].value
        else:
            return None

    def __setitem__(self, key, value):
        hash_value_of_key = self.hash(key)
        bucket = hash_value_of_key % self.length
        self.slots[bucket] = SuperNode(key, value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 17:
            self.index = 0
        try:
            while self.slots[self.index] == 0.0 and self.index < 17:
                self.index += 1
            next_to_return = self.slots[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return next_to_return

    def __contains__(self, item):
        return item in self.keys()

    def items(self):
        for node in self:
            yield node.key, node.value

    def keys(self):
        for node in self:
            yield node.key

    def values(self):
        for node in self:
            yield node.value

    def hash(self, key):
        return hash(key)
        hash_value = 13
        for char in key:
            hash_value = (self.PRIME * hash_value + ord(char))

        return hash_value


class SuperNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.key}: {self.value}"

class RPSInfo:
    utilityFunc = [[0, -1, 1],  # Rock
                   [1, 0, -1],  # Paper
                   [-1, 1, 0]]  # Scissors

    @staticmethod
    def return_column(x):
        array = SuperArray(3)
        for row in range(3):
            array[row] = RPSInfo.utilityFunc[row][x]
        return array
