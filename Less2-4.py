# строка-слова
strok = input('Введите несколько слов через пробел: ').split()
num_strok = 1
for el in strok:
    print(num_strok, el[:10])
    num_strok += 1