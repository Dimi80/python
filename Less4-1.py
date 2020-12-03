# зарплата_запуск скрипта с параметрами_cmd.exe
from sys import argv
resourse, hours, rate, prize, salary = argv
salary = float(hours) * float(rate) + float(prize)
print("Выработка в часах, ч: ", hours)
print("Ставка в час, руб./ч: ", rate)
print("Премия, руб.: ", prize)
print("Зарплата, руб. ", salary)
# python less4-1.py 200 100 100 salary