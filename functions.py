from functools import reduce

def square(x):
    return x ** 2

def increment(x):
    return x + 1

def wrapper(func, array):
    result = []

    for i in array:
        result.append(func(i))
    return result

lst = list(range(10))
print(lst)
print(list(map(lambda x: x**2, lst)))
print(list(map(lambda x: x+1, lst)))

def mult(x, y):
    return x * y

def sum1(x, y):
    return x + y

def wrapper(func, array):
    result = array[0]

    for i in array[1:]:
        result = func(result, i)
    return result

lst = list(range(1, 11))
print(lst)
print(reduce(lambda x, y: x+y, lst))
print(reduce(lambda x, y: x*y, lst))
