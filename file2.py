import math
from file1 import a as q, mn


def a():
    pass


def c():
    num1 = q()
    num2 = mn()
    if num2 == 0:
        return 0
    else:
        return num1 / num2


def d():
    num1 = q()
    num2 = mn()
    return num1 * num2


def square():
    result = d()
    return math.sqrt(result)


def e():
    n5 = int(input('Введите число 1: '))
    n6 = int(input('Введите число 2: '))
    n7 = int(input('Введите число 3: '))
    return (n5 + n6 + n7) / 3

def f():
    n5 = int(input('Введите число 1: '))
    n6 = int(input('Введите число 2: '))
    n7 = int(input('Введите число 3: '))
    if n5 < n6:
        if n5 < n7:
            return n5
    elif n6 < n5:
        if n6 < n7:
            return n6
    elif n7 < n5:
        if n7 < n6:
            return n7


