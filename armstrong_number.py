def armstrong_number(num):
    
    string_number = str(num)
    num_digit = len(string_number)
    
    sum_of_power = sum((int(i) ** num_digit for i in string_number))
    
    return sum_of_power==num

print(armstrong_number(1532))