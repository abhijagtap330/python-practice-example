def combine_dicts(d1, d2):
    # Create a new dictionary to hold the combined results
    combined = {}

    # Iterate through the first dictionary and add its items to the combined dictionary
    for key in d1:
        combined[key] = d1[key]

    # Iterate through the second dictionary
    for key in d2:
        if key in combined:
            # If the key is already in the combined dictionary, add the values
            combined[key] += d2[key]
        else:
            # If the key is not in the combined dictionary, add it
            combined[key] = d2[key]

    return combined

# Define the dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine the dictionaries
result_dict = combine_dicts(d1, d2)

# Print the result
print("Combined dictionary:", result_dict)