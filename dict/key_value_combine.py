keys = ['red', 'green', 'blue', 'sky_blue'] 
values = ['#FF0000','#008000', '#0000FF', "#2A6AAA"] 

def combined_key_value(keys,values):
    
    combined = dict(zip(keys,values))
    
    return combined

print(combined_key_value(keys,values))