# деление
def my_dvsn(arg1, arg2):
    return arg1 / arg2
arg1 = float(input('Введите числитель: '))
arg2 = float(input('Введите знаменатель: '))
while arg2 == 0:
    print("Деление на ноль!")
    arg2 = input('Введите значение знаменателя, отличное от нуля, либо "Enter" - для выхода: ')
    if arg2 == '':
        print("Завершено пользователем. Без результата.")
        exit(0)
    arg2 = float(arg2)
print('Результат: ', arg1, '/', arg2, '=', my_dvsn(arg1, arg2))