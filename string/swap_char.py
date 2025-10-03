string = 'Abhijeet'

single_string = [char for char in string]
print(single_string)

reverse_list = single_string[::-1]
print(reverse_list)

single_string[0], single_string[-1] = single_string[-1], single_string[0]
print(single_string)

list1 = [1, 4, 5, 7, 8]
countor = 0
for i in list1:
    countor += 1
print(countor)

