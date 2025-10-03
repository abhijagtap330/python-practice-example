def missing_number(array):
    expected_array = sum(range(1,100))
    sum_array = sum(array)
    print(expected_array, sum_array)
    return (expected_array - sum_array)

array = [i for i in range(1,100) if i not in [1,3,7]]

print(missing_number(array))

# def find_missing_number(array):
#     # Number of elements in the array including the missing number
#     n = 100
    
#     # Calculate the expected sum of numbers from 1 to 100
#     expected_sum = n * (n + 1) // 2
    
#     # Calculate the actual sum of numbers in the array
#     actual_sum = sum(array)
    
#     # The missing number is the difference between expected and actual sum
#     missing_number = expected_sum - actual_sum
    
#     return missing_number

# print(find_missing_number(array))
    