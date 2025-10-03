def min_max(dict):
    
    max_values = float()
    min_values = float('inf')
    
    for i in dict.values():
        
        if i > max_values:
            max_values = i
        if i < min_values:
            min_values = i
            
    return (min_values,max_values)


# Define the dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 5,
    'd': 15,
    'd': 15
}

print(min_max(my_dict)) 

dict1 = {"name":"mradul","age":23,"city":"indore"}

def remove_duplicates(dict):
    seen = set()
    unique = {}
    
    for key, value in dict.items():
        if value not in seen:
            seen.add(value)
            unique[key] = value
    return unique

