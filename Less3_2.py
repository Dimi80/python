# данные пользователя_именованые арг
def my_data(my_name, my_surname, birth_year, city, email, phone_numb):
    print(f"Имя: {my_name:<7}; Фамилия: {my_surname:<7}; Год рождения: {birth_year:<7}; Город проживания: {city:<7}; Электронная почта: {email:<7}; Телефонный номер: {phone_numb:<7}")
print("Введите ЧЕРЕЗ ПРОБЕЛ Ваши данные:")
print("1) Имя, 2) Фамилия, 3) Год рождения, 4) Город проживания, 5) Электронная почта, 6) Телефонный номер")
data_str = input(">>>").split()
if len(data_str) < 6:
    print("Недостаточно исходных данныхю. Запустите программу сначала")
    exit(0)
elif len(data_str) > 6:
    print("Избыток исходных данныхю. Запустите программу сначала")
    exit(0)
my_name, my_surname, birth_year, city, email, phone_numb = data_str
print(my_data(my_name, my_surname, birth_year, city, email, phone_numb))