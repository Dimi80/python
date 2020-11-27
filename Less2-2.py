# обмен соседних
orig_list = input('Введите исходный список через пробел: ').split()
numb_elem = len(orig_list)
if numb_elem == 1:
    print('Ничего делать не надо: введён один элемент.')
    exit(0)
new_list = []
print('Исходный список: ', orig_list)
for el in range(0, numb_elem // 2):
    new_list.append(orig_list[2 * el + 1])
    new_list.append(orig_list[2 * el])
if (numb_elem % 2) > 0:
    new_list.append(orig_list[2 * el + 2])
print('Результат обмена соседей в исходном списке: ', new_list)