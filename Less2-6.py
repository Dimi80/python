# товары
q = 1
i = 1
new_list = []
name_list = []
price_list = []
quantity_list = []
while q == 1:
    print('Товар №', i)
    name = input('Введите наименование: ')
    price = input('Введите цену: ')
    quantity = input('Введите цену: ')
    product = (i, {"Наименование": name, "Цена": price, "Количество": quantity})
    new_list.append(product)
    name_list.append(name)
    price_list.append(price)
    quantity_list.append(quantity)
    q = input('Для выхода нажмите "0", для продолжения - любую клавишу: ')
    if q == '0':
        for el in new_list:
            print(el)
        print('Аналитика:')
        print('Наименование: ', name_list)
        print('Цена: ', price_list)
        print('Количество: ', quantity_list)
        exit(0)
    else:
        q = 1
        i +=1


