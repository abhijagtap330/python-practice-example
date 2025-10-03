arr = [2, 3, 1, 20, 15]
k = 4

def number_of_smallest(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[k-1]

print(number_of_smallest(arr, k))