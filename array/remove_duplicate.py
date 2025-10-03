list1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9]

def remove_duplicate(array):
    unique_number = []
    seen = set()
    
    for i in array:
        if i not in seen:
            unique_number.append(i)
            seen.add(i)
    return unique_number


print(list1)
print(remove_duplicate(list1))