# сложение Х + ХХ + ХХХ
number = input('Введите число: ')
number = float(number)
if int(number) < 0:
    print('Необходимо ввести положительное число!')
    exit(0)
if (number % 1) > 0:
    print('! введённое число округлено до: ', int(number))
number = str(int(number))
num_1 = number
print('число_1: ', num_1)
num_2 = number + number
print('число_2: ', num_2)
num_3 = number + number + number
print('число_3: ', num_3)
num_sum = int(num_1) + int(num_3) + int(num_3)
print(num_1, '+', num_2, '+', num_3, '=', num_sum)