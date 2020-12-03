# числа, кратные 20 или 21
my_list = [i for i in range(20, 240, 1)]
print('Исходный список - 20...240 шаг =1', my_list)
krat = input('Введите целое число в пределах 1...240: ')
if krat < '1' or krat > '240' or float(krat % 1) != 0:
    print('Введены некорректные данные. Начните заново.')
    exit(0)
krat_list = [el for el in my_list if el % int(krat) == 0]
print('Список кратных чисел в пределах - 20...240: ', krat_list)