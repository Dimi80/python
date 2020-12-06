# фирмы_прибыль_убытки
import json
d_new = {}
fin_list = []
average = 0
profit_sum = 0
ind = 0
with open('task7.txt', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        key = line[0]
        profit = int(line[2]) - int(line[3])
        d_new[key] = profit
        profit_sum = profit_sum + profit
        if profit > 0:
            average = average + profit
            ind += 1
average_profit = {'average_profit': int(average / ind)}
fin_list.append(d_new)
fin_list.append(average_profit)
print(fin_list)
with open("task7.json", "w", encoding='utf-8') as write_f:
    json.dump(fin_list, write_f)