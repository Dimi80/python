# выручка - издержки
proceeds = float(input("Введите величину выручки, млн руб.: "))
costs = float(input("Введите величину издержек, млн руб.: "))
profit = (proceeds - costs)
if profit < 0:
    rezult = 'отрицательный'
elif profit > 0:
    rezult = 'положительный'
    num_emp = (input("Введите количество сотрудников (целое положительное число), чел.: "))
    if ((float(num_emp) % 1) > 0) or (float(num_emp) <= 0):
        print('Вы ввели недопустимое значение! Начните программу заново.')
        exit(0)
    num_emp = int (num_emp)
    print('Прибыль на каждого сотрудника составляет, тыс. руб./чел.: ', float(profit / num_emp))
else:
    rezult = 'нулевой'
print('Финансовый результат - ', rezult, ', составляет: ', profit, 'млн руб.')