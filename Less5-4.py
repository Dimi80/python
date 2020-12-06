# one-two-three
num_rus = ['Один', 'Два', 'Три', 'Четыре']
f_eng = open("task4.txt", 'r')
i = 0
with open('task4_rus.txt', 'w') as f_rus:
    for line in f_eng:
        line = line.split()
        line = (num_rus[i] + ' - ' + line[2] + '\n')
        f_rus.writelines(line)
        i += 1
f_eng.close()