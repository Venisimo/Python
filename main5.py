def task1():
    lst1 = [1, 2, 3, 4, 5, 6]
    summa = 0
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            summa += lst1[i]
    print(summa)
#task1()

def task2():
    lst2 = [3, 7, 10]
    summa = 0
    for i in range(len(lst2)):
        summa += lst2[i]
    print(summa)
#task2()

def task3():
    lst1 = []
    lst3 = [1, 2, 3, 4, 5, 6]
    for i in range(len(lst3)):
        if lst3[i] % 2 != 0:
            lst1.append(lst3[i])
    print(lst1)
#task3()

def task4():
    lst1 = [2, 4, 6, 8, 1, 1, 1]
    lst2 = [2, 9, 1, 2, 6]
    lst3 = []
    l1 = len(lst1)
    l2 = len(lst2)
    if l2 > l1:
        for i in range(l2 - l1):
            lst1.append(0)
    elif l1 > l2:
        for i in range(l1 - l2):
            lst2.append(0)
    lst3.append(lst1)
    lst3.append(lst2)
    print(lst3)
    return lst3
#task4()

def task5(x):
    lst4 = []
    for i in range(len(x[0])):
        lst4.append(x[0][i] + x[1][i])
    print(lst4)
#task5(task4())

def task6():
    dct1 = {"a": 14, "b": 5, "c": 3}
    minimum = dct1["a"]
    for key, value in dct1.items():
        if minimum > value:
            minimum = value
    print(key)
#task6()

def task7():
    lst1 = [1, 2, 3, 4, 0, 9]
    minimum = lst1[0]
    for i in range(len(lst1)):
        if minimum > lst1[i]:
            minimum = lst1[i]
    print(minimum)
task7()