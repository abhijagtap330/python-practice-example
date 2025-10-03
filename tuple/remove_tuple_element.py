def remove_element(tup, element_to_remove):
    # Create a new tuple excluding all occurrences of element_to_remove
    return tuple(item for item in tup if item != element_to_remove)

# Define the original tuple
my_tuple = (1, 'apple', 2, 'banana', 1, 'apple', 3)

# Define the element to remove
element = 'banana'

# Remove the element
new_tuple = remove_element(my_tuple, element)

# Print the result
print("Original tuple:", my_tuple)
print("Tuple after removing element:", new_tuple)