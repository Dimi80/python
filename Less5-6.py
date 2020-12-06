# словарь из файла
d_orig = {}
d_new = {}
with open("task6.txt", encoding='utf-8') as f:
    for line in f:
        key, *value = line.split()
        d_orig[key] = value
        sum_val = 0
        for el in value:
            el = str(el).split('(')
            if el[0] == '-':
                el[0] = 0
            sum_val = sum_val + int(el[0])
        d_new[key] = sum_val
print(d_new)