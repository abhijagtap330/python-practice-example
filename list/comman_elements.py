def comman_elements_true(l1,l2):
    comman = []
    for i in l1:
        for j in l2:
            if i == j:
                return False
    return True

# Example usage
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1,2]
list2 = [4, 5, 6, 7, 8]
list3 = [10, 20, 30]

print(comman_elements_true(list1, list2)) 
# print(comman_elements(list1, list3))

def common_elements(l1, l2):
    common = []
    for i in l1:
        if i in l2 and i not in common:
            common.append(i)
    return common

print(common_elements(list1, list2)) 

