# сотрудники_оклады
with open("task3.txt", encoding='utf-8') as f:
    f_str = 0
    oklad_min = []
    oklad_sum = 0
    for line in f:
        f_str += 1
        line = line.split()
        oklad_sum = oklad_sum + int(line[1])
        if int(line[1]) < 20000:
            oklad_min.append(line[0])
    print('Сотрудники с окладом менее 20000: ', oklad_min)
    print('Средний оклад: ', oklad_sum / f_str)