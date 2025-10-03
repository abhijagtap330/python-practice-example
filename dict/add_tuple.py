def add_tuple(d, key_tuple,values):
    
    d[values] = key_tuple
    
    return d
    
my_dict = {'a': 100, 'b': 200, 'c': 300}

# Define a tuple to use as a key and a value
key_tuple = (1, 2, 3)
value = 'E','x','mple'

print(add_tuple(my_dict,key_tuple,value))

string = '-'.join(value)
print(string)