def sym_pair(array, sum_num):
    pairs = []
    # Iterate through the array
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            # Check if the sum of the pair equals the specified sum
            if array[i] + array[j] == sum_num:
                pairs.append((array[i], array[j]))  # Append the pair as a tuple
    return pairs

# Example list and sum
list1 = [2, 4, 5, 6, 7, 8, 9, 50, 50, 1, 2, 4]

# Find and print pairs that sum to 10
print(sym_pair(list1, 100))
