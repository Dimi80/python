# сумма 2-х наибольших_позиционные арг
def my_func(var1, var2, var3):
    return (var1 + var2 + var3 - min(var1, var2, var3))
print('Сумма двух наибольших чисел: ', my_func(-10, 11, 100))