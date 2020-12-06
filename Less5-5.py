# сумма чисел в файле
f = open('my_numbers_task5.txt', 'w')
numbers = input('Введите несколько чисел через пробел: ')
f.write(numbers + '\n')
numbers = numbers.split()
num_sum = 0
for el in numbers:
    num_sum = num_sum + int(el)
f.write('Сумма введённых чисел = ' + str(num_sum))
f.close()
print('Сумма введённых чисел = ', num_sum)