# подсчёт кол-ва строк и кол-ва слов в строке
with open("task2.txt") as f_2:
    f_2_str = 0
    for line in f_2:
        f_2_str += 1
        line = line.split()
        print('Строка ', f_2_str , 'Количество слов: ', len(line))
    print('Количество строк в файле: ', f_2_str)