# создание файла txt с построчным вводом данных
f = open("my_text.txt", 'w')
my_text = []
my_str = 0
while my_str != '':
    my_str = input('Введите данные строки: ')
    if my_str == '':
        for line in my_text:
            f.write(line + '\n')
        f.close()
        exit(0)
    my_text.append(my_str)