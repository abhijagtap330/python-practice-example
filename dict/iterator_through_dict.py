def single_output(dict):
    
    for key, inner_dict in dict.items():
        
        print(key)
        
        for sub_key, sub_values in inner_dict.items():
            
            print(f"{sub_key}:{sub_values}")
            
# Define the dictionary
students = {
    'Aex': {'class': 'V', 'rolld_id': 2},
    'Puja': {'class': 'V', 'roll_id': 3}
}

print(single_output(students)) 