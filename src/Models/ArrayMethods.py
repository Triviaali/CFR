class ArrayMethods:
    def clip(self, array, min):
        clippedResult = []
        for x in array:
            if x > min:
                clippedResult.append(x)
            else:
                clippedResult.append(min)

        return clippedResult

    def zeros(self, length):
        return [0.0 for x in range(length)]

    def sum(self, array):
        sum = 0
        for x in array:
            sum += x
        return sum

    def repeat(self, element, times):
        result = [element for x in range(times)]
        if type(result[0]) == list:
            flat_list = []
            for sublist in result:
                for item in sublist:
                    flat_list.append(item)
            return flat_list
        return result

    def arrayAdd(self, array1, array2):
        temp = []
        for x in range(len(array1)):
            temp.append(array1[x] + array2[x])
        return temp

    def arrayMultiply(self, array1, array2):
        temp = []
        for x in range(len(array1)):
            temp.append(array1[x] * array2[x])
        return temp

    def divideAll(self, array, divisor):
        for x in range(len(array)):
            array[x] /= divisor
        return array

    def multiplyAll(self, array, multiplier):
        temp = array
        for x in range(len(array)):
            temp[x] = array[x] * multiplier
        return temp

    def substractAll(self, array, num):
        temp = array
        for x in range(len(array)):
            temp[x] = array[x] - num
        return temp

    def getColumnAsList(self, twoDArray, column):
        list = []
        for x in range(3):
            list.append(twoDArray[x][column])

        return list
