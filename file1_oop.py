class First:
    q = 'first'
    def __int__(self):
        q = 'second init'
    def a(self):
        print(self.q)

class Second:
    q = 'second'
    def __int__(self):
        e = 123
    @staticmethod
    def a():
        print('Method a from class Second')

class One:
    """
    Это класс One для чего-то
    """
    def __init__(self):
        self.one_var = 'value from class One'
    def a(self):
        """
        Это метод для чего-то
        """
        print('method a into class One')
class Two(One):
    def b(self):
        print('method b into class two')


obj_first = First()
obj_second = Second()

First.q = 'qwe'
#a1 = First()
a1 = Two()
a1.a()
print(a1.one_var)
#a1.x = 10
#a1.y = 20
#print(a1.x, a1.y, a1.q)

#b1 = First()
#b1.x = 30
#b1.y = 40
#print(b1.x, b1.y)

c1 = Second()
d1 = Second()

obj_first.a()
obj_second.a()