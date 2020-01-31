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
        return [0 for x in range(length)]

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
        for x in range(len(array1)):
            array1[x] += array2[x]
        return array1

    def divideAll(self, array, divisor):
        for x in range(len(array)):
            array[x] /= divisor
        return array

    def substractAll(self, array, num):
        for x in range(len(array)):
            array[x] -= num
        return array

    def getColumnAsList(self, twoDArray, column):
        list = []
        for x in range(3):
            list.append(twoDArray[x][column])

        return list
