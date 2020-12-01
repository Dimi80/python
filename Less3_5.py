# сумма чисел
q = 1
my_summa = 0
while q == 1:
    numbers = input('Введите несколько чисел через пробел: ').split()
    for el in numbers:
        if el.isdigit():
            el = float(el)
            my_summa += el
        else:
            print('Сумма введённых чисел = ', my_summa)
            exit(0)
    print('Сумма введённых чисел = ', my_summa)
    q = input('Для выхода нажмите "0", для продолжения - любую клавишу: ')
    if q != '0':
        q = 1