import math
class A:
    def __init__(self, obj):
        self.obj = obj
    def return_obj(self):
        return self.obj
class B(A):
    def get_obj_type(self):
        return type(self.obj)
    def get_sqrt(self):
        dt = self.get_obj_type()
        if dt == int:
            return math.sqrt(self.obj)
        elif dt == float:
            return math.sqrt(self.obj)
        else:
            print('error')
    def get_array_size(self, t='size'):
        dt = self.get_obj_type()
        summa = 0
        more = 0
        if dt == list or dt == tuple:
            if t == 'size':
                return len(self.obj)
            elif t == 'sum':
                for i in self.obj:
                    summa += i
                return summa
            elif t == 'more':
                return max(self.obj)
        return tuple()
class C(B):
    """
    наследует A и B
    """
    pass
if __name__ == '__main__':
    a1 = B(obj=[1, 2, 3])
    print(a1.return_obj())
    print(a1.get_sqrt())
    print(a1.get_array_size(t='sum'))