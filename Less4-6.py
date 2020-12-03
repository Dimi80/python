# итераторы
from itertools import count
from itertools import cycle
a = input('Введите начальное значение для итератора COUNT: ')
b = input('Введите количество повторений для итератора COUNT: ')
i = 1
for el in count(int(a)):
    if i <= int(b):
        print(el)
        i += 1
    else:
        a = input('Введите повторяющиеся элементы для итератора CYCLE: ').split()
        b = input('Введите количество повторений для итератора CYCLE: ')
        i = 1
        for el in cycle(a):
            if i <= int(b):
                print(el)
                i += 1
            else:
                exit(0)