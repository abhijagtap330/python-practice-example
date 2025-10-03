def largest_number(number):
    largest = number[0]
    
    for i in number:
        if i > largest:
            largest = i
    return largest

list1 = [12,114,143,155]
print(largest_number(list1))


