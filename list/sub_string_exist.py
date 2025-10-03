def contains_sublist(main_list, sublist):
    sublist_len = len(sublist)
    for i in range(len(main_list) - sublist_len + 1):
        if main_list[i:i + sublist_len] == sublist:
            return True
    return False

# Example usage
main_list = [1, 2, 3, 4, 5]
sublist = [3, 4]
print(contains_sublist(main_list, sublist))  # Output: True


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

def difference_between(l1, l2):
    # difference = []
    # for i in l1:
    #     if i not in l2:
    #         difference.append(i)
    
    return list(set(list1) - set(list2))

print(difference_between(main_list,sublist))