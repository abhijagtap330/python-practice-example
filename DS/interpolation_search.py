def interpolation_search(arr, x):
    """
    Perform interpolation search on a sorted array 'arr' to find the index of 'x'.
    
    :param arr: Sorted list of elements
    :param x: The element to search for
    :return: The index of the element x if present, otherwise -1
    """
    low = 0
    high = len(arr) - 1
    
    # Loop while the element is within the range of the array
    while low <= high and arr[low] <= x <= arr[high]:
        # Calculate the probe position
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        # Check if the element at position is the target element
        if arr[pos] == x:
            return pos
        # If the target is smaller, move the 'high' pointer
        elif arr[pos] > x:
            high = pos - 1
        # If the target is larger, move the 'low' pointer
        else:
            low = pos + 1
    
    # If the element is not found
    return -1

# Example usage
arr = [10, 12, 20, 32, 35, 40, 45, 50, 70, 80, 90]
x = 35

result = interpolation_search(arr, x)

if result != -1:
    print(f"Element {x} found at index {result}.")
else:
    print(f"Element {x} not found in the array.")
