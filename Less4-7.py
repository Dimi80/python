# yield_факториал
from math import factorial
def fctrl(n):
    for i in range(1, n):
        yield factorial(i)
n = input('Введите конечное число для расчёта факториала: ')
a = fctrl(int(n)+1)
for b in a:
    print(b, end = '; ')