# большая буква
def int_func(word):
    return word.capitalize()
my_words = input('Введите несколько слов строчными буквами латиницей через пробелы: ')
check_letter = set('qwertyuiopasdfghjklzxcvbnm ')
if all(lttr in check_letter for lttr in my_words) == False:
    print('Введены не корректные символы. Попробуйте начать заново.')
    exit(0)
my_words = my_words.split()
new_words = []
for word in my_words:
    word = int_func(word)
    new_words.append(word)
print('Преобразовано: ', *new_words)