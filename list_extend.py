def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    
    # Add any remaining elements
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])
    
    return merged_list

# Test
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]

lst1.extend(lst2)
print(lst1)
print(merge_sorted_lists(lst1, lst2))  # Output: [1, 2, 3, 4, 5, 6]

n = 2
num = n % len(lst1)
print(num)
print(lst1[-num:] + lst1[:-num])