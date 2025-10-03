def binary_search(arr, target, low, high):
    
    mid = (high + low) // 2
    # print(mid)
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)
    return -1
    
    
arr = [1,2,6,7,8,9]
target = 2

print(binary_search(sorted(arr), target, 0, len(arr) -1))