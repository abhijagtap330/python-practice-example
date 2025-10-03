
def second_largest(array):
    second = sorted(set(array),reverse=True)
    print(second) 
    return second[1]

list1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9]
print(second_largest(list1))

