class Integer:
    def __init__(self, value=0):
        self.value = int(value)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.value + int(other.value))

    def __str__(self):
        return f'{self.__class__.__name__}: {self.value}'

class Float:
    def __init__(self, data):
        self.data = float(data)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.data + float(other.data))

    def __radd__(self, other):
        if isinstance(other, Integer):
            return Integer(self.data + float(other.value))
        return NotImplemented


    def __str__(self):
        return f'{self.__class__.__name__}: {self.data}'


if __name__ == '__main__':
    i1 = Integer(5)
    f2 = Float(8)

    print(i1 + f2)
