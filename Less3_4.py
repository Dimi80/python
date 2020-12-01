# возведение в степень
def my_func():
    x = float(input('Введите действительное положительное число >0 X: '))
    if x <= 0:
        print('Данные по Х введены некорректно. Начните сначала.')
        exit(0)
    y = float(input('Введите целое отрицательное число < 0 Y: '))
    if y >= 0 or (y % 1) != 0:
        print('Данные по Y введены некорректно. Начните сначала.')
        exit(0)
    i = 1
    x_result = x
    while i < abs(y):
        x_result = x_result * x
        i += 1
    return 1 / x_result
print(my_func())