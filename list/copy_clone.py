#Approach 1

# my_list=[12,34,55,65]
# my_list2=my_list.copy()
# print(my_list2)

#Approach 2
# my_list=[12,34,55,65]
# my_list_copy=[12,34]
# my_list_copy.extend(my_list)
#
# print(my_list_copy)

#Approach 3

# my_list=[12,34,55,65]
# my_list_copy = list(my_list)
# print(my_list_copy)

#Approach 4

my_list=[12,34,55,65,89]
my_list_copy=[i for i in my_list]

print(my_list_copy)

