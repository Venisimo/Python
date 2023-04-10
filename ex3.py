def spisok():
    lst = [3, 10, 2]
    for i in range(len(lst)):
        print(lst[i])
    return lst
print(spisok())

def spisok2():
    slst = [[3, 5, 7], [6,7, 9]]
    print(slst[1][2])
print(spisok2())

def dct1():
    d = dict()
    d = {'k': 20, 2: 5, 'randomKey': 'a', 3: 3}
    for key in d.keys():
        print(d.get(key))
print(dct1())