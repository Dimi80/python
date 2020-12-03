# числа больше предыдущих из списка
my_list = [2, 32, 2, -5456, 7, 56, 7, 890, 6, 5, 4, 7, 565]
print(my_list)
numb_my = len(my_list)
ind_list = [ind for ind in range(0, numb_my) if my_list[ind] > my_list[ind - 1] and ind != 0]
orig_list = [my_list[el] for el in ind_list]
print(orig_list)
#решение: new_list = [my_num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]