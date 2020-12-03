# формирование списка с последующим перемножением элементов
from functools import reduce
print('Вводите целые числа для формирования списка')
a = input('Введите первый элемент списка: ')
b = input('Введите последний элемент списка: ')
c = input('Введите шаг списка: ')
my_lyst = [el for el in range(int(a), int(b) + 1, int(c))]
cmpstn_all = reduce(lambda x, y: x * y, my_lyst)
print('Сформирован список значений: ', my_lyst)
print('Произведение всех составляющих сформированного списка: ', cmpstn_all)