def delete_key(dict,key_to_remove):
    
    delete_key = dict.pop(key_to_remove, None)
    
    return delete_key

my_dict = {
    'a': 12,
    'b': 14,
    'c': 17,
    'd': 80
}

key_to_remove = 'c'
print(delete_key(my_dict,key_to_remove))
print(my_dict)