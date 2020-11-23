# max number
num_ent = float(input('Введите целое число: '))
if (num_ent % 1) > 0:
    print('! введённое число округлено до: ', int(num_ent))
num = abs(num_ent)
num_max = num % 10
while num > 0:
    if num_max == 9:
        print('в числе: ', num_ent, 'максимальная цифра: ', num_max)
        exit(0)
    if num % 10 > num_max:
        num_max = num % 10
    num = num // 10
print('в числе: ', num_ent, 'максимальная цифра: ', int(num_max))