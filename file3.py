from file1 import a, mn
from file2 import c, d, square, e as mid, f
def main():
    print('1 - сложение, 2 - вычитание, 3 - деление, 4 - умножение, 5 - квдрат числа, 6 - среднее значение, 7 - naibolshee chislo')
    user_input = int(input('Введите число: '))
    if user_input == 1:
        print(a())
    elif user_input == 2:
        print(mn())
    elif user_input == 3:
        print(c())
    elif user_input == 4:
        t = d()
        print(t)
    elif user_input == 5:
        square()
        print(square())
    elif user_input == 6:
        print(mid())
    elif user_input == 7:
        print(f())
    else:
        print('такого числа в списке нет')
main()