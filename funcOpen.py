def func1():
    a = open('file2.txt', 'x')
    b = open('file2.txt', 'w')
    b.write('hello\neveryone')
    b.close()
    c = open('file2.txt')
    print(c.read())
    c.close()
#func1()
def func2():
    with open('file2.txt', 'rb') as f:
        print(f.read())
    with open('file3.txt', 'x') as a:
        with open('file3.txt', 'w+b') as b:
            b.write(bytes('строка1\nстрока2', 'cp1251'))
    with open('file3.txt', 'rb') as c:
        print(c.read())
#func2()

def func4():
    with open('file4.txt', 'w+') as f:
        f.write('s1\ns2\ns3\ns4')
        with open('file4.txt', 'r') as f2:
            print(f2.read())
#func4()

def func5():
    with open('file4.txt', 'r') as f:
        print(f.readlines())
#func5()

def example():
    with open('file4.txt', 'r') as f:
        a = f.readlines()
        num = 0
        for i in a:
            num += 1
            print('Строка №', num, 'Текст:', i)
example()