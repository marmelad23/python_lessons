my_list = [1, 8, 8, 2, 3, 2, 4, 10, 4, 5]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)