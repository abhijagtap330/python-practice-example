
def comman_element(list1,list2):
    
    set1 = set(list1)
    set2 = set(list2)
    
    comman_values = set1.intersection(set2)
    
    total = sum(comman_values)
    
    return comman_values, total

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(comman_element(list1,list2))

list3 = list1 + list2
print(list3)
