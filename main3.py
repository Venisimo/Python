var1 = None
dict2 = dict()
def a(var1, p2):
    return var1+p2
print(a(2, 2))

def b(p1, p2):
    return p1*p2
print(b(3, 3))

def c(p1, p2):
    if p2 == 0:
        return 0
    return p1 / p2
print(c(2, 0))

def d(val):
    return type(val)
print(d(dict()))

def e(val):
    t = type(val)
    if t == str:
        return "t, строка"
    elif t == int:
        return "Целое число"
    elif t == list:
        return "Список"
    else:
        return 'неизвестный тип данных'
print(e(2.2))