string = "Abhijeet"
string1 = "Jagtap"

x = [char for char in string]
y = [char for char in string1]

join_elements = [x+y for x,y in zip(x,y)]

print(join_elements) 

def validate_first_element(string):
    x = [char for char in string]
    first_element = list(x[0])
    # if first_element == 'A':
    #     print("First char is A")
    # else:
    #     print("First char is not A")
    return first_element

print(validate_first_element(string1))