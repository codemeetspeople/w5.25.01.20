class Point:
    __slots__ = ['__x', '__y']

    def __init__(self, x=0, y=0):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = float(value)

    @y.setter
    def y(self, value):
        self.__y = float(value)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

if __name__ == '__main__':
    point = Point()
    print(point)
