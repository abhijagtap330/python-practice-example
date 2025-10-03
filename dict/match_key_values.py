def key_values(dict1,dict2):
    
    for key in dict1:
        
        if key in dict2 and dict1[key] == dict2[key]:
            return f"{key}:{dict1[key]} are in both dict"
 
# Sample dictionaries
dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}
           
print(key_values(dict1,dict2))