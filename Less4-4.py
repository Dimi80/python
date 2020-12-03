# последовательность неповторяющихся чисел
my_list = [1, 2, 3, 4, 423, 4343, 1, 2, 12, 2, 3, 323, 323, 423]
new_list = [el for el in my_list if my_list.count(el) == 1]
print('Исходный список чисел: ', my_list)
print('В списке не повторяются числа: ', new_list)