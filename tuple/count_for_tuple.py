def count_frequencies(tup):
    # Create an empty dictionary to hold frequency counts
    frequency = {}
    
    # Iterate through each item in the tuple
    for item in tup:
        if item in frequency:
            # Increment the count for existing item
            frequency[item] += 1
        else:
            # Add new item to the dictionary with count 1
            frequency[item] = 1
    
    return frequency

# Define a tuple
my_tuple = (1, 'apple', 2, 'apple', 3, 1, 2, 1)

# Find the frequency of each item
frequencies = count_frequencies(my_tuple)

# Print the result
print("Frequency of items in the tuple:")
for item, count in frequencies.items():
    print(f"{item}: {count}")

        