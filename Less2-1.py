# список
orig_list = ['Python', 23, 6.54, '823.7', None, 48]
print('Исходный список: ', orig_list)
new_list = []
for el in orig_list:
    new_list.append(type(el))
print('Типы элементов исходного списка: ', new_list)