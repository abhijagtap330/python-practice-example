def left_rotate(arr, d):
    n = len(arr)
    # If the array is empty or the number of rotations is zero, return the original array
    if n == 0 or d == 0:
        return arr
    
    # Compute the effective rotation (in case d is greater than n)
    d = d % n
    # Rotate the array
    rotated_arr = arr[d:] + arr[:d]
    
    return rotated_arr

list1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9]
print(left_rotate(list1,4))