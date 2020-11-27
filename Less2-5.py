# рейтинг
reiting = [9, 8, 8, 7, 6, 6, 6, 4, 1, -5]
print('Исходный список: ', reiting)
num_reiting = len(reiting)
new_numb = float(input('Введите число: '))
i = 0
for el in reiting:
    if new_numb <= (min(reiting)):
        reiting.append(new_numb)
        print('Новый список: ', reiting)
        exit(0)
    if new_numb > int(el):
        reiting.insert(i, new_numb)
        print('Новый список: ', reiting)
        exit(0)
    i +=1