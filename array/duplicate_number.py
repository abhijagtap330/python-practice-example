def duplicate_number(array):
    dupli = []
    for i in range(1,100):
        if array.count(i) > 1:
            dupli.append(i)
    return dupli

array = [2, 4, 5, 6, 7, 8, 9, 10, 10, 1, 2, 4]
print(duplicate_number(array))




