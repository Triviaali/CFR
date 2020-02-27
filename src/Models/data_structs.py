
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
