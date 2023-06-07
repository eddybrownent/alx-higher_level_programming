#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

another_list = [1]
yangu_list = copy_list(another_list)

print(yangu_list)

print(new_list == my_list)
print(new_list is my_list)
